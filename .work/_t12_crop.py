# -*- coding: utf-8 -*-
"""Tập 12 — crop generic: soi chữ ở độ phân giải gốc.

Dùng: py -3 .work/_t12_crop.py <file.png> <x0> <y0> <x1> <y1> <zoom> [out.png]
Tọa độ 0..1 (phần trăm theo cạnh). Nếu không chỉ định out.png ⇒ in ra .work/_t12/crops/
"""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".work" / "_t12" / "crops"
OUT.mkdir(parents=True, exist_ok=True)

a = sys.argv[1:]
if len(a) < 6:
    raise SystemExit(__doc__)
src = Path(a[0])
if not src.is_absolute():
    src = ROOT / src
x0, y0, x1, y1 = (float(v) for v in a[1:5])
k = float(a[5])
out = Path(a[6]) if len(a) > 6 else OUT / (src.stem + ".png")

im = Image.open(src)
w, h = im.size
c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
c = c.resize((int(c.width * k), int(c.height * k)), Image.Resampling.LANCZOS)
c.save(out)
print(f"{src.name} [{x0},{y0},{x1},{y1}] x{k} -> {out} {c.size}")
