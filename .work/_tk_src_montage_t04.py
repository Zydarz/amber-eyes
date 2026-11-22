# -*- coding: utf-8 -*-
"""Contact sheet 23 anh nen 16:9 goc cua Tap 04 — soi mat phong cach truoc khi sinh doc."""
import os
import sys

from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _tk_src_t04 import PAIRS, RAW  # noqa: E402

OUT = os.path.join(HERE, "_tk04_src_sheet.png")

COLS = 6
TW, TH = 380, 214          # 16:9
PAD, LAB = 10, 20
rows = (len(PAIRS) + COLS - 1) // COLS
W = COLS * (TW + PAD) + PAD
H = rows * (TH + PAD + LAB) + PAD
sheet = Image.new("RGB", (W, H), (14, 14, 16))
d = ImageDraw.Draw(sheet)

for i, (name, ref) in enumerate(PAIRS):
    p = os.path.join(RAW, ref)
    if not os.path.exists(p):
        print("  THIEU", ref)
        continue
    with Image.open(p) as im:
        im = im.convert("RGB").resize((TW, TH), Image.Resampling.LANCZOS)
    r, c = divmod(i, COLS)
    x = PAD + c * (TW + PAD)
    y = PAD + r * (TH + PAD + LAB)
    sheet.paste(im, (x, y))
    d.text((x + 2, y + TH + 4), "%s <- %s" % (name[5:], ref), fill=(210, 210, 210))

sheet.save(OUT, "PNG", optimize=True)
print("contact sheet nguon: %s (%d anh, %dx%d)" % (OUT, len(PAIRS), W, H))
