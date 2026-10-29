# -*- coding: utf-8 -*-
"""Đo độ trễ (lag) giữa master cũ và mới bằng tự tương quan.

Nếu có lag khác 0 -> timeline đã dịch -> âm thanh không còn khớp hình.
"""
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"


def read(p):
    with wave.open(str(p), "rb") as w:
        n, ch, sr = w.getnframes(), w.getnchannels(), w.getframerate()
        d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return (d.reshape(-1, ch) if ch == 2 else d), sr


JOBS = [
    ("T02 VN", WORK / "_cu" / "audio_master_t02.wav.bak_bgm", WORK / "audio_master_t02.wav"),
    ("T07 VN", WORK / "_cu" / "audio_master_t07.wav.bak_bgm", WORK / "audio_master_t07.wav"),
    ("T02 EN", WORK / "_cu" / "audio_master_EN_t02.wav.bak_bgm", WORK / "audio_master_EN_t02.wav"),
]
WIN = 8 * 48000          # 8 s
MAXLAG = int(2.0 * 48000)

for label, old_p, new_p in JOBS:
    if not old_p.exists() or not new_p.exists():
        continue
    a, sr = read(old_p)
    b, _ = read(new_p)
    n = min(len(a), len(b))
    print(f"\n=== {label} ===")
    for t in (60, 200, 400, 700, 1000, 1300):
        if t * sr + WIN + MAXLAG > n:
            continue
        x = a[t * sr:t * sr + WIN]
        best, blag = -1e18, 0
        for lag in range(-MAXLAG, MAXLAG + 1, 240):   # bước 5 ms
            y = b[t * sr + lag:t * sr + lag + WIN]
            if y.shape[0] != WIN:
                continue
            c = float((x * y).sum()) / (float(np.sqrt((x * x).sum() * (y * y).sum())) or 1e-12)
            if c > best:
                best, blag = c, lag
        print(f"  t={t:5d}s  lag toi uu = {blag/sr*1000:+8.1f} ms   tuong quan = {best:.4f}")
