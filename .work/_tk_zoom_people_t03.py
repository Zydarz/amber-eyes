# -*- coding: utf-8 -*-
"""Zoom khu vuc co nguoi trong nen doc Tap 03 - kiem tra KHONG lo mat (H1/H2)."""
import os
import sys

from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
DST = os.path.join(ROOT, "assets/bg")
OUT = os.path.join(ROOT, ".work/_tk03_zoom_people.png")

BOXES = [
    ("tk03_bar_stool_shadow", 0, 200, 1080, 1280),
    ("tk03_hitchhiker", 0, 300, 1080, 1380),
    ("tk03_interview_room", 0, 300, 1080, 1380),
    ("tk03_giant_doorway", 0, 200, 1080, 1280),
    ("tk03_two_agents", 0, 300, 1080, 1380),
    ("tk03_mother_shadow", 0, 200, 1080, 1280),
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
    with Image.open(os.path.join(DST, name + ".png")) as im:
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
