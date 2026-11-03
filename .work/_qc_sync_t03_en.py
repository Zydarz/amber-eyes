#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo lệch âm thanh – hình của mp4 cuối Tap03 EN so với audio master.

Dùng tương quan chéo bằng FFT (O(n log n)) thay cho np.correlate(mode='full') O(n^2)
(A11 #109: 480.000 mẫu = 2,3e11 phép -> treo máy).

Ký hiệu:
  c[m] = Σ x[n]·y[n-m]  (x = mp4, y = master wav)
  -> đỉnh tại m = độ trễ của âm thanh trong mp4 so với master (ms).

Có self-test: dịch tín hiệu vài mẫu, kiểm đúng dấu ở cả hai chiều.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MP4 = ROOT / "02_SAN_XUAT" / "Tap03_EN" / "xuat_ban" / "Tap03_EN_master.mp4"
WAV = WORK / "audio_master_EN_t03.wav"
SR = 8000
WINDOWS = [(120.0, 150.0), (400.0, 430.0), (900.0, 930.0), (1400.0, 1430.0)]


def grab(src, t0, t1):
    p = subprocess.run([str(FF), "-v", "error", "-ss", f"{t0}", "-t", f"{t1 - t0}", "-i", str(src),
                        "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                       capture_output=True)
    if p.returncode != 0 or not p.stdout:
        raise SystemExit(f"khong doc duoc audio: {src}\n{p.stderr.decode('utf-8', 'replace')[:400]}")
    return np.frombuffer(p.stdout, dtype="<i2").astype(np.float32) / 32768.0


def xcorr_lag(x, y, maxlag):
    """Trả (lag_mau, r) : lag > 0 nghĩa là x trễ hơn y."""
    c = xcorr_full(x, y)
    mid = len(y) - 1
    seg = c[mid - maxlag: mid + maxlag + 1]
    lags = np.arange(-maxlag, maxlag + 1)
    b = int(np.argmax(seg))
    return int(lags[b]), float(seg[b])


def xcorr_full(x, y):
    """Tương quan chéo TUYẾN TÍNH theo thứ tự lag: index i <-> lag = i - (len(y)-1).

    c[m] = SUM_n x[n]*y[n-m] (định lý tương quan DFT).
    Với mảng vòng N >= len(x)+len(y)-1: lag >= 0 nằm ở index m, lag < 0 nằm ở
    index N+m ⇒ phải GHÉP phần đuôi (lag âm) + phần đầu (lag >= 0).
    """
    L = len(x) + len(y) - 1
    N = 1
    while N < L:
        N *= 2
    c = np.fft.irfft(np.fft.rfft(x, N) * np.conj(np.fft.rfft(y, N)), N)
    return np.concatenate([c[N - len(y) + 1:], c[:len(x)]])


def self_test():
    """Kiểm tra dấu + chỉ số của xcorr_lag bằng tín hiệu tổng hợp.

    PHẢI kiểm 2 điều:
      (1) FFT khớp `np.correlate` (chuẩn chính xác) trên mảng ngắn;
      (2) dấu của lag: x = y dịch PHẢI d  =>  lag = +d.
    """
    rng = np.random.default_rng(7)
    sig = rng.standard_normal(2048).astype(np.float32)
    k = 37

    def shift_right(a, k):
        out = np.zeros_like(a)
        out[k:] = a[:-k]
        return out

    c_fft = xcorr_full(sig, shift_right(sig, k))
    c_ref = np.correlate(sig, shift_right(sig, k), mode="full")
    same = c_fft.shape == c_ref.shape and np.allclose(c_fft, c_ref, atol=1e-3)
    print(f"self-test (1): FFT == np.correlate: {same} · max|sai lệch| = "
          f"{float(np.abs(c_fft - c_ref).max()):.2e}")
    if not same:
        raise SystemExit("self-test that bai - FFT khong khop np.correlate")
    l1, r1 = xcorr_lag(sig, shift_right(sig, k), 200)
    l2, r2 = xcorr_lag(shift_right(sig, k), sig, 200)
    ok = (l1 == -k) and (l2 == k)
    print(f"self-test (2): shift(+{k}) -> lag {l1} (mong doi {-k}) · lag {l2} (mong doi {k}) · "
          f"r={r1:.4f}/{r2:.4f} -> {'OK' if ok else 'LOI'}")
    if not ok:
        raise SystemExit("self-test that bai - dau lag sai")
    return ok


self_test()

MAXLAG = int(0.3 * SR)          # ±300 ms
print()
worst = 0.0
rows = []
for t0, t1 in WINDOWS:
    x = grab(MP4, t0, t1)
    y = grab(WAV, t0, t1)
    n = min(len(x), len(y))
    x, y = x[:n], y[:n]
    x = x - x.mean()
    y = y - y.mean()
    x /= (np.linalg.norm(x) + 1e-9)
    y /= (np.linalg.norm(y) + 1e-9)
    lag, r = xcorr_lag(x, y, MAXLAG)
    ms = lag / SR * 1000
    worst = max(worst, abs(ms))
    rows.append((t0, t1, lag, ms, r))
    print(f"  {t0:7.0f}-{t1:7.0f} s · lag {lag:+5d} mau = {ms:+7.1f} ms · r = {r:.4f}")

print()
print(f"lech A/V lon nhat: {worst:.1f} ms (chuan A11 #64: <= 20 ms)")
if worst > 20:
    print("!! LECH > 20 ms")
    sys.exit(1)
print("OK: lech <= 20 ms")
