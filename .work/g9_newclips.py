"""Do F0 + QC cho 4 clip THAM CHIEU MOI (voice_ref_voxcpm2_g9) va 7 clip goc.

Muc dich:
  1. Do F0 (2 thuat toan: AC tho = voice_audition.f0_median, AC chuan hoa+parabolic
     + sua octave = pp2) cho tat ca clip.
  2. Kiem tra QC §4: thoi luong 16-28 s, mono, 24 kHz.
  3. Do drift da biet tu pilot v5 de DU DOAN F0 clone cua 4 clip moi.
  4. Duyet moi phan bo vai (H/D/N1/N2) theo G9 (>= 4 nua cung, ca 2 thuat toan).

Khong goi ASR, khong goi model. Chi doc WAV local.
"""
import json
import math
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent                                    # repo goc
sys.path.insert(0, str(HERE))                        # voice_audition nam trong .work/
sys.path.insert(0, str(ROOT))
from voice_audition import f0_median as f0_ac  # noqa: E402

NEW_DIR = ROOT / "assets" / "voice_ref_voxcpm2_g9"
OLD_DIR = ROOT / "assets" / "voice_ref_voxcpm2"
OUT = HERE / "g9_newclips.json"

LO_SEC, HI_SEC = 16.0, 28.0

# F0 clone THUC do duoc o pilot v5 (AC tho) -> ti le clone/clip cho tung clip
PILOT_V5_CLONE = {
    "H.wav": 131.0,     # ref 108.1 -> 131.0  (+21%)
    "D.wav": 122.0,     # ref 128.3 -> 122.0  (-5%)
    "W3.wav": 162.2,    # ref 162.2 -> 162.2  (0%)
    "W4.wav": 140.4,    # ref 137.1 -> 140.4  (+2%)
}
# ref F0 (AC tho) cua 7 clip goc
OLD_REF_AC = {"H": 108.1, "D": 128.3, "C": 210.5, "W1": 252.6,
              "W2": 200.0, "W3": 162.2, "W4": 137.1}
# F0 clone do duoc o pilot v3/v4 (AC tho) cho vai C, N1, N2 voi clip goc
PILOT_CLONE_AC = {"C<-C.wav": 205.0, "N2<-W1.wav": 276.0, "N1<-W1.wav": 259.0,
                   "N1<-W2.wav": 205.0, "N1<-W3.wav": 168.0, "N1<-W4.wav": 143.0}


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
    """AC chuan hoa + parabolic + sua octave (pp2) — giong g9_matrix.py."""
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


def measure(p):
    a, sr = read_wav(p)
    fr = f0_p2(a, sr)
    dur = len(a) / sr
    ac = f0_ac(a, sr)
    p2 = float(np.median(fr)) if fr else 0.0
    qc = []
    if not (LO_SEC <= dur <= HI_SEC):
        qc.append("THOI_LUONG %.2fs ngoai [%.0f,%.0f]" % (dur, LO_SEC, HI_SEC))
    if sr != 24000:
        qc.append("SR %d != 24000" % sr)
    if abs(ac - p2) / max(ac, 1e-9) > 0.12:
        qc.append("AC_THRO vs PP2 lech %.1f%% (>|12%%|)" % (abs(ac - p2) / ac * 100))
    return {"file": p.name, "dur": round(dur, 2), "sr": sr,
            "f0_ac": round(ac, 1), "f0_p2": round(p2, 1), "n_frames": len(fr),
            "qc": qc}


# ------------------------------------------------------------------ do
print("=" * 100)
print("F0 + QC cho 4 CLIP MOI (assets/voice_ref_voxcpm2_g9)")
print("=" * 100)
new = {}
for p in sorted(NEW_DIR.glob("*.wav")):
    m = measure(p)
    new[p.stem] = m
    print("  %-10s dur=%6.2fs sr=%d  F0_ac=%6.1f  F0_pp2=%6.1f  %s" % (
        m["file"], m["dur"], m["sr"], m["f0_ac"], m["f0_p2"],
        ("  << " + "; ".join(m["qc"])) if m["qc"] else "OK"))

