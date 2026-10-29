#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bảng mức cuối cùng của assets/sfx/t3/ — max/mean toàn file + mean của 3 đoạn đầu."""
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


def vd(p, extra=()):
    r = subprocess.run([str(FF), "-hide_banner", *extra, "-i", str(p), "-af", "volumedetect",
                        "-f", "null", "-"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    mx = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    mn = re.search(r"mean_volume: (-?[\d.]+) dB", r.stderr)
    return (float(mx.group(1)) if mx else None, float(mn.group(1)) if mn else None)


print(f"{'file':<26}{'dai(s)':>8}{'max dB':>9}{'mean dB':>10}   mean 0-2s / 2-4s / 4-6s")
for w in sorted(OUT.glob("*.wav")):
    d = float(subprocess.run([str(FFP), "-v", "error", "-show_entries", "format=duration",
                              "-of", "default=noprint_wrappers=1:nokey=1", str(w)],
                             capture_output=True, text=True).stdout.strip() or 0)
    mx, mn = vd(w)
    segs = []
    for i in (0, 2, 4):
        if i + 2 <= d:
            m2, _ = vd(w, extra=("-ss", str(i), "-t", "2"))
            segs.append(f"{m2:.0f}" if m2 is not None else "—")
        else:
            segs.append("—")
    print(f"{w.stem:<26}{d:>8.1f}{mx:>9.1f}{mn:>10.1f}   {' / '.join(segs)}")
