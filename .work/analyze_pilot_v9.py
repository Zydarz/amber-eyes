"""Phan tich PILOT v9 — giong mau moi vai D (khan tram) + C (trong sac) sau khi Higgs clone.

Input : .work/kaggle_higgs/out_higgs_v9/ (tai ve tu Kaggle, manifest + wav)
        .work/kaggle_higgs/out_higgs_prod/out_higgs_prod/ (moc so sanh H, N1, N2 cua luot san xuat)
Output: .work/pilot_v9_result.json + .work/pilot_v9_result.txt

Do:
  * F0 clone 2 thuat toan: AC (voice_audition.f0_median) + YIN (voxcpm_yin_f0.yin)
  * toc do (am tiet/giay), khoang lang trong cau (-50 dB) > 0.3 s, dinh
  * CER: ASR listen_audio luot 1 moi file; luot 2 cho file > 2% (Q6). Cau bi chan (Q3b) -> loai
  * G9: MOI cap vai ke ca khac gioi, DAT khi CA HAI thuat toan >= 4 nua cung
  * G8: F0 theo cam xuc trong tung clip

Usage: python .work/analyze_pilot_v9.py [--cer] [--tag v10]
"""
import argparse
import itertools
import json
import math
import pathlib
import re
import subprocess
import sys
import wave
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from voice_audition import f0_median as f0_ac  # noqa: E402
from voxcpm_yin_f0 import yin  # noqa: E402
import vi_cer  # noqa: E402

V9 = HERE / "kaggle_higgs" / "out_higgs_v9"
PROD = HERE / "kaggle_higgs" / "out_higgs_prod" / "out_higgs_prod"
CACHE = HERE / "kaggle_higgs" / "_asr_cache_v9"
NC_MIN = 4.0
CER_MAX = 0.02
BLOCK = re.compile(r"This request was blocked|blocked by|safety", re.I)
BASE_REFS = {"H": "H.wav", "N1": "W6_LOW.wav", "N2": "W5_HIGH.wav"}
N_BASE_H = 40          # so file H san xuat dung lam moc (deu theo thu tu)


def read_wav(p):
    with wave.open(str(p), "rb") as w:
        sr, nch = w.getframerate(), w.getnchannels()
        a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    if nch > 1:
        a = a.reshape(-1, nch).mean(axis=1)
    return a, sr


def max_gap(a, sr, thr=-50.0, win=0.02):
    n = int(win * sr)
    k = len(a) // n
    db = 20 * np.log10(np.sqrt((a[:k * n].reshape(k, n) ** 2).mean(1)) + 1e-9)
    on = np.where(db > thr)[0]
    if not len(on):
        return 0.0, 0.0
    run = best = 0
    for v in db[on[0]:on[-1] + 1]:
        run = run + 1 if v <= thr else 0
        best = max(best, run)
    return best * win, (on[-1] - on[0] + 1) * win


def measure(p, text):
    a, sr = read_wav(p)
    f = yin(a, sr)
    gap, speech = max_gap(a, sr)
    syl = len(vi_cer.norm_ref(text).split())
    return {"f0_ac": round(f0_ac(a, sr), 1), "f0_yin": round(float(np.median(f)) if len(f) else 0.0, 1),
            "dur": round(len(a) / sr, 2), "gap": round(gap, 2),
            "syl_s": round(syl / speech, 2) if speech else 0.0,
            "peak_db": round(20 * math.log10(float(np.max(np.abs(a))) + 1e-12), 1)}


def nc(a, b):
    return abs(12 * math.log2(a / b)) if a and b else 0.0


def med(v):
    v = sorted(x for x in v if x)
    return float(np.median(v)) if v else 0.0


# ------------------------------------------------------------------ ASR
def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:300])
    return json.loads(r.stdout)


def asr(p, rnd):
    cf = CACHE / f"{p.stem}__r{rnd}.json"
    if cf.exists():
        return json.loads(cf.read_text(encoding="utf-8"))
    up = mcode(["upload-temp-url", str(p), "--mime-type", "audio/wav"])
    af = CACHE / f"{p.stem}__r{rnd}.args.json"
    af.write_text(json.dumps({"audio_info": {"url": up.get("temp_url"), "mime_type": "audio/wav",
                                             "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
                             ensure_ascii=False), encoding="utf-8")
    res = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)])
    cf.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    return res


