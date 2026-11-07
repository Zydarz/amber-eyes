#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contact sheet ảnh tĩnh Tập 08 để QC bằng mắt (H9) — 12 ảnh/tab.

Dùng:  py -3 .work/_qc_contact_stills_t08.py [vi|en|ja] [outdir]
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
LANG = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
SUF = {"vi": "_t08", "en": "_EN_t08", "ja": "_JA_t08"}[LANG]
SD = ROOT / f".work/video3{SUF}/stills"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / f".work/video3{SUF}/qc"
OUT.mkdir(parents=True, exist_ok=True)

files = sorted(SD.glob("shot_*.png"),
               key=lambda p: (int(p.stem.split("_")[1].split("-")[0]),
                              int(p.stem.split("_")[1].split("-")[1])))
print(f"{LANG}: {len(files)} anh · {SD}")

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
    out = OUT / f"qc_stills_{LANG}_{si // (COLS * ROWS) + 1:02d}.png"
    sheet.save(out)
    print(" ", out.name, sheet.size, f"({len(chunk)} anh)")
