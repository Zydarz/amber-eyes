# -*- coding: utf-8 -*-
"""Contact sheet 28 anh nen 16:9 GOC cua Tap 03 (de soi phong cach truoc khi sinh 9:16)."""
import os
import sys

from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_src_t03 import PAIRS, src_path  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
OUT = os.path.join(ROOT, ".work/_tk03_src_montage.png")

COLS = 7
TW, TH = 360, 203          # 16:9 thumb
PAD, LAB = 8, 16

rows = (len(PAIRS) + COLS - 1) // COLS
W = COLS * (TW + PAD) + PAD
H = rows * (TH + PAD + LAB) + PAD
sheet = Image.new("RGB", (W, H), (14, 14, 16))
d = ImageDraw.Draw(sheet)

for i, (name, ref) in enumerate(PAIRS):
    r, c = divmod(i, COLS)
    x = PAD + c * (TW + PAD)
    y = PAD + r * (TH + PAD + LAB)
    with Image.open(src_path(ref)) as im:
        th = im.convert("RGB").resize((TW, TH), Image.Resampling.LANCZOS)
    sheet.paste(th, (x, y))
    d.text((x + 2, y + TH + 2), name[5:][:26], fill=(210, 210, 210))

sheet.save(OUT, "PNG", optimize=True)
print("contact sheet: %s (%d anh, %dx%d, %.2f MB)" % (OUT, len(PAIRS), W, H, os.path.getsize(OUT) / 1048576))