def cer_round(r, rnd):
    try:
        h = asr(r["path"], rnd).get("transcription") or ""
    except Exception as e:                                  # noqa: BLE001
        return {"rnd": rnd, "err": str(e)[:200]}
    if BLOCK.search(h):
        return {"rnd": rnd, "blocked": True, "hyp": h}
    return {"rnd": rnd, "cer": round(vi_cer.cer_pair(r["text"], h), 4), "hyp": h}


def run_cer(rows):
    CACHE.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=2) as ex:
        r1 = list(ex.map(lambda r: cer_round(r, 1), rows))
    for r, a in zip(rows, r1):
        r["asr"] = [a]
    need = [r for r in rows if (r["asr"][0].get("cer") or 0) > CER_MAX]
    with ThreadPoolExecutor(max_workers=2) as ex:
        r2 = list(ex.map(lambda r: cer_round(r, 2), need))
    for r, a in zip(need, r2):
        r["asr"].append(a)
    for r in rows:
        cs = [a["cer"] for a in r["asr"] if "cer" in a]
        r["blocked"] = any(a.get("blocked") for a in r["asr"])
        r["cer_r1"] = r["asr"][0].get("cer")
        r["cer_min"] = min(cs) if cs else None      # Q6: chi tinh LOI khi CA 2 luot deu > 2%
        r["cer_fail"] = bool(cs) and min(cs) > CER_MAX


# ------------------------------------------------------------------ main
ap = argparse.ArgumentParser()
ap.add_argument("--cer", action="store_true")
ap.add_argument("--tag", default="v9")
a = ap.parse_args()
V9 = HERE / "kaggle_higgs" / f"out_higgs_{a.tag}"
CACHE = HERE / "kaggle_higgs" / f"_asr_cache_{a.tag}"

man_p = next(V9.rglob("higgs_manifest.json"))
man = json.loads(man_p.read_text(encoding="utf-8-sig"))
print("manifest:", man_p, "| OK:", sum(1 for r in man if r.get("ok")), "| FAIL:",
      sum(1 for r in man if not r.get("ok")))
rows = []
for r in man:
    if not r.get("ok"):
        continue
    p = next(V9.rglob(r["file"]), None)
    if p is None:
        print("!! thieu file", r["file"])
        continue
    rows.append({"key": r["key"], "role": r["role"], "ref": r["ref_wav"].replace(".wav", ""),
                 "emotion": r.get("emotion"), "variant": r.get("variant"), "path": p,
                 "text": r.get("text_plain") or r.get("text_sent") or "",
                 **measure(p, r.get("text_plain") or r.get("text_sent") or "")})
print("do F0 xong:", len(rows), "file v9")

