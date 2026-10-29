#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phân tích envelope RMS theo từng giây cho các file wav trong assets/sfx/t3/.
Dùng ffmpeg astats với reset=1 → mỗi khung 1 giây có 1 cặp số liệu.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = ROOT / "assets" / "sfx" / "t3"

only = sys.argv[1:] if len(sys.argv) > 1 else None

for w in sorted(OUT.glob("*.wav")):
    if only and w.stem not in only:
        continue
    r = subprocess.run(
        [str(FF), "-hide_banner", "-i", str(w), "-af", "astats=metadata=1:reset=1", "-f", "null", "-"],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    rms = [float(x) for x in re.findall(r"RMS level dB: (-?[\d.]+|-inf)", r.stderr)]
    pk = [float(x) for x in re.findall(r"Peak level dB: (-?[\d.]+|-inf)", r.stderr)]
    rms = [v for v in rms if v > -120]
    pk = [v for v in pk if v > -120]
    n = len(rms)
    print(f"\n=== {w.stem}.wav  ({n} khung ~1s) ===")
    print("  RMS/giay:", " ".join(f"{v:.0f}" for v in rms[:40]))
    if len(rms) > 40:
        print("           ", " ".join(f"{v:.0f}" for v in rms[40:80]))
    if pk:
        print(f"  peak max={max(pk):.1f} dB   rms max={max(rms):.1f} dB   rms tb={(sum(rms)/n):.1f} dB")
