# -*- coding: utf-8 -*-
"""Montage nen doc TikTok Tap 07 de user soi (4 cot x 4 hang, o 512 px)."""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t07 import PAIRS  # noqa: E402

ROOT = HERE.parent
DST = ROOT / "assets" / "bg"
OUT = HERE / "qc_montage_t07"
OUT.mkdir(exist_ok=True)

COLS, ROWS = 4, 4
CELL = 512
PAD = 10
LBL = 26

names = [n for n, _ in PAIRS]
have = [(n, DST / (n + ".png")) for n in names if (DST / (n + ".png")).exists()]
missing = [n for n in names if not (DST / (n + ".png")).exists()]

W = COLS * CELL + (COLS + 1) * PAD
H = ROWS * (CELL + LBL) + (ROWS + 1) * PAD
sheet = Image.new("RGB", (W, H), (18, 18, 20))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("arial.ttf", 15)
except Exception:
    font = ImageFont.load_default()

for i, (n, p) in enumerate(have):
    r, c = divmod(i, COLS)
    x = PAD + c * (CELL + PAD)
    y = PAD + r * (CELL + LBL + PAD)
    with Image.open(p) as im:
        im = im.convert("RGB").resize((CELL, CELL), Image.Resampling.LANCZOS)
    sheet.paste(im, (x, y))
    d.text((x + 2, y + CELL + 4), n.replace("tk07_", "")[:38], fill=(210, 210, 210), font=font)

out = OUT / "montage_tk07.jpg"
sheet.save(out, quality=92)
print("co file:", len(have), "· thieu:", len(missing))
print("montage:", out, sheet.size)
for m in missing:
    print("  THIEU:", m)