print()
print("=" * 100)
print("F0 + QC cho 7 CLIP GOC (assets/voice_ref_voxcpm2) — de doi chieu")
print("=" * 100)
old = {}
for p in sorted(OLD_DIR.glob("*.wav")):
    m = measure(p)
    old[p.stem] = m
    print("  %-10s dur=%6.2fs sr=%d  F0_ac=%6.1f  F0_pp2=%6.1f  %s" % (
        m["file"], m["dur"], m["sr"], m["f0_ac"], m["f0_p2"],
        ("  << " + "; ".join(m["qc"])) if m["qc"] else "OK"))

# --------------------------------------------------- drift pilot v5 -> du doan clone
print()
print("=" * 100)
print("TI LE DRIFT DA DO (pilot v5): clone/clip")
print("=" * 100)
drift = {}
for ref, clone in PILOT_V5_CLONE.items():
    stem = ref.replace(".wav", "")
    r = old.get(stem, {})
    if r and r["f0_ac"]:
        ratio = clone / r["f0_ac"]
        drift[stem] = round(ratio, 3)
        print("  %-6s ref=%6.1f Hz -> clone=%6.1f Hz   ratio=%.3f (%+.1f%%)" % (
            stem, r["f0_ac"], clone, ratio, (ratio - 1) * 100))

ratios = sorted(drift.values())
lo_ratio, hi_ratio = ratios[0], ratios[-1]
mid_ratio = drift.get("W4.wav", 1.03)
print()
print("  ti le quan sat: min=%.3f  max=%.3f  (W3/W4 nhom 1.02-1.06, H.wav cao 1.21)" % (
    lo_ratio, hi_ratio))

print()
print("=" * 100)
print("DU DOAN F0 CLONE cho 4 clip moi (dung ti le 1.02-1.06 cho ref >= 132 Hz,")
print("                 va 1.06-1.22 cho ref thap) — CANH BAO: phai do lai bangng pilot v6")
print("=" * 100)
pred = {}
for stem, m in new.items():
    f = m["f0_ac"]
    if f >= 132:
        r_lo, r_hi = 1.02, 1.06
    else:
        r_lo, r_hi = 1.06, 1.22
    pred[stem] = {"f0_ac": f, "ratio_lo": r_lo, "ratio_hi": r_hi,
                  "clone_lo": round(f * r_lo, 1), "clone_hi": round(f * r_hi, 1)}
    print("  %-10s F0_ac=%6.1f  ratio %.2f-%.2f  => clone uoc %6.1f - %6.1f Hz" % (
        stem, f, r_lo, r_hi, f * r_lo, f * r_hi))

# --------------------------------------------------- duyet phan bo G9
print()
print("=" * 100)
print("G9 — DUYET phan bo vai (du doan, se xac nhan bang pilot v6)")
print("=" * 100)

C_CLONE = 205.0
N2_W1_CLONE = 276.0


def check(pairs):
    """pairs: list (tenA, tenB, f0A, f0B) -> (min_nc, max_nc, verdict)"""
    ds = [nc(a, b) for _, _, a, b in pairs]
    lo, hi = min(ds), max(ds)
    verdict = "DAT" if lo >= 4 else ("CANH BAO" if hi >= 4 else "TRUOT")
    return lo, hi, verdict


h_lo = pred["M_LOW"]["clone_lo"]
h_hi = pred["M_LOW"]["clone_hi"]
d_lo = pred["M_HIGH"]["clone_lo"]
d_hi = pred["M_HIGH"]["clone_hi"]
w6_lo = pred["W6_LOW"]["clone_lo"]
w6_hi = pred["W6_LOW"]["clone_hi"]
w5_lo = pred["W5_HIGH"]["clone_lo"]
w5_hi = pred["W5_HIGH"]["clone_hi"]

