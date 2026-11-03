#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo lệch âm thanh – hình của mp4 cuối so với audio master (tương quan chéo).

So sánh cùng một đoạn có lời nói: mp4 cuối (AAC) vs audio_master_t07.wav (PCM).
Lệch = đỉnh tương quan dịch chuyển (ms). 0 = khớp.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MP4 = ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "Tap07_master.mp4"
WAV = WORK / "audio_master_t07.wav"
SR = 8000
T0, T1 = 100.0, 160.0


def grab(src):
    p = subprocess.run([str(FF), "-v", "error", "-ss", f"{T0}", "-t", f"{T1 - T0}", "-i", str(src),
                        "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                       capture_output=True)
    if p.returncode != 0 or not p.stdout:
        raise SystemExit(f"khong doc duoc audio: {src}\n{p.stderr.decode('utf-8', 'replace')[:400]}")
    a = np.frombuffer(p.stdout, dtype="<i2").astype(np.float32)
    return a / 32768.0


a_mp4 = grab(MP4)
a_wav = grab(WAV)
n = min(len(a_mp4), len(a_wav))
a_mp4, a_wav = a_mp4[:n], a_wav[:n]

# chuẩn hoá năng lượng để tương quan không bị lệch biên độ
a_mp4 = a_mp4 - a_mp4.mean()
a_wav = a_wav - a_wav.mean()
a_mp4 /= (np.linalg.norm(a_mp4) + 1e-9)
a_wav /= (np.linalg.norm(a_wav) + 1e-9)

MAXLAG = int(0.3 * SR)          # ±300 ms
full = np.correlate(a_mp4, a_wav, mode="full")
mid = len(a_wav) - 1
seg = full[mid - MAXLAG: mid + MAXLAG + 1]
lags = np.arange(-MAXLAG, MAXLAG + 1)
best = int(np.argmax(seg))
corr = float(seg[best])

print(f"doan so sanh: {T0:.0f}–{T1:.0f} s · {SR} Hz mono · {n} mau")
print(f"dinh tuong quan: lag = {lags[best]} mau = {lags[best] / SR * 1000:.1f} ms · r = {corr:.4f}")
if abs(lags[best]) > int(0.02 * SR):
    print("!! LECH > 20 ms")
    sys.exit(1)
print("OK: lech <= 20 ms")
