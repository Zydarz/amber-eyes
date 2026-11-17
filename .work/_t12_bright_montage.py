# -*- coding: utf-8 -*-
"""QC Tập 12 — dựng tờ montage KÈM tăng sáng, để soi chữ trong ảnh noir quá tối.

Dùng: py -3 .work/_t12_bright_montage.py --dir .work/_t12/old29v5 --out .work/qc_montage/old29_v5_b.jpg --cols 2 --cell 1000 --gain 2.0
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]

ap = argparse.ArgumentParser()
ap.add_argument("--dir", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--cols", type=int, default=2)
ap.add_argument("--cell", type=int, default=1000)
ap.add_argument("--gain", type=float, default=2.0)
ap.add_argument("--sheet", type=int, default=0, help="0 = tat ca")
args = ap.parse_args()

src = ROOT / args.dir
files = sorted(p for p in src.glob("*.png"))
if args.sheet:
    per = args.cols * 4
    files = files[args.sheet * per:(args.sheet + 1) * per]
if not files:
    print("!! khong co anh")
    sys.exit(1)

cw, ch, pad, lab = args.cell, int(args.cell * 9 / 16), 6, 26
rows = (len(files) + args.cols - 1) // args.cols
sheet = Image.new("RGB", (args.cols * (cw + pad) + pad,
                           rows * (ch + pad + lab) + pad), (18, 18, 18))
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB").resize((cw, ch), Image.LANCZOS)
    if args.gain != 1.0:
        im = ImageEnhance.Brightness(im).enhance(args.gain)
        im = ImageEnhance.Contrast(im).enhance(1.15)
    x = pad + (i % args.cols) * (cw + pad)
    y = pad + (i // args.cols) * (ch + pad + lab)
    sheet.paste(im, (x, y))
    d.text((x + 4, y + ch + 4), f.stem, fill=(255, 90, 90))

out = ROOT / args.out
out.parent.mkdir(parents=True, exist_ok=True)
sheet.save(out, quality=92)
print(f"ok {out} · {sheet.size} · {len(files)} anh · gain={args.gain}")
