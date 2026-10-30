"""Tao bien the clip tham chieu "nữ THẤP" cho vai N1 (G9 Tap 02).

LY DO
-----
G9 (AGENTS.md): 2 vai cung gioi phai cach >= 4 nua cung F0.
Tap 02 co 3 vai NU: C (chuyen gia tam ly) · N1 (nguoi ke thu nhat) · N2 (nguoi ke thu hai).
Do da (pilot v3+v4, n=8/o, AC tho / pp2):
    C  <- C.wav  = 205.1 / 194.9 Hz
    N1 <- W1.wav = 247.4 / 234.0 Hz
    N2 <- W2.wav = 206.9 / 198.7 Hz
=> C<->N1 = 3.23 nc, C<->N2 = 0.16 nc, N1<->N2 = 3.08 nc  => TRUOT G9 ca 3 cap.

Clip moi W6_LOW (nu thap, 179.1 / 169.0 Hz) sinh ra tren Mac van CHUA du:
clone du doan ~183-190 Hz => C<->N1 chi ~1.7 nc, van truot.
De clone cua N1 rơi <= 162.8 Hz (AC tho) va <= 154.7 Hz (pp2) — de cach >= 4 nc
ca C (205.1/194.9) lan N2 — can HAT F0 clip tham chieu xuong them.

=> Dung phase vocoder (time-stretch + resample) de tao nhieu bien the:
   -2.0, -2.5, -3.0, -3.5, -4.0 nua cung (semitone).
Pilot v6 se do F0 clone THUC cua tung bien the de chon.

GHI CHUAN: bien the van la asset tao boi chinh du an (Apache-2.0, VoxCPM2 Voice
Design), khong dung file cua ben thu ba. refs.json se ghi rõ f0 sau khi hạ.

Usage:  python .work/g9_shift_clip.py
"""
import json
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from voice_audition import f0_median as f0_ac  # noqa: E402

G9_DIR = ROOT / "assets" / "voice_ref_voxcpm2_g9"
SRC = G9_DIR / "W6_LOW.wav"
OUT = HERE / "g9_shift_clip.json"

# so nua cung can ha (am = hao)
SHIFTS = [-2.0, -2.5, -3.0, -3.5, -4.0]
# muc dich: F0 clone cua N1 phai <= day (do chinh xac bang pilot v6)
TARGET_CLONE_AC_MAX = 162.8
TARGET_CLONE_PP2_MAX = 154.7
# ti le clone/clip quan sat duoc (pilot v3+v4+v5)
DRIFT_LO, DRIFT_HI = 0.95, 1.10
LO_SEC, HI_SEC = 16.0, 28.0


# ------------------------------------------------------------------ io
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


