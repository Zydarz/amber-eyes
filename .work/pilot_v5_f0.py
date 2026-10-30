"""Pilot v5 — do F0 THUC cua audio clone khi doi clip tham chieu H/D sang W3/W4.

Day la thoi nghiem QUYET DINH cho G9 H<->D:
  - H clone tu H.wav (107 Hz) -> 131 Hz
  - D clone tu D.wav (132 Hz) -> 122 Hz
  => 2 vai trung ve cung mot vung ~125 Hz

Pilot v5 doi clip tham chieu:
  H <- W3.wav (157 Hz) · H <- W4.wav (134 Hz)
  D <- W3.wav (157 Hz) · D <- W4.wav (134 Hz)
Neu Higgs GIU F0 cua clip tham chieu, 2 vai se tach ra.
Neu KHONG, ca 4 o se ve lai ~125 Hz => phai tao clip moi.

Khong goi ASR, khong goi model. Chi doc WAV local + 2 thuat toan F0.
"""
import json
import math
import pathlib
import sys
import wave
from collections import defaultdict

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent                                    # repo goc
sys.path.insert(0, str(ROOT))
from voice_audition import f0_median as f0_ac  # noqa: E402

KAGGLE = HERE / "kaggle_higgs"
WAV = KAGGLE / "out_higgs_v5" / "out_higgs_v5"
OUT = HERE / "pilot_v5_f0.json"


def read_wav(p):
    with wave.open(str(p), "rb") as w:
        sr, nch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(w.getnframes())
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    if nch > 1:
        a = a.reshape(-1, nch).mean(axis=1)
    return a, sr


def f0_p2(x, sr, fmin=70.0, fmax=400.0):
    """AC chuan hoa + parabolic + sua octave — giong .work/g9_matrix.py."""
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


def med(vals):
    v = sorted(x for x in vals if x)
    return v[len(v) // 2] if v else 0.0


def nc(a, b):
    if not a or not b or a <= 0 or b <= 0:
        return 0.0
    return abs(12 * math.log2(a / b))


man_p = WAV / "higgs_manifest.json"
man = json.loads(man_p.read_text(encoding="utf-8-sig"))
rows = [r for r in man if r.get("ok")]
print("manifest:", man_p, "| OK:", len(rows), "| FAIL:", len(man) - len(rows))

for r in rows:
    p = WAV / r["file"]
    if not p.exists():
        cands = list((KAGGLE / "out_higgs_v5").rglob(r["file"]))
        if not cands:
            r["_missing"] = True
            continue
        p = cands[0]
    a, sr = read_wav(p)
    fr = f0_p2(a, sr)
    r["f0_ac"] = round(f0_ac(a, sr), 1)
    r["f0_p2"] = round(float(np.median(fr)), 1) if fr else 0.0
    r["dur_local"] = round(len(a) / sr, 2)

g = defaultdict(list)
for r in rows:
    if r.get("_missing"):
        continue
    g[(r["role"], r["ref_wav"], r["temp"])].append(r)

print()
print("=" * 104)
print("PILOT v5 — F0 THUC cua audio clone")
print("=" * 104)
print("%-4s %-9s %-5s %-4s %-9s %-9s %-9s %-11s" % (
    "Vai", "Clip", "Temp", "n", "F0_ac", "F0_pp2", "drift%", "Thoi luong"))
table = {}
for k in sorted(g):
    v = g[k]
    ac = sorted(x["f0_ac"] for x in v if x["f0_ac"])
    p2 = sorted(x["f0_p2"] for x in v if x["f0_p2"])
    du = sorted(x["dur_local"] for x in v if x["dur_local"])
    m_ac, m_p2 = med(ac), med(p2)
    table[k] = {"role": k[0], "ref_wav": k[1], "temp": k[2], "n": len(v),
                "f0_ac": m_ac, "f0_p2": m_p2,
                "f0_ac_min": min(ac), "f0_ac_max": max(ac),
                "f0_p2_min": min(p2), "f0_p2_max": max(p2),
                "dur_min": du[0], "dur_max": du[-1]}
    drift = ""
    if k[0] == "H" and k[1] == "H.wav":
        drift = "+22%"
    elif k[0] == "D" and k[1] == "D.wav":
        drift = "-7%"
    print("%-4s %-9s %-5s %-4d %-9.1f %-9.1f %-9s %-11s" % (
        k[0], k[1], k[2], len(v), m_ac, m_p2, drift,
        "%.1f-%.1f s" % (du[0], du[-1])))

print()
print("=" * 104)
print("G9 H<->D — DUYET TAT CA TO HOP (H clip) x (D clip)")
print("=" * 104)
print("%-10s %-10s %-10s %-10s %-8s %-8s %s" % (
    "H clip", "D clip", "H F0", "D F0", "nc_ac", "nc_pp2", "Ket"))
rows_out = []
for h_ref in ("H.wav", "W4.wav", "W3.wav"):
    for d_ref in ("D.wav", "W4.wav", "W3.wav"):
        h = table.get(("H", h_ref, 0.8))
        d = table.get(("D", d_ref, 0.8))
        if not h or not d:
            continue
        a, b = nc(h["f0_ac"], d["f0_ac"]), nc(h["f0_p2"], d["f0_p2"])
        ok = min(a, b) >= 4
        warn = (not ok) and max(a, b) >= 4
        verdict = "DAT" if ok else ("CANH BAO" if warn else "TRUOT")
        print("%-10s %-10s %-10.1f %-10.1f %-8.2f %-8.2f %s" % (
            h_ref, d_ref, h["f0_ac"], d["f0_ac"], a, b, verdict))
        rows_out.append({"h_ref": h_ref, "d_ref": d_ref,
                         "h_f0_ac": h["f0_ac"], "d_f0_ac": d["f0_ac"],
                         "h_f0_p2": h["f0_p2"], "d_f0_p2": d["f0_p2"],
                         "nc_ac": round(a, 2), "nc_pp2": round(b, 2),
                         "verdict": verdict})

# --- ket luan co chon loc: co the tach bang clip CO SAN khong? ---
print()
print("=" * 104)
print("KET LUAN")
print("=" * 104)
best = max(rows_out, key=lambda r: min(r["nc_ac"], r["nc_pp2"]))
print("To hop tot nhat voi clip CO SAN: H<-%s , D<-%s  => %.2f nc (AC thô) / %.2f nc (AC chuẩn hóa) -> %s" % (
    best["h_ref"], best["d_ref"], best["nc_ac"], best["nc_pp2"], best["verdict"]))
newf0 = {k[1]: v["f0_ac"] for k, v in table.items() if k[0] in ("H", "D") and k[2] == 0.8}
print()
print("F0 clone theo clip tham chieu (gop vai H va D, temp 0.8):")
for ref in sorted(newf0):
    print("   %-8s -> %6.1f Hz" % (ref, newf0[ref]))
print()
print("=> Neu F0 clone DI CHUYEN theo clip tham chieu (W3 cao hon W4 cao hon H/D goc),")
print("   Higgs GIU (mot phan) cao do. Neu 4 o deu ve ~125 Hz, Higgs KHONG giu.")

OUT.write_text(json.dumps({
    "table": {"|".join([str(k[0]), k[1], str(k[2])]): v for k, v in table.items()},
    "h_d_combos": rows_out,
    "best_existing": best,
    "clone_f0_by_ref": newf0,
}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n->", OUT)
