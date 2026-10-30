# -*- coding: utf-8 -*-
"""Kiểm tra trực tiếp: bed H3 của T07 đã đổi từ drone sang cello chưa?

So trong khoảng lặng giữa lời thoại (chỉ còn bed):
  - tỉ lệ năng lượng dải thấp 20-150 Hz (drone/sub rất nặng) vs dải trung 300-2000 Hz (cello)
  - tương quan mẫu cũ/mới
"""
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"


def read(p):
    with wave.open(str(p), "rb") as w:
        n, ch, sr = w.getnframes(), w.getnchannels(), w.getframerate()
        d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return (d.reshape(-1, ch) if ch == 2 else d), sr


def band_ratio(x, sr, f1=20, f2=150, f3=300, f4=2000):
    """Tỉ lệ năng lượng dải thấp / dải trung (dùng FFT đơn giản)."""
    if x.ndim > 1:
        x = x.mean(axis=1)
    X = np.abs(np.fft.rfft(x * np.hanning(len(x))))
    f = np.fft.rfftfreq(len(x), 1 / sr)
    low = X[(f >= f1) & (f < f2)].sum()
    mid = X[(f >= f3) & (f < f4)].sum()
    return float(low / max(mid, 1e-12))


def quietest_window(x, sr, a, b, win=1.0):
    """Cửa sổ yên tĩnh nhất trong [a,b] (theo RMS)."""
    k = int(win * sr)
    best, bi = 1e9, int(a * sr)
    for s in range(int(a * sr), int(b * sr) - k, k // 2):
        seg = x[s:s + k]
        r = float(np.sqrt((seg ** 2).mean()))
        if r < best:
            best, bi = r, s
    return bi, best


for label, old_p, new_p, acts in [
    ("T07 VN", WORK / "_cu" / "audio_master_t07.wav.bak_bgm", WORK / "audio_master_t07.wav",
     {1: (23.0, 296.6), 2: (298.6, 565.1), 3: (567.1, 798.0),
      4: (800.0, 1067.5), 5: (1069.5, 1300.6)}),
    ("T02 VN", WORK / "_cu" / "audio_master_t02.wav.bak_bgm", WORK / "audio_master_t02.wav",
     {1: (23.0, 325.7), 2: (327.7, 572.4), 3: (574.4, 918.1),
      4: (920.1, 1258.4), 5: (1260.4, 1596.7)}),
]:
    if not old_p.exists() or not new_p.exists():
        continue
    a, sr = read(old_p)
    b, _ = read(new_p)
    print(f"\n=== {label} (sr={sr}) ===")
    print(f"{'Hoi':<5}{'vi tri (s)':<14}{'lo/mid CU':>10}{'lo/mid MOI':>11}{'tuong quan':>12}")
    print("-" * 56)
    for act, (s, e) in sorted(acts.items()):
        i, rms_q = quietest_window(b, sr, s, e)
        j = min(i + int(1.0 * sr), len(b))
        xo, xn = a[i:j], b[i:j]
        if xo.size == 0:
            continue
        r_old = band_ratio(xo, sr)
        r_new = band_ratio(xn, sr)
        num = float((xo * xn).sum())
        den = float(np.sqrt((xo * xo).sum() * (xn * xn).sum())) or 1e-12
        print(f"H{act:<4}{f'{i/sr:.1f}':<14}{r_old:>10.2f}{r_new:>11.2f}{num/den:>12.4f}")
