#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sánh 2 chuỗi limiter khi đóng gói (A7 / A11 #64) — đo TRƯỚC khi mux thật.

Chuỗi A (đang khai cho VN): alimiter=limit=0.7943:...:level=disabled
Chuỗi B (chuỗi EN/JA):     alimiter=limit=0.63:...:level=disabled:latency=1

Đo trên chính audio master của Tập 03:
  1. true peak / LUFS sau khi AAC 192k (giống hệt bước mux)
  2. độ lệch A/V do limiter thêm vào (tự tương quan sóng âm trước/sau)
"""
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
TMP = WORK / "_limiter_test"
TMP.mkdir(exist_ok=True)

CHAINS = {
    "A (VN hiện tại, limit=0.7943, KHÔNG latency)":
        "alimiter=limit=0.7943:attack=5:release=50:level=disabled",
    "B (EN/JA, limit=0.63 + latency=1)":
        "alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1",
}


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


def to_pcm(path, n=12_000_000):
    raw = subprocess.run([str(FF), "-v", "error", "-i", str(path), "-f", "f32le",
                          "-ac", "1", "-ar", "48000", "-t", "120", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def lag_ms(a, b, sr=48000):
    """Trễ của b so với a (ms) qua tự tương quan."""
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    a = a - a.mean()
    b = b - b.mean()
    m = 1 << int(np.ceil(np.log2(2 * n)))
    A = np.fft.rfft(a, m)
    B = np.fft.rfft(b, m)
    cc = np.fft.irfft(A * np.conj(B), m)
    k = int(np.argmax(cc[:4000]))
    if k > 2000:
        k -= m
    return k / sr * 1000.0


print(f"Audio master: {WAV.name}")
lufs, lra, peak = loudness(WAV)
print(f"  WAV goc      : LUFS={lufs}  LRA={lra}  true peak={peak} dBFS\n")

ref = to_pcm(WAV)
results = {}
for name, chain in CHAINS.items():
    out_aac = TMP / (name.split()[0] + ".m4a")
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(WAV), "-af", chain,
                    "-c:a", "aac", "-b:a", "192k", str(out_aac)], check=True)
    l, lr, p = loudness(out_aac)
    cur = to_pcm(out_aac)
    d = lag_ms(ref, cur)
    results[name] = (l, lr, p, d)
    print(f"{name}")
    print(f"  sau AAC      : LUFS={l}  LRA={lr}  true peak={p} dBFS")
    print(f"  lech A/V     : {d:+.2f} ms")
    print(f"  A7 true peak <= -1,5 dBFS ? {'ĐẠT' if p is not None and p <= -1.5 else 'LOI'}")
    print(f"  |lech| <= 50 ms ?          {'ĐẠT' if abs(d) <= 50 else 'LOI'}")
    print()

print("TÓM TẮT")
for name, (l, lr, p, d) in results.items():
    print(f"  {name[:2]}: peak={p} dBFS · lệch={d:+.2f} ms · "
          f"{'ĐẠT' if p <= -1.5 and abs(d) <= 50 else 'LOI'}")
