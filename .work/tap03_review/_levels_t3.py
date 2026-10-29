#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo max_volume / mean_volume thật của file wav cuối cùng trong assets/sfx/t3/.
Ngoài ra: RMS theo từng giây (chia đoạn 1 s bằng atrim + volumedetect) để thấy hình dạng envelope.
"""
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFP = FF.with_name("ffprobe.exe")
OUT = ROOT / "assets" / "sfx" / "t3"


def vd(path, extra=()):
    r = subprocess.run([str(FF), "-hide_banner", *extra, "-i", str(path), "-af", "volumedetect",
                        "-f", "null", "-"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    mx = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    mn = re.search(r"mean_volume: (-?[\d.]+) dB", r.stderr)
    return (float(mx.group(1)) if mx else None, float(mn.group(1)) if mn else None)


def dur(p):
    r = subprocess.run([str(FFP), "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


for w in sorted(OUT.glob("*.wav")):
    d = dur(w)
    mx, mn = vd(w)
    print(f"\n=== {w.stem}.wav  {d:.1f}s ===")
    print(f"  max={mx} dB   mean={mn} dB")
    n = min(int(d), 24)
    row = []
    for i in range(n):
        m2, _ = vd(w, extra=("-ss", str(i), "-t", "1"))
        row.append("—" if m2 is None else f"{m2:.0f}")
    print("  max/s:", " ".join(row))
