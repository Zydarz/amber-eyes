#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh tờ soi mắt (QC sheet) cho ảnh nền tập 37/38/39: 4 cột x 8 ô, nhãn tên rõ.

Dùng: py -3 _sheets_3739.py 37 [outdir]
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "qc_montage"

ep = sys.argv[1]
CW, PAD, LAB = 512, 6, 30
CH = int(CW * 9 / 16)
ROW = CH + LAB + PAD
COLS, PER = 4, 32

files = sorted(BG.glob(f"t{ep}_*.png"))
try:
    f = ImageFont.truetype("arial.ttf", 22)
except Exception:
    f = ImageFont.load_default()

OUT.mkdir(parents=True, exist_ok=True)
for part in range(0, len(files), PER):
    chunk = files[part:part + PER]
    rows = (len(chunk) + COLS - 1) // COLS
    sheet = Image.new("RGB", (COLS * (CW + PAD), rows * ROW), (10, 10, 12))
    dr = ImageDraw.Draw(sheet)
    for i, p in enumerate(chunk):
        c, r = i % COLS, i // COLS
        im = Image.open(p).convert("RGB").resize((CW, CH), Image.LANCZOS)
        x, y = c * (CW + PAD), r * ROW
        sheet.paste(im, (x, y))
        dr.text((x + 4, y + CH + 4), p.stem.replace(f"t{ep}_", ""), font=f, fill=(240, 240, 245))
    out = OUT / f"sheet_t{ep}_{part // PER:02d}.jpg"
    sheet.save(out, quality=88)
    print(f"ok {out.name} {sheet.size} {len(chunk)} anh")