# moc so sanh tu luot san xuat (cung thuat toan)
pman = json.loads(next(PROD.rglob("higgs_manifest.json")).read_text(encoding="utf-8-sig"))
base = []
for role, ref in BASE_REFS.items():
    rr = [r for r in pman if r.get("ok") and r["role"] == role and r["ref_wav"] == ref]
    if role == "H":
        rr = rr[::max(1, len(rr) // N_BASE_H)][:N_BASE_H]
    for r in rr:
        p = PROD / r["file"]
        if p.exists():
            base.append({"role": role, "ref": "PROD_" + ref.replace(".wav", ""), "emotion": r.get("emotion"),
                         **measure(p, r.get("text_plain") or "")})
print("moc san xuat:", len(base), "file")

if a.cer:
    print("ASR ...")
    run_cer(rows)

# ------------------------------------------------------------------ bang theo clip
g = defaultdict(list)
for r in rows + base:
    g[(r["role"], r["ref"])].append(r)
T = {}
for (role, ref), v in g.items():
    t = {"role": role, "ref": ref, "n": len(v), "f0_ac": round(med([x["f0_ac"] for x in v]), 1),
         "f0_yin": round(med([x["f0_yin"] for x in v]), 1),
         "syl_s": round(med([x["syl_s"] for x in v]), 2),
         "gap_gt03": sum(1 for x in v if x["gap"] > 0.3), "gap_max": max(x["gap"] for x in v),
         "peak_max": max(x["peak_db"] for x in v)}
    emo = defaultdict(list)
    for x in v:
        emo[x["emotion"]].append(x["f0_yin"])
    t["f0_by_emotion"] = {k: round(med(e), 1) for k, e in emo.items()}
    em = [m for m in t["f0_by_emotion"].values() if m]
    t["g8_spread_nc"] = round(nc(max(em), min(em)), 2) if len(em) > 1 else 0.0
    if a.cer and not ref.startswith("PROD_"):
        cs = [x for x in v if x.get("cer_min") is not None]
        t["cer_mean_r1"] = round(100 * np.mean([x["cer_r1"] for x in cs if x["cer_r1"] is not None]), 2)
        t["cer_max_min"] = round(100 * max(x["cer_min"] for x in cs), 1) if cs else None
        t["n_cer_fail"] = sum(1 for x in v if x.get("cer_fail"))
        t["n_blocked"] = sum(1 for x in v if x.get("blocked"))
    T[(role, ref)] = t

L = ["=" * 118, "PILOT v9 — F0 CLONE (AC / YIN) · toc do · lang · G8 · CER", "=" * 118,
     f"{'Vai':4} {'Clip':12} {'n':>3} {'F0_ac':>6} {'F0_yin':>6} {'am/s':>5} {'lang>0.3':>8} "
     f"{'G8 nc':>6} {'CER tb':>7} {'CER loi':>7} {'chan':>4}  F0 theo cam xuc"]
for k in sorted(T, key=lambda k: (k[0], k[1])):
    t = T[k]
    L.append(f"{t['role']:4} {t['ref']:12} {t['n']:3d} {t['f0_ac']:6.1f} {t['f0_yin']:6.1f} {t['syl_s']:5.2f} "
             f"{t['gap_gt03']:4d}/{t['n']:<3d} {t['g8_spread_nc']:6.2f} "
             f"{str(t.get('cer_mean_r1', '-')):>7} {str(t.get('n_cer_fail', '-')):>7} {str(t.get('n_blocked', '-')):>4}  "
             + " ".join(f"{e}={f}" for e, f in t["f0_by_emotion"].items()))

# ------------------------------------------------------------------ G9 moi cap
L += ["", "=" * 118, "G9 — MOI cap vai (ke ca khac gioi). DAT khi min(AC, YIN) >= 4 nua cung", "=" * 118]
Ds = [k for k in T if k[0] == "D"]
Cs = [k for k in T if k[0] == "C"]
others = [k for k in T if k[1].startswith("PROD_")]
pairs = {}


def d(k1, k2):
    return round(min(nc(T[k1]["f0_ac"], T[k2]["f0_ac"]), nc(T[k1]["f0_yin"], T[k2]["f0_yin"])), 2)


for k1 in Ds + Cs:
    for k2 in others + (Cs if k1[0] == "D" else []):
        pairs[f"{k1[1]}~{k2[1]}"] = d(k1, k2)
        L.append(f"  {k1[0]}:{k1[1]:10} <-> {k2[0]}:{k2[1]:12} {pairs[f'{k1[1]}~{k2[1]}']:6.2f} nc  "
                 f"{'DAT' if pairs[f'{k1[1]}~{k2[1]}'] >= NC_MIN else 'TRUOT'}")

# ------------------------------------------------------------------ to hop D x C
L += ["", "=" * 118, "TO HOP D x C (H = PROD_H, N1/N2 = san xuat). Bien = cap gan nhat", "=" * 118]
combos = []
for kd, kc in itertools.product(Ds, Cs):
    ds = {f"D~{o[1]}": d(kd, o) for o in others}
    ds.update({f"C~{o[1]}": d(kc, o) for o in others})
    ds["D~C"] = d(kd, kc)
    worst = min(ds, key=ds.get)
    cer_ok = (not a.cer) or (T[kd].get("n_cer_fail", 1) == 0 and T[kc].get("n_cer_fail", 1) == 0)
    combos.append({"D": kd[1], "C": kc[1], "min_nc": ds[worst], "worst_pair": worst, "pairs": ds,
                   "g9_pass": ds[worst] >= NC_MIN, "cer_pass": cer_ok})
combos.sort(key=lambda c: (-(c["g9_pass"] and c["cer_pass"]), -c["min_nc"]))
for c in combos:
    L.append(f"  D={c['D']:8} C={c['C']:8} bien {c['min_nc']:5.2f} nc ({c['worst_pair']})  "
             f"G9 {'DAT' if c['g9_pass'] else 'TRUOT'}  CER {'DAT' if c['cer_pass'] else 'TRUOT/chua do'}")

txt = "\n".join(L)
print(txt)
(HERE / f"pilot_{a.tag}_result.txt").write_text(txt + "\n", encoding="utf-8")
for r in rows:
    r["path"] = str(r["path"])
(HERE / f"pilot_{a.tag}_result.json").write_text(json.dumps(
    {"table": {f"{k[0]}|{k[1]}": v for k, v in T.items()}, "pairs": pairs, "combos": combos,
     "rows": rows, "base": base}, ensure_ascii=False, indent=1), encoding="utf-8")
