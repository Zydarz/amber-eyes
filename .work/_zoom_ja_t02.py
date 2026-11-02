#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zoom vao vung nghi ngo cua anh tinh JA Tap02 de soi ky (H2/H5/A9.3)."""
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SD = ROOT / ".work" / "video3_JA_t02" / "stills"
OUT = ROOT / ".work" / "_cu" / "ja_t02_zoom"
OUT.mkdir(parents=True, exist_ok=True)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# (shot, (x0,y0,x1,y1) theo 1920x1080, ten)
JOBS = [
    ("1-05", (620, 300, 1320, 720), "zoom_1-05_46tuoi"),
    ("1-24", (700, 380, 1400, 780), "zoom_1-24_watermark"),
    ("1-29", (40, 760, 1100, 1040), "zoom_1-29_text_mascot"),
    ("1-03", (1250, 40, 1920, 420), "zoom_1-03_card"),
    ("1-04", (1250, 40, 1920, 420), "zoom_1-04_card"),
]

for sid, box, name in JOBS:
    p = SD / f"shot_{sid}.png"
    if not p.exists():
        print("thieu", p)
        continue
    with Image.open(p) as im:
        crop = im.crop(box)
        w, h = crop.size
        crop = crop.resize((w * 2, h * 2), Image.Resampling.LANCZOS)
        out = OUT / f"{name}.png"
        crop.save(out)
        print(f"{sid} -> {out.name} ({crop.size[0]}x{crop.size[1]})")