print()
print("A) H <-> D — 2 phuong an chinh")
print("   %-34s %-14s %-14s %s" % ("Phuong an", "nc ac", "nc pp2", "Ket"))
for name, hcl, dcl in (
    ("H<-M_LOW, D<-M_HIGH", (h_lo, h_hi), (d_lo, d_hi)),
    ("H<-M_LOW, D<-D.wav(goc)", (h_lo, h_hi), (122.0, 122.0)),
    ("H<-H.wav(goc), D<-M_HIGH", (131.0, 131.0), (d_lo, d_hi)),
):
    lo, hi, v = check([("H", "D", hcl[0], dcl[0]), ("H", "D", hcl[1], dcl[1])])
    print("   %-34s %-14.2f %-14.2f %s" % (name, lo, hi, v))

print()
print("B) C / N1 / N2 — 3 cap nua deu phai >= 4 nc")
print("   %-46s %-9s %-9s %-9s %s" % (
    "Phuong an", "C<->N1", "C<->N2", "N1<->N2", "Ket"))
combos = [
    ("C<-C.wav, N1<-W6_LOW, N2<-W1.wav", 205.0, (w6_lo, w6_hi), 276.0),
    ("C<-C.wav, N1<-W6_LOW, N2<-W5_HIGH", 205.0, (w6_lo, w6_hi), (w5_lo, w5_hi)),
    ("C<-W5_HIGH, N1<-W6_LOW, N2<-W1.wav", (w5_lo, w5_hi), (w6_lo, w6_hi), 276.0),
    ("C<-C.wav, N1<-W6_LOW, N2<-W1.wav [shift]", 205.0, (155.0, 155.0), 276.0),
]
for name, ccl, n1cl, n2cl in combos:
    ds = []
    for c in (ccl[0] if isinstance(ccl, tuple) else ccl,
              ccl[1] if isinstance(ccl, tuple) else ccl):
        for n1 in n1cl:
            for n2 in n2cl:
                ds += [nc(c, n1), nc(c, n2), nc(n1, n2)]
    lo, hi, v = check([("x", "y", 1.0, 1.0)])  # placeholder
    lo, hi = min(ds), max(ds)
    verdict = "DAT" if lo >= 4 else ("CANH BAO" if hi >= 4 else "TRUOT")
    print("   %-46s %-9.2f %-9.2f %-9.2f %s" % (
        name, min(nc(ccl[0] if isinstance(ccl, tuple) else ccl, n1) for n1 in n1cl),
        min(nc(ccl[0] if isinstance(ccl, tuple) else ccl, n2) for n2 in n2cl),
        min(nc(n1, n2) for n1 in n1cl for n2 in n2cl), verdict))

print()
print("=" * 100)
print("KHOANG F0 CLONE BAT BUOC cho N1 (khi C=205 Hz va N2=276 Hz)")
print("=" * 100)
n1_max = min(C_CLONE, N2_W1_CLONE) / (2 ** (4 / 12))
print("  N1 clone phai <= %.1f Hz  (de cach >= 4 nc ca C va N2)" % n1_max)
print("  => clip tham chieu N1 can F0 <= ~%.0f Hz (dung drift ~1.03)" % (n1_max / 1.03))
print("  W6_LOW hien tai: ref %.1f Hz -> clone uoc %.1f-%.1f Hz  => %s" % (
    new["W6_LOW"]["f0_ac"], w6_lo, w6_hi,
    "DU" if w6_lo <= n1_max else "TRUOT"))
print("  W5_HIGH (cao): ref %.1f Hz -> clone uoc %.1f-%.1f Hz => sat N2" % (
    new["W5_HIGH"]["f0_ac"], w5_lo, w5_hi))

OUT.write_text(json.dumps({
    "new_clips": new, "old_clips": old,
    "pilot_v5_drift": drift,
    "predicted_clone": pred,
    "g9_hd_notes": "H<-M_LOW, D<-M_HIGH du doan dat; can pilot v6 xac nhan",
}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n->", OUT)
