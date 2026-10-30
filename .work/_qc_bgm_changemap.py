# -*- coding: utf-8 -*-
"""Bản đồ thay đổi: mỗi giây, độ lệch giữa master cũ và mới.

In ra các đoạn thời gian thay đổi liên tiếp (RMS lệch > ngưỡng) để biết
bed thực sự thay đổi ở đâu.
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


JOBS = [
    ("T02 VN", WORK / "_cu" / "audio_master_t02.wav.bak_bgm", WORK / "audio_master_t02.wav"),
    ("T07 VN", WORK / "_cu" / "audio_master_t07.wav.bak_bgm", WORK / "audio_master_t07.wav"),
    ("T02 EN", WORK / "_cu" / "audio_master_EN_t02.wav.bak_bgm", WORK / "audio_master_EN_t02.wav"),
]
THRESH = 0.004          # RMS lệch mỗi giây

for label, old_p, new_p in JOBS:
    if not old_p.exists() or not new_p.exists():
        continue
    a, sr = read(old_p)
    b, _ = read(new_p)
    n = min(len(a), len(b))
    k = sr
    diffs = []
    for s in range(0, n - k, k):
        x, y = a[s:s + k], b[s:s + k]
        d = float(np.sqrt(((y - x) ** 2).mean()))
        diffs.append((s / sr, d))
    mx = max(d for _, d in diffs)
    print(f"\n=== {label} ===  max RMS lech/giay = {mx:.5f}  (nguong {THRESH})")
    seg, start = [], None
    for t, d in diffs + [(None, None)]:
        hot = d is not None and d > THRESH
        if hot and start is None:
            start = t
        elif not hot and start is not None:
            seg.append((start, t))
            start = None
    if not seg:
        print("  (khong co doan nao vuot nguong)")
    for s, e in seg:
        print(f"  THAY DOI: {s:8.1f} s -> {e:8.1f} s   (dai {e-s:.1f} s)")
    # top 10 giay lech nhat
    top = sorted(diffs, key=lambda x: -x[1])[:10]
    print("  top 10 giay lech lon nhat: " +
          ", ".join(f"{t:.0f}s({d:.4f})" for t, d in top))
