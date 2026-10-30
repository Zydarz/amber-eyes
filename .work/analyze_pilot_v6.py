"""Phan tich ket qua PILOT v6 — do F0 clone that + CER, quyet dinh gan vai (G9).

Input : .work/kaggle_higgs/out_higgs_v6/out_higgs_v6/  (tai ve tu Kaggle)
Output: .work/pilot_v6_result.json + .work/pilot_v6_result.txt

Tinh toan:
  * F0 clone 2 thuat toan (AC tho = voice_audition.f0_median, AC chuan hoa +
    parabolic + sua octave = pp2)
  * CER voi ASR `listen_audio` (2 luot, lay luot XAU HON) — chi do khi co
    --cer, mac dinh chi do F0 (nhanh)
  * Bang G9 cho MOI phan bo (H, D, C, N1, N2) — 3 cap nua phai >= 4 nc o CA HAI
    thuat toan (quy tac bao thu: min(ac, pp2) >= 4)
"""
import argparse
import json
import math
import pathlib
import sys
import wave
from collections import defaultdict

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))
from voice_audition import f0_median as f0_ac  # noqa: E402

WAV = HERE / "kaggle_higgs" / "out_higgs_v6" / "out_higgs_v6"
OUT_J = HERE / "pilot_v6_result.json"
OUT_T = HERE / "pilot_v6_result.txt"

# so do chuan bi (pilot v3/v4/v5, AC tho / pp2) — tai lai tu
# .work/baseline_clone_f0.py (da kiem lai loi octave: 0/296 file loi)
BASE_P = HERE / "baseline_clone_f0.json"
BASELINE = {}
if BASE_P.exists():
    _bt = json.loads(BASE_P.read_text(encoding="utf-8-sig"))["table"]
    for k, v in _bt.items():
        BASELINE[(v["role"], v["ref_wav"])] = (v["f0_ac"], v["f0_p2"])
    print("baseline: %d o tu %s" % (len(BASELINE), BASE_P.name))
else:
    print("!! khong co baseline_clone_f0.json -> dung so do gan trong code")
NC_MIN = 4.0


def read_wav(p):
    with wave.open(str(p), "rb") as w:
        sr, nch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(w.getnframes())
    if sw == 2:
        a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    elif sw == 4:
        a = np.frombuffer(raw, np.int32).astype(np.float32) / 2147483648
    else:
        a = np.frombuffer(raw, np.uint8).astype(np.float32) / 128 - 1
    if nch > 1:
        a = a.reshape(-1, nch).mean(axis=1)
    return a, sr


def f0_p2(x, sr, fmin=70.0, fmax=400.0):
    win = int(0.045 * sr)
    hop = int(0.010 * sr)
    lo, hi = int(sr / fmax), int(sr / fmin)
    out, prev = [], None
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.01:
            continue
        f = f - f.mean()
        peak = np.max(np.abs(f))
        if peak > 0:
            f = np.clip(f, -0.5 * peak, 0.5 * peak)
        n = len(f)
        nfft = 1 << int(np.ceil(np.log2(2 * n)))
        F = np.fft.rfft(f, nfft)
        ac = np.fft.irfft(F * np.conj(F), nfft)[:n]
        if ac[0] <= 0:
            continue
        acn = ac / ac[0]
        k = lo + int(np.argmax(acn[lo:hi]))
        if acn[k] < 0.25:
            continue
        shift = 0.0
        if 0 < k < n - 1:
            a0, a1, a2 = acn[k - 1], acn[k], acn[k + 1]
            d = a0 - 2 * a1 + a2
            if d != 0:
                shift = 0.5 * (a0 - a2) / d
        f0 = sr / (k + shift)
        if prev is not None:
            if 0.5 * prev < f0 < prev:
                k2 = int(round(k / 2))
                if k2 >= lo and acn[k2] > 0.8 * acn[k]:
                    f0 = sr / (k2 + shift)
            elif prev < f0 < 2 * prev:
                k2 = int(round(k * 2))
                if k2 < len(acn) and acn[k2] > 0.8 * acn[k]:
                    f0 = sr / (k2 + shift)
        out.append(f0)
        prev = f0
    return float(np.median(out)) if out else 0.0


