#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cắt vùng badge vai (trái trên) của 1 ảnh tĩnh để soi sóng âm."""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]

src = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / ".work/video3_t03/stills/shot_1-01.png")
out = sys.argv[2] if len(sys.argv) > 2 else str(ROOT / ".work/_qc_t03_20261105/badge_zoom.png")
im = Image.open(src).convert("RGB")
crop = im.crop((40, 40, 640, 200)).resize((1800, 480), Image.LANCZOS)
Path(out).parent.mkdir(parents=True, exist_ok=True)
crop.save(out)
print("->", out, crop.size)
