#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo lệch âm thanh – hình của mp4 cuối JA Tap02 so với audio master wav.

Tương quan chéo bằng FFT (O(n log n)) thay cho np.correlate(mode='full') O(n²).
Chuẩn: A11 #64 — |lệch| ≤ 20 ms.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MP4 = ROOT / "02_SAN_XUAT" / "Tap02_JA" / "xuat_ban" / "Tap02_JA_master.mp4"
WAV = WORK / "audio_master_JA_t02.wav"
SR = 8000
WINDOWS = [(30.0, 60.0), (450.0, 480.0), (900.0, 930.0), (1400.0, 1430.0), (1700.0, 1730.0)]


def grab(src, t0, t1):
    p = subprocess.run([str(FF), "-v", "error", "-ss", f"{t0}", "-t", f"{t1 - t0}", "-i", str(src),
                        "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                       capture_output=True)
    if p.returncode != 0 or not p.stdout:
        raise SystemExit(f"khong doc duoc audio: {src}\n{p.stderr.decode('utf-8', 'replace')[:400]}")
    return np.frombuffer(p.stdout, dtype="<i2").astype(np.float32) / 32768.0


def xcorr_full(x, y):
    L = len(x) + len(y) - 1
    N = 1
    while N < L:
        N *= 2
    c = np.fft.irfft(np.fft.rfft(x, N) * np.conj(np.fft.rfft(y, N)), N)
    return np.concatenate([c[N - len(y) + 1:], c[:len(x)]])


def xcorr_lag(x, y, maxlag):
    c = xcorr_full(x, y)
    mid = len(y) - 1
    seg = c[mid - maxlag: mid + maxlag + 1]
    lags = np.arange(-maxlag, maxlag + 1)
    b = int(np.argmax(seg))
    return int(lags[b]), float(seg[b])


def main():
    if not MP4.exists():
        sys.exit(f"CHUA CO {MP4}")
    if not WAV.exists():
        sys.exit(f"CHUA CO {WAV}")

    maxlag = int(SR * 0.10)  # ±100 ms
    lags_ms = []
    print(f"=== ĐO LỆCH A/V (Tap02 JA) ===")
    for t0, t1 in WINDOWS:
        w_wav = grab(WAV, t0, t1)
        w_mp4 = grab(MP4, t0, t1)
        lag, score = xcorr_lag(w_mp4, w_wav, maxlag)
        dt_ms = (lag / SR) * 1000.0
        lags_ms.append(dt_ms)
        print(f"  [{t0:6.1f} - {t1:6.1f} s] lệch = {dt_ms:+6.2f} ms  (score = {score:8.1f})")

    mean_lag = np.mean(lags_ms)
    max_abs = np.max(np.abs(lags_ms))
    print(f"\nTrung bình lệch: {mean_lag:+6.2f} ms · Độ lệch tuyệt đối lớn nhất: {max_abs:6.2f} ms")
    if max_abs <= 20.0:
        print("KET QUA: PASS (<= 20 ms)")
    else:
        print("KET QUA: FAIL (> 20 ms)")


if __name__ == "__main__":
    main()
