#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envelope chi tiết 0,25 s cho các tiếng động độc lập trong assets/sfx/t3/ — dùng để chọn điểm cắt.
Chỉ in các đoạn có max trên -45 dB (phần có tiếng), bỏ qua khoảng lặng.
"""
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = ROOT / "assets" / "sfx" / "t3"

STEP = 0.25
THRESH = -45.0

for w in sorted(OUT.glob("fx_*.wav")):
    print(f"\n=== {w.stem}.wav ===")
    t = 0.0
    parts = []
    while t < 20.0:
        r = subprocess.run([str(FF), "-hide_banner", "-ss", f"{t:.2f}", "-t", str(STEP), "-i", str(w),
                            "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        m = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
        v = float(m.group(1)) if m else -120.0
        if v > THRESH:
            parts.append(f"{t:5.2f}s:{v:6.1f}")
        t += STEP
        if len(parts) and t > 20:
            break
    # gom thành nhóm liên tiếp
    print("  co tieng:", " ".join(parts) if parts else "(khong co gi)")
