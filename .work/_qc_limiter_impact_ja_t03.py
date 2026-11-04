#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo mức độ bóp đỉnh của alimiter trên master JA: bao nhiêu mẫu vượt trần?

- trần 0.7943 (-2,0 dBFS) = chuỗi MẶC ĐỊNH (không có latency=1)
- trần 0.63   (-4,0 dBFS) = chuỗi ĐÃ SỬA (khớp bản EN đã chứng minh)
"""
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = r"D:/TEST/Gax/amber-eyes/.work/audio_master_JA_t03.wav"

with wave.open(P, "rb") as w:
    nch = w.getnchannels()
    sw = w.getsampwidth()
    sr = w.getframerate()
    nf = w.getnframes()
    print(f"wav: {nf} frames · {nch} ch · {sw*8} bit · {sr} Hz · {nf/sr:.3f} s")
    raw = w.readframes(nf)

a = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
a = a.reshape(-1, nch)
mono = a.max(axis=1)                     # trên cùng stereo (worst case)
peak = float(np.abs(mono).max())
print(f"đỉnh mẫu (max|stereo|) = {20*np.log10(peak):.3f} dBFS")
tot = mono.size
for thr_db, lab in [(-2.0, "0.7943 (mặc định)"), (-3.0, "0.708"), (-4.0, "0.63 (đã sửa)")]:
    thr = 10 ** (thr_db / 20)
    over = np.abs(mono) > thr
    n = int(over.sum())
    # số đoạn liên tiếp bị bóp
    if n:
        idx = np.flatnonzero(over)
        segs = 1 + int((np.diff(idx) > 1).sum())
        dur_s = n / sr
    else:
        segs = 0
        dur_s = 0.0
    print(f"  trần {thr_db:+.1f} dBFS ({lab}): {n} mẫu = {dur_s:.3f} s · {n/tot*100:.4f}% · {segs} đoạn liên tiếp")

# khoảng cách giữa các đỉnh để ước lượng pumping
idx = np.flatnonzero(np.abs(mono) > 10 ** (-2.0 / 20))
if idx.size > 1:
    gaps = np.diff(idx) / sr
    print(f"  khoảng cách giữa 2 đỉnh vượt -2 dBFS: median {np.median(gaps):.2f} s · p10 {np.percentile(gaps,10):.2f} s")
else:
    print(f"  chỉ {idx.size} đỉnh vượt -2 dBFS (dưới ngưỡng thống kê)")
