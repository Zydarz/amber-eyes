#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sánh nhanh 2 chuỗi limiter (file .m4a đã dựng sẵn) — đo true peak sau AAC
và độ lệch A/V do limiter. Cửa sổ ngắn + FFT nhỏ để không ngốn máy."""
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
WAV = WORK / "audio_master_t03.wav"
TD = WORK / "_limiter_test"
SR = 8000


def loudness(path):
    e = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
                        "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    seg = e[e.rfind("Integrated loudness:"):][:2500]
    I = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", seg)
    LRA = re.findall(r"LRA:\s*(-?[\d.]+)\s*LU", seg)
    PK = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", seg)
    return (float(I[-1]) if I else None, float(LRA[-1]) if LRA else None,
            float(PK[-1]) if PK else None)


def win(path, t0, dur):
    raw = subprocess.run([str(FF), "-v", "error", "-ss", f"{t0}", "-i", str(path), "-t", f"{dur}",
                          "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def lag_ms(a, b):
    n = min(len(a), len(b))
    a = a[:n] - a[:n].mean()
    b = b[:n] - b[:n].mean()
    m = 1 << int(np.ceil(np.log2(2 * n)))
    cc = np.fft.irfft(np.fft.rfft(a, m) * np.conj(np.fft.rfft(b, m)), m)
    k = int(np.argmax(cc[:2000]))
    if k > 1000:
        k -= m
    return k / SR * 1000.0


T0 = 120.0   # đoạn có lời thoại
DUR = 40.0
print(f"Đo trên đoạn {T0:.0f}s + {DUR:.0f}s")
lufs, lra, peak = loudness(WAV)
print(f"WAV gốc        : LUFS={lufs} LRA={lra} true peak={peak} dBFS\n")

ref = win(WAV, T0, DUR)
rows = []
for tag, label in (("A", "A (VN hiện tại) limit=0.7943, KHÔNG latency"),
                   ("B", "B (EN/JA)        limit=0.63 + latency=1")):
    f = TD / f"{tag}.m4a"
    if not f.exists():
        print(f"{tag}: thiếu file")
        continue
    l, lr, p = loudness(f)
    d = lag_ms(ref, win(f, T0, DUR))
    rows.append((tag, label, l, lr, p, d))
    print(f"{label}")
    print(f"   sau AAC 192k : LUFS={l}  LRA={lr}  true peak={p} dBFS")
    print(f"   lệch A/V     : {d:+.2f} ms")
    print(f"   A7 peak<=-1,5 : {'ĐẠT' if p <= -1.5 else 'LOI'}"
          f"   |  |lệch|<=50ms: {'ĐẠT' if abs(d) <= 50 else 'LOI'}")
    print()

print("TÓM TẮT")
for tag, label, l, lr, p, d in rows:
    print(f"  {tag}: peak={p} dBFS · lệch={d:+.2f} ms · "
          f"{'ĐẠT' if p <= -1.5 and abs(d) <= 50 else 'LOI'}")
