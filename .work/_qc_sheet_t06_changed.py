#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghep contact sheet 11 shot DA DOI CAPTION de soi bang mat (A9.3)."""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
SD = Path(r"D:/TEST/Gax/amber-eyes/.work/video3_t06/stills")
OUT = Path(r"D:/TEST/Gax/amber-eyes/.work/video3_t06/_qc_changed11.png")

SHOTS = ["1-05", "1-12", "2-06", "2-08", "2-14", "2-15",
         "3-03", "3-04", "3-08", "5-01", "5-07"]
COLS, TW = 3, 620
TH = int(TW * 1080 / 1920)
PAD, LBL = 6, 22

ims = []
for s in SHOTS:
    p = SD / f"shot_{s}.png"
    im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
    ims.append((s, im))

rows = (len(ims) + COLS - 1) // COLS
W = COLS * TW + (COLS + 1) * PAD
H = rows * (TH + LBL + PAD) + PAD
sheet = Image.new("RGB", (W, H), (18, 18, 22))
from PIL import ImageDraw, ImageFont

d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 15)
except Exception:
    font = ImageFont.load_default()
for i, (s, im) in enumerate(ims):
    r, c = divmod(i, COLS)
    x = PAD + c * (TW + PAD)
    y = PAD + r * (TH + LBL + PAD)
    d.text((x + 2, y), f"shot {s}", fill=(255, 214, 90), font=font)
    sheet.paste(im, (x, y + LBL))
sheet.save(OUT)
print(f"OK  {OUT}  ({W}x{H}, {len(ims)} shot)")
