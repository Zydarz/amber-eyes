#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repair the AI backgrounds the user supplied (review 22/10).

  bg_h2_empty_wheelchair : erase the legible "FEEDING TUBE" labels (inpaint)
  bg_h3_profiling_desk   : crop the 2% black bar at the bottom, keep 16:9
Output: assets/bg/<code>.png at 2112x1188 (plan 5.4 / 5.6 working size)
"""
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

ROOT = Path(r"D:\TEST\Gax\Audi")
SRC = ROOT / "assets" / "photos" / "noir" / "_4k"
OUT = ROOT / "assets" / "bg"
SIZE = (2112, 1188)

# label boxes on the 5504x3072 source (x0, y0, x1, y1)
H2_LABELS = [(4268, 2223, 4493, 2364), (4483, 2195, 4755, 2392), (4857, 2270, 5147, 2457)]


def to_169(im):
    w, h = im.size
    if w / h > 16 / 9:
        nw = int(h * 16 / 9)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w * 9 / 16)
        im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    return im.resize(SIZE, Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    # --- h2: inpaint label text
    im = cv2.imread(str(SRC / "bg_h2_empty_wheelchair_4k.jpg"))
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(gray)
    for x0, y0, x1, y1 in H2_LABELS:
        roi = gray[y0:y1, x0:x1]
        m = (roi < 120).astype(np.uint8) * 255
        mask[y0:y1, x0:x1] = cv2.dilate(m, np.ones((7, 7), np.uint8))
    fixed = cv2.inpaint(im, mask, 9, cv2.INPAINT_TELEA)
    for x0, y0, x1, y1 in H2_LABELS:              # soften what is left
        fixed[y0:y1, x0:x1] = cv2.GaussianBlur(fixed[y0:y1, x0:x1], (0, 0), 2.5)
    cv2.imwrite(str(SRC.parent / "bg_h2_empty_wheelchair_fixed_4k.jpg"), fixed, [cv2.IMWRITE_JPEG_QUALITY, 95])
    to_169(Image.fromarray(cv2.cvtColor(fixed, cv2.COLOR_BGR2RGB))).save(OUT / "wheelchair_room.png")

    # --- h3: drop bottom black bar
    im3 = Image.open(SRC / "bg_h3_profiling_desk_4k.jpg").convert("RGB")
    a = np.asarray(im3.convert("L"), np.float32).mean(axis=1)
    bot = next(i for i, v in enumerate(a[::-1]) if v > 12)
    im3 = im3.crop((0, 0, im3.width, im3.height - bot - 4))
    to_169(im3).save(OUT / "brain_desk.png")

    # --- h4, h5: already clean, just resize
    to_169(Image.open(SRC / "bg_h4_locked_door_4k.jpg").convert("RGB")).save(OUT / "locked_door.png")
    to_169(Image.open(SRC / "bg_h5_courtroom_dawn_4k.jpg").convert("RGB")).save(OUT / "court_dawn.png")
    print("done", sorted(p.name for p in OUT.iterdir()))


if __name__ == "__main__":
    main()
