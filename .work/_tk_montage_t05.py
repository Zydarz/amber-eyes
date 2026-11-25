# -*- coding: utf-8 -*-
"""Contact sheet 34 nen doc Tap 05 de nhanh soi (khong phai bao cao QC)."""
import pathlib
import sys

from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t05 import PAIRS  # noqa: E402

DST = HERE.parent / "assets" / "bg"
OUT = HERE / "_tk05_montage.png"

CELL_W, CELL_H = 260, 462
COLS = 7
PAD = 10
LABEL_H = 26

items = list(PAIRS)
rows = (len(items) + COLS - 1) // COLS
W = COLS * (CELL_W + PAD) + PAD
H = rows * (CELL_H + LABEL_H + PAD) + PAD

sheet = Image.new("RGB", (W, H), (16, 16, 18))
dr = ImageDraw.Draw(sheet)

for i, (name, ref) in enumerate(items):
    p = DST / (name + ".png")
    if not p.exists():
        continue
    r, c = divmod(i, COLS)
    x = PAD + c * (CELL_W + PAD)
    y = PAD + r * (CELL_H + LABEL_H + PAD)
    with Image.open(p) as im:
        im = im.convert("RGB").resize((CELL_W, CELL_H), Image.Resampling.LANCZOS)
        sheet.paste(im, (x, y))
    dr.text((x + 3, y + CELL_H + 6), name.replace("tk05_", ""), fill=(210, 210, 215))

sheet.save(OUT, "PNG")
print("contact sheet:", OUT, sheet.size, "%.1f MB" % (OUT.stat().st_size / 1048576))
