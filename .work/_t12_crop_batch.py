# -*- coding: utf-8 -*-
"""QC Tập 12 — crop N vùng nghi vấn rồi gộp 1 tờ montage để soi 1 lần.

Dùng: py -3 .work/_t12_crop_batch.py --spec .work/_t12/spec_v5.json --out .work/qc_montage/old29_v5_z1.jpg --cols 2 --cell 700
Spec: [{"file": "...png", "box": [x0,y0,x1,y1], "zoom": 10, "tag": "ten vung"}, ...]
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]

ap = argparse.ArgumentParser()
ap.add_argument("--spec", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--cols", type=int, default=2)
ap.add_argument("--cell", type=int, default=700)
ap.add_argument("--gain", type=float, default=1.6)
args = ap.parse_args()

spec = json.loads((ROOT / args.spec).read_text(encoding="utf-8"))
cw, ch, pad, lab = args.cell, int(args.cell * 9 / 16), 6, 24
items = []
for s in spec:
    src = Path(s["file"])
    if not src.is_absolute():
        src = ROOT / src
    im = Image.open(src).convert("RGB")
    w, h = im.size
    x0, y0, x1, y1 = s["box"]
    c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    k = s.get("zoom", 10)
    c = c.resize((max(1, int(c.width * k)), max(1, int(c.height * k))), Image.LANCZOS)
    if args.gain != 1.0:
        c = ImageEnhance.Brightness(c).enhance(args.gain)
    # vua lai kich thuoc vao o chu nhat
    c.thumbnail((cw, ch), Image.LANCZOS)
    items.append((c, s.get("tag", src.stem)))

rows = (len(items) + args.cols - 1) // args.cols
sheet = Image.new("RGB", (args.cols * (cw + pad) + pad,
                          rows * (ch + pad + lab) + pad), (15, 15, 15))
d = ImageDraw.Draw(sheet)
for i, (c, tag) in enumerate(items):
    x = pad + (i % args.cols) * (cw + pad)
    y = pad + (i // args.cols) * (ch + pad + lab)
    sheet.paste(c, (x, y))
    d.text((x + 4, y + ch + 4), tag[:110], fill=(255, 90, 90))

out = ROOT / args.out
out.parent.mkdir(parents=True, exist_ok=True)
sheet.save(out, quality=92)
print(f"ok {out} · {sheet.size} · {len(items)} vung")
