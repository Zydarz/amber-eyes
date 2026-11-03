#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung contact sheet 12 anh/tab de QC bang mat (H9) — .work/video3_t07/stills."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
SD = ROOT / ".work/video3_t07/stills"
OUT = ROOT / ".work/video3_t07/qc"
OUT.mkdir(parents=True, exist_ok=True)

files = sorted(SD.glob("shot_*.png"),
               key=lambda p: (int(p.stem.split("_")[1].split("-")[0]),
                              int(p.stem.split("_")[1].split("-")[1])))
print(f"{len(files)} anh")

COLS, ROWS = 3, 4
CW, CH = 528, 297
LAB = 34
try:
    font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
except Exception:
    font = ImageFont.load_default()

for si in range(0, len(files), COLS * ROWS):
    chunk = files[si:si + COLS * ROWS]
    sheet = Image.new("RGB", (COLS * CW, ROWS * (CH + LAB)), (24, 24, 28))
    d = ImageDraw.Draw(sheet)
    for i, f in enumerate(chunk):
        cx, cy = (i % COLS) * CW, (i // COLS) * (CH + LAB)
        im = Image.open(f).convert("RGB").resize((CW, CH), Image.LANCZOS)
        sheet.paste(im, (cx, cy + LAB))
        sid = f.stem.replace("shot_", "")
        d.rectangle([cx, cy, cx + CW, cy + LAB], fill=(10, 10, 12))
        d.text((cx + 8, cy + 4), sid, fill=(255, 220, 120), font=font)
        d.rectangle([cx, cy, cx + CW - 1, cy + LAB + CH - 1], outline=(70, 70, 80))
    out = OUT / f"qc_stills_{si // (COLS * ROWS) + 1}.png"
    sheet.save(out)
    print(" ", out.name, sheet.size, f"({len(chunk)} anh)")
