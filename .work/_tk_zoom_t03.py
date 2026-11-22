# -*- coding: utf-8 -*-
"""Zoom 1:1 cac vung ngo nhi trong nen doc Tap 03 (H2: chu la, mat lo, watermark)."""
import os
import sys

from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
DST = os.path.join(ROOT, "assets/bg")
OUT = os.path.join(ROOT, ".work/_tk03_zoom.png")

# (ten anh, x0, y0, x1, y1) theo toa do 1080x1920
BOXES = [
    ("tk03_two_agents", 520, 780, 780, 1080),
    ("tk03_vacaville_1978", 480, 820, 860, 1120),
    ("tk03_red_flags", 60, 980, 700, 1360),
    ("tk03_organized_split", 120, 1000, 820, 1420),
    ("tk03_case_photos", 120, 300, 960, 900),
    ("tk03_cassette", 400, 700, 1080, 1200),
]

CELL = 420
PAD, LAB = 10, 18
cols = 3
rows = (len(BOXES) + cols - 1) // cols
W = cols * (CELL + PAD) + PAD
H = rows * (CELL + PAD + LAB) + PAD
sheet = Image.new("RGB", (W, H), (12, 12, 14))
d = ImageDraw.Draw(sheet)

for i, (name, x0, y0, x1, y1) in enumerate(BOXES):
    p = os.path.join(DST, name + ".png")
    with Image.open(p) as im:
        crop = im.convert("RGB").crop((x0, y0, x1, y1))
        crop = crop.resize((CELL, int(CELL * crop.size[1] / crop.size[0])),
                           Image.Resampling.LANCZOS)
    r, c = divmod(i, cols)
    x = PAD + c * (CELL + PAD)
    y = PAD + r * (CELL + PAD + LAB)
    sheet.paste(crop, (x, y))
    d.text((x + 2, y + CELL + 3), name[5:], fill=(210, 210, 210))

sheet.save(OUT, "PNG", optimize=True)
print("zoom sheet: %s (%dx%d)" % (OUT, W, H))
