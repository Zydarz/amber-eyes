#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo max_volume (dBFS) của các file mp3 trong inbox."""
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"

names = sys.argv[1:]
if not names:
    names = sorted(p.stem for p in INBOX.glob("*.mp3"))

for n in names:
    p = INBOX / (n + ".mp3")
    if not p.exists():
        print("%-40s KHONG CO FILE" % n)
        continue
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(p), "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    md = re.search(r"mean_volume: (-?[\d.]+) dB", r.stderr)
    dur = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    d = "-"
    if dur:
        d = "%.1f" % (int(dur.group(1)) * 3600 + int(dur.group(2)) * 60 + float(dur.group(3)))
    print("%-40s max=%-8s mean=%-8s dur=%-8s size=%d" % (
        n, m.group(1) if m else "?", md.group(1) if md else "?", d, p.stat().st_size))
