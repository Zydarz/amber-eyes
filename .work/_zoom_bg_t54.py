# -*- coding: utf-8 -*-
"""Crop vung nhi nghi de soi mat (H2: phong to vung nhi nghi).

usage: py -3 .work/_zoom_bg_t54.py <ten nen> <x0> <y0> <x1> <y1> [out]
"""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

name = sys.argv[1]
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
out = sys.argv[6] if len(sys.argv) > 6 else str(HERE / ("_zoom_%s.png" % name))
src = ROOT / "assets" / "bg" / ("%s.png" % name)
im = Image.open(src).convert("RGB")
crop = im.crop((x0, y0, x1, y1)).resize(((x1 - x0) * 3, (y1 - y0) * 3), Image.LANCZOS)
crop.save(out)
print("%s  crop (%d,%d)-(%d,%d)  -> %s  %dx%d" % (name, x0, y0, x1, y1, out, crop.size[0], crop.size[1]))
