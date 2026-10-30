"""Tao bien the clip tham chieu cho vai N1 bang TD-PSOLA (sach, khong phase vocoder).

LY DO (sau pilot v6 + kiem tra ASR tren clip goc)
--------------------------------------------------
Pilot v6 do duoc: clone tu W6_LOW_S25..S40 co CER 9,5-12,5% (bo danh tu rieng),
trong khi clip goc ASR chinh rat sach (S25 = 0,00%). => loi do khi CLONE,
khong phai loi cua clip.

Hai nghi van ( tach ra bang 2 bien the):
  (1) phase vocoder lam nho waveform -> codec tao token rac -> model "do loi" nghe
  (2) g9_shift_clip.py CAT 0,80 s im lang O GIUA CAU (5,76-6,56 s) -> noi truc tiep
      2 doan am -> moc ghep trong clip tham chieu

Bien the tao o day:
  W6_LOW_PSxx  : TD-PSOLA (giu nguyen doan waveform) + resample FFT, KHONG cat im lang
  W6_LOW_TRIM  : chi cat im lang (khong doi cao do) -> test rieng goc (2)

Usage: python .work/g9_psola_shift.py
"""
import json
import pathlib
import sys

import numpy as np
from scipy import signal

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from voice_audition import f0_median as f0_ac  # noqa: E402

G9_DIR = ROOT / "assets" / "voice_ref_voxcpm2_g9"
SRC = G9_DIR / "W6_LOW.wav"
OUT = HERE / "g9_psola_shift.json"

# so nua cung can ha (am = hao). alpha = 2**(st/12)
SHIFTS = [-1.5, -2.0, -2.5, -3.0]
FMIN, FMAX = 60.0, 400.0
HOP_S, WIN_S = 0.002, 0.040


# ------------------------------------------------------------------ io
def read_wav(p):
    import wave
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
    import wave
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


# ------------------------------------------------------------------ pitch marks
def frame_f0(x, sr):
    """F0 + tam khung (tu phoi 5 ms, win 40 ms)."""
    hopn = int(HOP_S * sr)
    winn = int(WIN_S * sr)
    lo, hi = int(sr / FMAX), int(sr / FMIN)
    f0s, cs = [], []
    for s in range(0, len(x) - winn, hopn):
        f = x[s:s + winn]
        c = s + winn // 2
        if np.sqrt((f ** 2).mean()) < 0.005:
            f0s.append(0.0)
            cs.append(c)
            continue
        f = f - f.mean()
        n = len(f)
        nfft = 1 << int(np.ceil(np.log2(2 * n)))
        F = np.fft.rfft(f, nfft)
        ac = np.fft.irfft(F * np.conj(F), nfft)[:n]
        if ac[0] <= 0:
            f0s.append(0.0)
            cs.append(c)
            continue
        acn = ac / ac[0]
        k = lo + int(np.argmax(acn[lo:hi]))
        if acn[k] < 0.30:
            f0s.append(0.0)
            cs.append(c)
            continue
        shift = 0.0
        if 0 < k < n - 1:
            a0, a1, a2 = acn[k - 1], acn[k], acn[k + 1]
            d = a0 - 2 * a1 + a2
            if d != 0:
                shift = 0.5 * (a0 - a2) / d
        f0s.append(sr / (k + shift))
        cs.append(c)
    return np.array(f0s), np.array(cs)


