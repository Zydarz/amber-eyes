"""Tinh lai bang F0 CLONE goc (pilot v3 + v4 + v5) CO buoc sua loi octave.

Ly do: `g9_matrix.py` / `pilot_v5_f0.py` tinh pp2 MA khong sua loi octave.
Neu thuat toan pp2 chon nham/gap o mot so file, so do goc se lech => so sanh
pilot v6 voi baseline co the ra ket qua sai.

Xuat: .work/baseline_clone_f0.json  (dung lam baseline cho analyze_pilot_v6.py)
"""
import json
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

KAGGLE = HERE / "kaggle_higgs"
OUT = HERE / "baseline_clone_f0.json"


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
    return out


def med(v):
    v = sorted(x for x in v if x)
    return v[len(v) // 2] if v else 0.0


def fix_octave(ac, p2):
    if not ac or not p2:
        return p2, None
    if abs(p2 * 2 - ac) / ac < 0.05:
        return round(p2 * 2, 1), "x2"
    if abs(p2 / 2 - ac) / ac < 0.05:
        return round(p2 * 2, 1), "nhan2"
    return p2, None


rows = []
n_tot = n_fix = 0
for tag, sub in (("v3", "out_higgs_v3"), ("v4", "out_higgs_v4"), ("v5", "out_higgs_v5")):
    cands = sorted((KAGGLE / sub).rglob("higgs_manifest.json"))
    if not cands:
        print("!! khong thay manifest", tag)
        continue
    man_p = cands[0]
    root = man_p.parent
    man = json.loads(man_p.read_text(encoding="utf-8-sig"))
    n_ok = 0
    for r in man:
        if not r.get("ok"):
            continue
        p = root / r["file"]
        if not p.exists():
            cands2 = list((KAGGLE / sub).rglob(r["file"]))
            if not cands2:
                continue
            p = cands2[0]
        a, sr = read_wav(p)
        ac = f0_ac(a, sr)
        fr = f0_p2(a, sr)
        p2_raw = float(np.median(fr)) if fr else 0.0
        p2, fix = fix_octave(ac, p2_raw)
        n_tot += 1
        if fix:
            n_fix += 1
        rows.append({"pilot": tag, "role": r["role"], "ref_wav": r["ref_wav"],
                     "temp": r["temp"], "id": r.get("id"),
                     "f0_ac": round(ac, 1), "f0_p2_raw": round(p2_raw, 1),
                     "f0_p2": round(p2, 1), "octave_fix": fix})
        n_ok += 1
    print("%s: %d/%d audio do xong" % (tag, n_ok, len(man)))

print()
print("sua loi octave: %d/%d audio (%.1f%%)" % (n_tot and n_fix or 0, n_tot, 100 * n_fix / max(1, n_tot)))

g = defaultdict(list)
for r in rows:
    g[(r["role"], r["ref_wav"], r["temp"])].append(r)

table = {}
print()
print("=" * 100)
print("BANG F0 CLONE GOC — CO sua loi octave")
print("=" * 100)
print("%-4s %-12s %-5s %-4s %-9s %-9s %-9s %-9s" % (
    "Vai", "Clip", "Temp", "n", "F0_ac", "F0_pp2", "pp2_cu", "n_fix"))
for k in sorted(g):
    v = g[k]
    acs = [x["f0_ac"] for x in v]
    p2s = [x["f0_p2"] for x in v]
    p2raw = [x["f0_p2_raw"] for x in v]
    nf = len([x for x in v if x["octave_fix"]])
    table["|".join([k[0], k[1], str(k[2])])] = {
        "role": k[0], "ref_wav": k[1], "temp": k[2], "n": len(v),
        "f0_ac": round(med(acs), 1), "f0_p2": round(med(p2s), 1),
        "f0_p2_raw": round(med(p2raw), 1),
        "n_octave_fix": nf,
        "f0_ac_min": min(acs), "f0_ac_max": max(acs),
    }
    print("%-4s %-12s %-5s %-4d %-9.1f %-9.1f %-9.1f %-9d" % (
        k[0], k[1], k[2], len(v), med(acs), med(p2s), med(p2raw), nf))

OUT.write_text(json.dumps({
    "table": table,
    "n_audio": n_tot, "n_octave_fix": n_fix,
    "note": "pp2 da sua loi octave (x2 / nhan2) khi lech < 5% so voi AC tho",
}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n->", OUT)
