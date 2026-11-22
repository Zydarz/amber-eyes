# -*- coding: utf-8 -*-
"""Contact sheet 26 anh nen doc 9:16 Tap 02 (de xem nhanh)."""
import glob
import os

from PIL import Image, ImageDraw

ROOT = r"D:/TEST/Gax/amber-eyes"
OUT = os.path.join(ROOT, ".work/_tk02_montage_v2.png")
files = sorted(glob.glob(os.path.join(ROOT, "assets/bg/tk02_*.png")))
COLS, ROWS = 7, 4
TW, TH = 216, 384          # thumb 1080x1920 x 0.2
PAD, LAB = 8, 18

W = COLS * (TW + PAD) + PAD
H = ROWS * (TH + PAD + LAB) + PAD
sheet = Image.new("RGB", (W, H), (14, 14, 16))
d = ImageDraw.Draw(sheet)

for i, p in enumerate(files):
    r, c = divmod(i, COLS)
    x = PAD + c * (TW + PAD)
    y = PAD + r * (TH + PAD + LAB)
    with Image.open(p) as im:
        th = im.convert("RGB").resize((TW, TH), Image.Resampling.LANCZOS)
    sheet.paste(th, (x, y))
    name = os.path.basename(p)[len("tk02_"):-len(".png")]
    d.text((x + 2, y + TH + 3), name[:22], fill=(205, 205, 205))

sheet.save(OUT, "PNG", optimize=True)
print("contact sheet: %s (%d anh, %dx%d, %.1f MB)" % (OUT, len(files), W, H, os.path.getsize(OUT) / 1048576))
