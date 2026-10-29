#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghép contact sheet từ ảnh tĩnh có sẵn (dùng để soi nhanh, không cần mp4)."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else r"D:\TEST\Gax\Audi\.work\video3_t02\stills")
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else r"D:\TEST\Gax\Audi\.work\qc_tap02\preview")
COLS, ROWS = 4, 4
TW, TH = 480, 270
PER = COLS * ROWS

files = sorted(p for p in SRC.glob("*.png"))
OUT.mkdir(parents=True, exist_ok=True)
try:
    f = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 22)
except OSError:
    f = ImageFont.load_default()

sheets = (len(files) + PER - 1) // PER
for k in range(sheets):
    chunk = files[k * PER:(k + 1) * PER]
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 30)), (14, 14, 17))
    d = ImageDraw.Draw(sheet)
    for i, p in enumerate(chunk):
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x, y = (i % COLS) * TW, (i // COLS) * (TH + 30)
        sheet.paste(im, (x, y))
        d.text((x + 8, y + TH + 4), p.stem, font=f, fill=(242, 239, 233))
    sheet.save(OUT / f"preview_{k + 1:02d}.png")
print(f"{len(files)} anh -> {sheets} to -> {OUT}")