def build_marks(x, sr):
    """Danh dau nhip: MOT dau moi CHU KY (khong phai moi khung 5 ms).

    Diem danh dau = cuc boi cuc day thong thap 900 Hz (nhip thanh).
    """
    b_lp, a_lp = signal.butter(4, 900.0 / (sr / 2), "low")
    xl = signal.filtfilt(b_lp, a_lp, x)
    f0s, cs = frame_f0(x, sr)
    voiced = [(int(c), float(f)) for c, f in zip(cs, f0s) if f > 0]
    if len(voiced) < 10:
        return [], xl

    def refine(pred, T0):
        """Chon cuc boi cuc LOCAL MAX gan vi tri du doan nhat (giu nhat quan pha)."""
        a = max(1, int(pred - T0 * 0.5))
        b = min(len(xl) - 1, int(pred + T0 * 0.5))
        if b - a < 8:
            return int(pred)
        seg = xl[a:b]
        is_peak = np.zeros(len(seg), dtype=bool)
        is_peak[1:-1] = (seg[1:-1] >= seg[:-2]) & (seg[1:-1] > seg[2:])
        idx = np.flatnonzero(is_peak)
        if len(idx) == 0:
            return a + int(np.argmax(np.abs(seg)))
        abs_idx = idx + a
        j = int(np.argmin(np.abs(abs_idx - pred)))
        return int(abs_idx[j])

    marks = []
    if not voiced:
        return marks, xl
    # 1) diem dau: lam theo khung vang dau tien
    c0, f00 = voiced[0]
    T0 = sr / f00
    m = refine(c0, T0)
    marks.append((m, T0))
    # 2) moi chu ky: dung MOT lan, T0 lay tu bang do F0 cuc bo
    #    (khong phu thuoc vi tri khung -> so nhip = so chu ky that)
    import bisect
    ccs = [c for c, _ in voiced]
    ffs = [f for _, f in voiced]
    limit = ccs[-1] + 4 * T0
    while m < limit:
        i = bisect.bisect_right(ccs, m) - 1
        if i < 0:
            break
        f = ffs[i]
        if f <= 0:
            break
        T0 = sr / f
        m2 = refine(m + T0, T0)
        if m2 <= m:
            m2 = int(m + T0)
        marks.append((m2, T0))
        m = m2
    return marks, xl


# ------------------------------------------------------------------ TD-PSOLA
def psola_pitch_shift(x, sr, semitones):
    """Hao/cao cao do giu nguyen thoi luong. TD-PSOLA + resample FFT."""
    alpha = 2.0 ** (semitones / 12.0)
    marks, xl = build_marks(x, sr)
    M = len(marks)
    if M < 20:
        raise SystemExit("khong du pitch marks: %d" % M)
    # --- buoc 1: time-scale x alpha (F0 giu nguyen), alpha<1 => ngan
    # khoang cach tong hop = chu ky that cua nguon, DO CHUNG VOI bo do F0 du dung
    f0_src = f0_ac(x, sr)
    if f0_src <= 0:
        f0_src = 180.0
    T0m = sr / f0_src
    out_len = int(round(len(x) * alpha))
    J = max(8, int(round(out_len / T0m)))
    out = np.zeros(out_len + 4 * sr, dtype=np.float32)
    wsum = np.zeros_like(out)
    for j in range(J):
        ia = int(round(j * M / J))
        ia = min(M - 1, max(0, ia))
        m, T0 = marks[ia]
        L = max(16, int(round(T0)))
        a = max(0, m - L)
        b = min(len(x), m + L)
        seg = x[a:b]
        if len(seg) < 16:
            continue
        w = np.hanning(len(seg) + 1)[:len(seg)]
        s = int(round(j * T0m)) - len(seg) // 2
        e = s + len(seg)
        if s < 0 or e > len(out):
            continue
        out[s:e] += seg * w
        wsum[s:e] += w * w
    print("      [psola] wsum: median=%.3f max=%.3f | out truoc chuan hoa peak=%.3f"
          % (float(np.median(wsum)), float(np.max(wsum)), float(np.max(np.abs(out)))))
    # chuan hoa: tranh chia cho wsum ~ 0 (canh bien cua Hann) -> dinh gia
    pos = wsum[wsum > 0]
    wref = float(np.median(pos)) if len(pos) else 1.0
    out = out / np.maximum(wsum, 0.25 * wref)
    y = out[:out_len]
    # chuan hoa bien do ve goc (dung phan vi, tranh 1 dinh gia lam lech)
    pk0 = float(np.percentile(np.abs(x), 99.9)) or 1.0
    pk1 = float(np.percentile(np.abs(y), 99.9))
    if pk1 > 0:
        y = (y * (pk0 / pk1)).astype(np.float32)
    # --- buoc 2: resample ve thoi luong goc (FFT, band-limited) -> F0 * alpha
    print("      [psola] len x=%d M=%d J=%d out_len=%d | y rms=%.4f peak=%.3f"
          % (len(x), M, J, out_len, float(np.sqrt((y ** 2).mean())), pk1))
    y2 = signal.resample(y, len(x)).astype(np.float32)
    print("      [psola] sau resample len=%d rms=%.4f"
          % (len(y2), float(np.sqrt((y2 ** 2).mean()))))
    return y2