def med(v):
    v = sorted(x for x in v if x)
    return v[len(v) // 2] if v else 0.0


def nc(a, b):
    if not a or not b or a <= 0 or b <= 0:
        return 0.0
    return abs(12 * math.log2(a / b))


# ------------------------------------------------------------------ CER (tu chon)
def run_cer(rows):
    import re
    import subprocess
    from concurrent.futures import ThreadPoolExecutor
    sys.path.insert(0, str(HERE))
    CACHE = HERE / "kaggle_higgs" / "_asr_cache_v6"
    CACHE.mkdir(parents=True, exist_ok=True)

    def mcode(args, timeout=600):
        r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=timeout)
        if r.returncode != 0:
            raise RuntimeError((r.stderr or r.stdout or "")[:400])
        return json.loads(r.stdout)

    def asr(path, rnd):
        cf = CACHE / f"{path.stem}__r{rnd}.json"
        if cf.exists():
            try:
                return json.loads(cf.read_text(encoding="utf-8"))
            except Exception:
                pass
        up = mcode(["upload-temp-url", str(path), "--mime-type", "audio/wav"])
        url = up.get("temp_url")
        if not url:
            return {"transcription": "", "code": -1}
        af = CACHE / f"{path.stem}__r{rnd}.args.json"
        af.write_text(json.dumps(
            {"audio_info": {"url": url, "mime_type": "audio/wav",
                            "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
            ensure_ascii=False), encoding="utf-8")
        res = mcode(["connector", "call", "connector__matrix__listen_audio",
                     "--args-file", str(af)])
        res["_round"] = rnd
        cf.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
        return res

    from voice_audition import cer, norm
    ONES = ("zero one two three four five six seven eight nine ten eleven twelve "
            "thirteen fourteen fifteen sixteen seventeen eighteen nineteen").split()
    TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()

    def vi_num(n):
        n = int(n)
        if n < 20:
            return ONES[n]
        if n < 100:
            return TENS[n // 10] + (" " + ONES[n % 10] if n % 10 else "")
        return str(n)

    def vi_numbers(text):
        def rep(m):
            s = m.group(0).replace(".", "")
            if not s.isdigit():
                return m.group(0)
            parts = []
            while len(s) > 3:
                parts.insert(0, s[-3:])
                s = s[:-3]
            if s:
                parts.insert(0, s)
            return " ".join(vi_num(p) for p in parts)
        return re.sub(r"\d[\d.]*", rep, text)

    def work(r):
        p = WAV / r["file"]
        if not p.exists():
            return r
        hyps = []
        for rnd in (1, 2):
            try:
                res = asr(p, rnd)
            except Exception as e:
                res = {"transcription": "", "error": str(e)[:200]}
            h = res.get("transcription") or res.get("text") or ""
            if re.search(r"This request was blocked|blocked by|safety", h, re.I):
                h = ""
            hyps.append(h)
        txt = r.get("text_plain") or r.get("text_sent") or ""
        txt = re.sub(r"<\|[^|]*\|>", " ", txt)
        txt = re.sub(r"<#.*?#>", " ", txt)
        r["text_norm"] = norm(vi_numbers(txt))
        best = None
        for h in hyps:
            if not h:
                continue
            c = cer(txt, h)
            best = c if best is None else max(best, c)
        r["cer"] = best
        r["cer_ok"] = best is not None
        return r

    with ThreadPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(work, rows))
    return rows


# ------------------------------------------------------------------ main
ap = argparse.ArgumentParser()
ap.add_argument("--cer", action="store_true", help="do them CER (canh goc ASR)")
ap.add_argument("--dir", default=None, help="thu muc output pilot (mac dinh: .work/kaggle_higgs/out_higgs_v6/out_higgs_v6)")
a = ap.parse_args()

WAV = pathlib.Path(a.dir) if a.dir else (HERE / "kaggle_higgs" / "out_higgs_v6" / "out_higgs_v6")
OUT_J = HERE / "pilot_v6_result.json"
OUT_T = HERE / "pilot_v6_result.txt"
SEARCH_ROOT = WAV if a.dir else (HERE / "kaggle_higgs" / "out_higgs_v6")

man_p = WAV / "higgs_manifest.json"
if not man_p.exists():
    cands = sorted(SEARCH_ROOT.rglob("higgs_manifest.json"))
    if not cands:
        raise SystemExit("khong tim thay manifest pilot v6")
    man_p = cands[0]
man = json.loads(man_p.read_text(encoding="utf-8-sig"))
rows = [r for r in man if r.get("ok")]
print("manifest:", man_p, "| OK:", len(rows), "| FAIL:", len(man) - len(rows))

for r in rows:
    p = WAV / r["file"]
    if not p.exists():
        cands = list(SEARCH_ROOT.rglob(r["file"]))
        if not cands:
            continue
        p = cands[0]
    a_, sr = read_wav(p)
    r["f0_ac"] = round(f0_ac(a_, sr), 1)
    r["f0_p2_raw"] = round(f0_p2(a_, sr), 1)
    r["dur_local"] = round(len(a_) / sr, 2)

# ---- sua loi OCTAVE cua thuat toan pp2 (do lai 1 lan / 2 lan) -----------
# pp2 co the chon nham (1/2) hoac gap (x2) so voi AC tho. Neu khong sua,
# bang G9 se bao "CANH BAO" gia. Chi sua khi sai lech < 5% va ghi lai.
n_oct = 0
for r in rows:
    ac, p2 = r.get("f0_ac"), r.get("f0_p2_raw")
    if not ac or not p2:
        r["f0_p2"] = p2 or 0.0
        continue
    if abs(p2 * 2 - ac) / ac < 0.05:
        r["f0_p2"] = round(p2 * 2, 1)
        r["octave_fix"] = "x2"
        n_oct += 1
    elif abs(p2 / 2 - ac) / ac < 0.05:
        r["f0_p2"] = round(p2 * 2, 1)
        r["octave_fix"] = "nhan2"
        n_oct += 1
    else:
        r["f0_p2"] = p2
print("sua loi octave pp2: %d/%d audio" % (n_oct, len(rows)))

if a.cer:
    print("do CER (2 luot)... co the la 5-10 phut")
    rows = run_cer(rows)

# ------------------------------------------------------------------ bang F0
g = defaultdict(list)
for r in rows:
    g[(r["role"], r["ref_wav"])].append(r)

table = {}
for k, v in g.items():
    acs = sorted(x["f0_ac"] for x in v if x["f0_ac"])
    p2s = sorted(x["f0_p2"] for x in v if x["f0_p2"])
    table[k] = {"role": k[0], "ref_wav": k[1], "n": len(v),
                "f0_ac": med(acs), "f0_p2": med(p2s),
                "f0_ac_min": min(acs), "f0_ac_max": max(acs),
                "f0_p2_min": min(p2s), "f0_p2_max": max(p2s),
                "dur_min": min(x["dur_local"] for x in v),
                "dur_max": max(x["dur_local"] for x in v)}
    if a.cer:
        cs = [x["cer"] for x in v if x.get("cer_ok")]
        table[k]["cer_mean"] = round(100 * sum(cs) / len(cs), 2) if cs else None
        table[k]["cer_max"] = round(100 * max(cs), 1) if cs else None
        table[k]["n_cer_gt2"] = len([c for c in cs if c > 0.02])

L = []
L.append("=" * 108)
L.append("PILOT v6 — F0 CLONE that (AC tho / AC chuan hoa) + drift so voi clip")
L.append("=" * 108)
L.append("%-4s %-16s %-4s %-9s %-9s %-9s %-9s %s" % (
    "Vai", "Clip", "n", "F0_ac", "F0_pp2", "drift_ac", "drift_pp2", "khoang ac"))
for k in sorted(table):
    t = table[k]
    ref = HERE / "assets_ref_f0.json"
    drift_ac = drift_p2 = ""
    src = k[1].replace(".wav", "")
    rfp = ROOT / "assets" / "voice_ref_voxcpm2" / k[1]
    if not rfp.exists():
        rfp = ROOT / "assets" / "voice_ref_voxcpm2_g9" / k[1]
    if rfp.exists():
        aa, ss = read_wav(rfp)
        rac, rp2 = f0_ac(aa, ss), f0_p2(aa, ss)
        drift_ac = "%+.1f%%" % ((t["f0_ac"] / rac - 1) * 100)
        drift_p2 = "%+.1f%%" % ((t["f0_p2"] / rp2 - 1) * 100)
    L.append("%-4s %-16s %-4d %-9.1f %-9.1f %-9s %-9s %.1f-%.1f" % (
        k[0], k[1], t["n"], t["f0_ac"], t["f0_p2"], drift_ac, drift_p2,
        t["f0_ac_min"], t["f0_ac_max"]))
    if a.cer:
        L[-1] += "   CER tb %s%% max %s%% >2%%: %s" % (
            t.get("cer_mean"), t.get("cer_max"), t.get("n_cer_gt2"))

# ------------------------------------------------------------------ G9
L.append("")
L.append("=" * 108)
L.append("G9 — MOI cap cung gioi (nguong >= 4 nua cung; DAT khi CA HAI thuat toan >= 4)")
L.append("=" * 108)


def verdict(d_ac, d_p2):
    if min(d_ac, d_p2) >= NC_MIN:
        return "DAT"
    if max(d_ac, d_p2) >= NC_MIN:
        return "CANH BAO"
    return "TRUOT"


def get(role, ref):
    return table.get((role, ref))


def pair(r1, r2, d1, d2):
    if not (r1 and r2):
        return None
    return (r1["f0_ac"], r2["f0_ac"], r1["f0_p2"], r2["f0_p2"], d1, d2)


H_REFS = ["M_LOW.wav", "H.wav"]
D_REFS = ["M_HIGH.wav", "D.wav"]
N1_REFS = ["W6_LOW_S40.wav", "W6_LOW_S35.wav", "W6_LOW_S30.wav",
           "W6_LOW_S25.wav", "W6_LOW.wav"]
N2_REFS = ["W5_HIGH.wav", "W2.wav", "W1.wav"]
C_REFS = ["C.wav"]

results = []
L.append("")
L.append("A) H <-> D")
L.append("   %-16s %-16s %-9s %-9s %s" % ("H clip", "D clip", "nc_ac", "nc_pp2", "Ket"))
for hr in H_REFS:
    for dr in D_REFS:
        h, d = get("H", hr), get("D", dr)
        if not (h and d):
            continue
        x, y = nc(h["f0_ac"], d["f0_ac"]), nc(h["f0_p2"], d["f0_p2"])
        v = verdict(x, y)
        L.append("   %-16s %-16s %-9.2f %-9.2f %s" % (hr, dr, x, y, v))
        results.append({"pair": "H-D", "h_ref": hr, "d_ref": dr,
                        "nc_ac": round(x, 2), "nc_pp2": round(y, 2), "verdict": v})

L.append("")
L.append("B) C / N1 / N2 — 3 cap nua, ca 3 cap phai >= 4 nc")
L.append("   %-16s %-16s %-9s %-9s %-9s %s" % (
    "N1 clip", "N2 clip", "C<->N1", "C<->N2", "N1<->N2", "Ket"))
for cr in C_REFS:
    c = get("C", cr)
    for n1r in N1_REFS:
        for n2r in N2_REFS:
            n1, n2 = get("N1", n1r), get("N2", n2r)
            if not (c and n1 and n2):
                continue
            a1 = min(nc(c["f0_ac"], n1["f0_ac"]), nc(c["f0_p2"], n1["f0_p2"]))
            a2 = min(nc(c["f0_ac"], n2["f0_ac"]), nc(c["f0_p2"], n2["f0_p2"]))
            a3 = min(nc(n1["f0_ac"], n2["f0_ac"]), nc(n1["f0_p2"], n2["f0_p2"]))
            v = verdict(a1, a2)
            L.append("   %-16s %-16s %-9.2f %-9.2f %-9.2f %s" % (
                n1r, n2r, a1, a2, a3, v))
            results.append({"pair": "C-N1-N2", "c_ref": cr, "n1_ref": n1r, "n2_ref": n2r,
                            "c_n1": round(a1, 2), "c_n2": round(a2, 2),
                            "n1_n2": round(a3, 2), "verdict": v})

L.append("")
L.append("C) PHOI DAY DU (H,D,C,N1,N2) — moi phai DAT ca 3 cap nua + H/D")
full = []
for hr in H_REFS:
    for dr in D_REFS:
        for cr in C_REFS:
            for n1r in N1_REFS:
                for n2r in N2_REFS:
                    h, d, c = get("H", hr), get("D", dr), get("C", cr)
                    n1, n2 = get("N1", n1r), get("N2", n2r)
                    if not (h and d and c and n1 and n2):
                        continue
                    hd = min(nc(h["f0_ac"], d["f0_ac"]), nc(h["f0_p2"], d["f0_p2"]))
                    a1 = min(nc(c["f0_ac"], n1["f0_ac"]), nc(c["f0_p2"], n1["f0_p2"]))
                    a2 = min(nc(c["f0_ac"], n2["f0_ac"]), nc(c["f0_p2"], n2["f0_p2"]))
                    a3 = min(nc(n1["f0_ac"], n2["f0_ac"]), nc(n1["f0_p2"], n2["f0_p2"]))
                    ok = min(hd, a1, a2, a3) >= NC_MIN
                    warn = (not ok) and max(hd, a1, a2, a3) >= NC_MIN
                    v = "DAT" if ok else ("CANH BAO" if warn else "TRUOT")
                    full.append({"h_ref": hr, "d_ref": dr, "c_ref": cr,
                                 "n1_ref": n1r, "n2_ref": n2r,
                                 "h_d": round(hd, 2), "c_n1": round(a1, 2),
                                 "c_n2": round(a2, 2), "n1_n2": round(a3, 2),
                                 "margin": round(min(hd, a1, a2, a3), 2),
                                 "verdict": v})
full.sort(key=lambda r: -r["margin"])
L.append("   %-16s %-16s %-16s %-16s %-16s %-8s %s" % (
    "H", "D", "C", "N1", "N2", "margin", "Ket"))
for r in full[:18]:
    L.append("   %-16s %-16s %-16s %-16s %-16s %-8.2f %s" % (
        r["h_ref"], r["d_ref"], r["c_ref"], r["n1_ref"], r["n2_ref"],
        r["margin"], r["verdict"]))
n_dat = len([r for r in full if r["verdict"] == "DAT"])
L.append("")
L.append("   => %d/%d phoi DAT (tu 36 cap nhat)" % (n_dat, len(full)))

txt = "\n".join(L)
OUT_T.write_text(txt, encoding="utf-8")
OUT_J.write_text(json.dumps({
    "table": {"|".join([k[0], k[1]]): v for k, v in table.items()},
    "pairs": results, "full": full, "n_full": len(full),
    "n_full_dat": n_dat,
}, ensure_ascii=False, indent=1), encoding="utf-8")
print(txt)
print("\n->", OUT_T)
print("->", OUT_J)
