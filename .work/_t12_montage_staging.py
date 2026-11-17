# -*- coding: utf-8 -*-
"""Tập 12 — dựng montage từ THƯ MỤC STAGING (không đụng assets/bg).

Dùng: py -3 .work/_t12_montage_staging.py --dir .work/_t12/old29 --list .work/_t12/sheets_old29/list_g01.json --out .work/qc_montage/old29_g01 [--cols 4 --cell 512]
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]

ap = argparse.ArgumentParser()
ap.add_argument("--dir", required=True)
ap.add_argument("--list", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--cols", type=int, default=4)
ap.add_argument("--cell", type=int, default=512)
a = ap.parse_args()

src = Path(a.dir)
if not src.is_absolute():
    src = ROOT / src
names = json.loads((ROOT / a.list).read_text(encoding="utf-8"))["must"]
try:
    font = ImageFont.truetype("arial.ttf", 26)
except Exception:
    font = ImageFont.load_default()

cell, cols = a.cell, a.cols
rows = (len(names) + cols - 1) // cols
label_h = 34
W, H = cols * cell, rows * (cell + label_h)
sheet = Image.new("RGB", (W, H), (10, 10, 12))
d = ImageDraw.Draw(sheet)

for i, n in enumerate(names):
    f = src / f"t12_{n}.png"
    if not f.exists():
        d.text(((i % cols) * cell + 6, (i // cols) * (cell + label_h) + 6),
               f"THIEU {n}", fill=(255, 80, 80), font=font)
        continue
    im = Image.open(f).convert("RGB").resize((cell, cell), Image.Resampling.LANCZOS)
    x, y = (i % cols) * cell, (i // cols) * (cell + label_h)
    sheet.paste(im, (x, y))
    d.rectangle([x, y + cell, x + cell, y + cell + label_h], fill=(10, 10, 12))
    d.text((x + 4, y + cell + 3), n, fill=(235, 235, 235), font=font)

out = ROOT / a.out if not Path(a.out).is_absolute() else Path(a.out)
out.parent.mkdir(parents=True, exist_ok=True)
sheet.save(out, quality=90)
print(f"ok {out} · ({W}, {H}) · {len(names)} anh · {rows} hang x {cols} cot")