# ------------------------------------------------------------------ cat im lang an toan
def trim_edges(x, sr, max_dur=28.0, thr_db=-40.0):
    """Cat im lang o DAU/CUOI (khong cat giua cau -> khong sinh moc ghep)."""
    need = len(x) / sr - max_dur
    if need <= 0:
        return x, 0.0
    win = int(0.02 * sr)
    nfr = len(x) // win
    fr = np.abs(x[:nfr * win].reshape(nfr, win)).max(axis=1)
    db = 20 * np.log10(fr + 1e-9)
    sil = db < thr_db
    # dau
    i = 0
    while i < nfr and sil[i]:
        i += 1
    head = i * win
    # cuoi
    j = nfr - 1
    while j >= 0 and sil[j]:
        j -= 1
    tail = (nfr - 1 - j) * win
    if (head + tail) / sr >= need:
        cut = int(need * sr)
        if cut <= head:
            return x[head:], head / sr
        if cut <= tail:
            return x[:len(x) - tail], tail / sr
        keep = int(need * sr)
        return x[head:len(x) - tail], (head + tail) / sr
    return x, 0.0


# ------------------------------------------------------------------ chay
print("=" * 96)
print("TAO BIEN THE CLIP (TD-PSOLA) + BIEN THE CHI CAT IM LANG")
print("=" * 96)

x0, sr = read_wav(SRC)
print("nguon: %s  dur=%.2fs  sr=%d" % (SRC.name, len(x0) / sr, sr))
print("F0 nguon: AC tho=%.1f Hz | AC chuan hoa=%.1f Hz"
      % (f0_ac(x0, sr), f0_p2(x0, sr)))

txt_src = (G9_DIR / "W6_LOW.txt").read_text(encoding="utf-8-sig").strip()

rows = []

# --- bien the CHI CAT im lang (khong doi cao do) -> tach nghi van "moc ghep"
trimmed, cut = trim_edges(x0, sr)
# cat im lang giua cau y het (5,76-6,56 s) de tao moc ghep y het
win = int(0.02 * sr)
nfr = len(x0) // win
fr = np.abs(x0[:nfr * win].reshape(nfr, win)).max(axis=1)
db = 20 * np.log10(fr + 1e-9)
sil = db < -40
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
a, b = max(runs, key=lambda r: r[1] - r[0])
splice = np.concatenate([x0[:a], x0[b:]])
write_wav(G9_DIR / "W6_LOW_TRIM.wav", splice, sr)
(G9_DIR / "W6_LOW_TRIM.txt").write_text(txt_src, encoding="utf-8")
sa, ss = read_wav(G9_DIR / "W6_LOW_TRIM.wav")
print()
print("  %-14s cat im lang %.2f-%.2f s (khong doi cao do)  dur=%.2fs  F0_ac=%.1f  F0_pp2=%.1f"
      % ("W6_LOW_TRIM", a / sr, b / sr, len(sa) / ss, f0_ac(sa, ss), f0_p2(sa, ss)))
rows.append({"name": "W6_LOW_TRIM", "kind": "trim-only", "semitones": 0.0,
              "dur": round(len(sa) / ss, 2), "f0_ac": round(f0_ac(sa, ss), 1),
              "f0_pp2": round(f0_p2(sa, ss), 1)})

# --- bien the TD-PSOLA (KHONG cat im lang)
for st in SHIFTS:
    name = "W6_LOW_PS%02d" % int(round(abs(st) * 10))
    y = psola_pitch_shift(x0, sr, st)
    y, cut = trim_edges(y, sr)
    out_p = G9_DIR / (name + ".wav")
    write_wav(out_p, y, sr)
    (G9_DIR / (name + ".txt")).write_text(txt_src, encoding="utf-8")
    ya, sr2 = read_wav(out_p)
    dur = len(ya) / sr2
    f_ac, f_p2 = f0_ac(ya, sr2), f0_p2(ya, sr2)
    print()
    print("  %-14s %+.1f st (x%.4f)  dur=%.2fs  F0_ac=%6.1f  F0_pp2=%6.1f  peak=%.3f"
          % (name, st, 2 ** (st / 12), dur, f_ac, f_p2, float(np.max(np.abs(ya)))))
    rows.append({"name": name, "kind": "psola", "semitones": st,
                 "factor": round(2 ** (st / 12), 4), "dur": round(dur, 2),
                 "f0_ac": round(f_ac, 1), "f0_pp2": round(f_p2, 1)})

OUT.write_text(json.dumps({"source": str(SRC.relative_to(ROOT)).replace("\\", "/"),
                           "source_f0_ac": round(f0_ac(x0, sr), 1),
                           "source_f0_pp2": round(f0_p2(x0, sr), 1),
                           "variants": rows}, ensure_ascii=False, indent=1),
              encoding="utf-8")
print("\n->", OUT)