def write_wav(p, a, sr):
    p.parent.mkdir(parents=True, exist_ok=True)
    a = np.clip(a, -0.999, 0.999)
    with wave.open(str(p), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(int(sr))
        w.writeframes((a * 32767).astype(np.int16).tobytes())


# ------------------------------------------------------------------ F0 pp2
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


# ------------------------------------------------------------------ trim im lang
def trim_silence(x, sr, max_dur=28.0, thr_db=-40.0):
    """Xoa 1 doan im lang dai nhat de thoi luong <= max_dur (khong mat chu)."""
    need = len(x) / sr - max_dur
    if need <= 0:
        return x, None, 0.0
    win = int(0.02 * sr)
    nfr = len(x) // win
    fr = np.abs(x[:nfr * win].reshape(nfr, win)).max(axis=1)
    db = 20 * np.log10(fr + 1e-9)
    sil = db < thr_db
    runs = []
    i = 0
    while i < nfr:
        if sil[i]:
            j = i
            while j < nfr and sil[j]:
                j += 1
            runs.append((i * win, j * win))
            i = j
        else:
            i += 1
    runs = [r for r in runs if r[1] - r[0] >= int(0.12 * sr)]
    if not runs:
        return x, None, 0.0
    a, b = max(runs, key=lambda r: r[1] - r[0])
    if (b - a) / sr < need:
        # khong du im lang -> cat duoi (bo cau cuoi, phai sua .txt)
        cut = int((len(x) / sr - max_dur + 0.05) * sr)
        return x[:len(x) - cut], ("tail", cut / sr), (b - a) / sr
    out = np.concatenate([x[:a], x[b:]])
    return out, ("silence", (b - a) / sr), (b - a) / sr


# ------------------------------------------------------------------ phase vocoder
def _stft(x, nfft, hop):
    pad = nfft // 2
    xp = np.pad(x, (pad, pad), mode="reflect")
    nfr = 1 + (len(xp) - nfft) // hop
    idx = np.arange(nfft)[None, :] + hop * np.arange(nfr)[:, None]
    return xp[idx] * np.hanning(nfft + 1)[:-1]


def _istft(frames, nfft, hop, length):
    out = np.zeros(nfft + hop * (len(frames) - 1))
    wsum = np.zeros_like(out)
    w = np.hanning(nfft + 1)[:-1]
    for i, f in enumerate(frames):
        s = i * hop
        out[s:s + nfft] += f * w
        wsum[s:s + nfft] += w * w
    out /= np.maximum(wsum, 1e-8)
    pad = nfft // 2
    return out[pad:pad + length]


def pitch_shift(x, semitones, sr, nfft=2048, hop=512):
    """Hao/cao cao do giu nguyen thoi luong (phase vocoder + resample)."""
    s = 2.0 ** (semitones / 12.0)
    # 1) time-stretch: thoi luong nhan s, cao do giu nguyen
    frames = _stft(x, nfft, hop)
    S = np.fft.rfft(frames, axis=1)
    mag, phase = np.abs(S), np.angle(S)
    nfr = len(frames)
    k = np.arange(S.shape[1])
    phi_adv = 2 * np.pi * k / nfft * hop
    dphase = phase[1:] - phase[:-1] - phi_adv
    phase_acc = np.zeros_like(phase)
    phase_acc[0] = phase[0]
    phase_acc[1:] = phase[0] + np.cumsum(dphase, axis=0)
    # vi tri phan tich (float) cho tung frame dau ra
    positions = np.arange(0, nfr - 1, 1.0 / s)
    i0 = np.floor(positions).astype(int)
    frac = (positions - i0)[:, None]
    mag_o = (1 - frac) * mag[i0] + frac * mag[i0 + 1]
    ph_o = (1 - frac) * phase_acc[i0] + frac * phase_acc[i0 + 1]
    Y = mag_o * np.exp(1j * ph_o)
    y_frames = np.fft.irfft(Y, nfft, axis=1) * np.hanning(nfft + 1)[:-1]
    y = _istft(y_frames, nfft, hop, int(round(len(x) * s)))
    # 2) resample ve dang dai goc: cao do x s, thoi luong goc
    out_len = len(x)
    t_old = np.linspace(0.0, 1.0, len(y), endpoint=False)
    t_new = np.linspace(0.0, 1.0, out_len, endpoint=False)
    y2 = np.interp(t_new, t_old, y).astype(np.float32)
    return y2, s


# ------------------------------------------------------------------ chay
print("=" * 96)
print("TAO BIEN THE CLIP NU THAP cho vai N1 (G9)")
print("=" * 96)

a0, sr = read_wav(SRC)
print("nguon: %s  dur=%.2fs  sr=%d" % (SRC.name, len(a0) / sr, sr))
f0_src_ac, f0_src_p2 = f0_ac(a0, sr), f0_p2(a0, sr)
print("F0 nguon: AC tho=%.1f Hz | AC chuan hoa=%.1f Hz" % (f0_src_ac, f0_src_p2))

trimmed, how, cut_s = trim_silence(a0, sr)
print("trim: %s  (cat %.2f s) -> dur %.2f s" % (how, cut_s, len(trimmed) / sr))
base_ac, base_p2 = f0_ac(trimmed, sr), f0_p2(trimmed, sr)

rows = []
for st in SHIFTS:
    name = "W6_LOW_S%02d" % int(round(abs(st) * 10))
    y, s = pitch_shift(trimmed, st, sr)
    out_p = G9_DIR / (name + ".wav")
    write_wav(out_p, y, sr)
    # .txt giong W6_LOW (cat im lang khong bo chu)
    (G9_DIR / (name + ".txt")).write_text(
        (G9_DIR / "W6_LOW.txt").read_text(encoding="utf-8-sig").strip(),
        encoding="utf-8")
    ya, sr2 = read_wav(out_p)
    f_ac, f_p2 = f0_ac(ya, sr2), f0_p2(ya, sr2)
    dur = len(ya) / sr2
    # du doan clone theo ti le quan sat
    pred_ac_lo = base_ac * s * DRIFT_LO
    pred_ac_hi = base_ac * s * DRIFT_HI
    pred_p2_lo = base_p2 * s * DRIFT_LO
    pred_p2_hi = base_p2 * s * DRIFT_HI
    ok_ac = pred_ac_hi <= TARGET_CLONE_AC_MAX
    ok_p2 = pred_p2_hi <= TARGET_CLONE_PP2_MAX
    ok_dur = LO_SEC <= dur <= HI_SEC
    peak = float(np.max(np.abs(ya)))
    print()
    print("  %-14s  -%.1f st (x%.4f)  dur=%.2fs  F0_ac=%6.1f  F0_pp2=%6.1f  peak=%.3f" % (
        name, abs(st), s, dur, f_ac, f_p2, peak))
    print("       du doan clone ac=%6.1f-%6.1f (can <=%.1f) %s | pp2=%6.1f-%6.1f (can <=%.1f) %s | dur %s" % (
        pred_ac_lo, pred_ac_hi, TARGET_CLONE_AC_MAX, "OK" if ok_ac else "LO",
        pred_p2_lo, pred_p2_hi, TARGET_CLONE_PP2_MAX, "OK" if ok_p2 else "LO",
        "OK" if ok_dur else "LO"))
    rows.append({
        "name": name, "semitones": st, "factor": round(s, 4),
        "dur": round(dur, 2), "f0_ac": round(f_ac, 1), "f0_pp2": round(f_p2, 1),
        "peak": round(peak, 4),
        "pred_clone_ac": [round(pred_ac_lo, 1), round(pred_ac_hi, 1)],
        "pred_clone_pp2": [round(pred_p2_lo, 1), round(pred_p2_hi, 1)],
        "ok_ac": ok_ac, "ok_pp2": ok_p2, "ok_dur": ok_dur,
        "wav": str(out_p.relative_to(ROOT)).replace("\\", "/"),
    })

print()
print("=" * 96)
print("KET LUA: cac bien the DUOC DUNG nếu ok_ac AND ok_pp2 (worst-case drift)")
print("=" * 96)
good = [r for r in rows if r["ok_ac"] and r["ok_pp2"] and r["ok_dur"]]
for r in rows:
    print("  %-14s %s" % (r["name"], "DU" if r in good else "khong"))
if good:
    best = min(good, key=lambda r: r["pred_clone_ac"][1])
    print("\n  -> uu tien: %s  (clone ac uoc <= %.1f Hz)" % (
        best["name"], best["pred_clone_ac"][1]))

OUT.write_text(json.dumps({
    "source": str(SRC.relative_to(ROOT)).replace("\\", "/"),
    "source_f0_ac": round(f0_src_ac, 1), "source_f0_pp2": round(f0_src_p2, 1),
    "trimmed_dur": round(len(trimmed) / sr, 2), "trim_how": how[0] if how else None,
    "trim_seconds": round(cut_s, 2),
    "target_clone_ac_max": TARGET_CLONE_AC_MAX,
    "target_clone_pp2_max": TARGET_CLONE_PP2_MAX,
    "variants": rows,
}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n->", OUT)
