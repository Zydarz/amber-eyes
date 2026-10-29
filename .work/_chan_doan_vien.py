#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chan doan vien: in profile do sang theo hang/cot de phan biet
  - viet den that (bar): do sang nhe hang, bang phang, dung ngay
  - troi toi / vien vignette: do sang tang dan
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
BG = Path(r"D:\TEST\Gax\Audi\assets\bg")

for name in sys.argv[1:]:
    im = Image.open(BG / f"{name}.png").convert("L")
    a = np.asarray(im, np.float32)
    h, w = a.shape
    print(f"\n=== {name}  ({w}x{h}) ===")
    print("  hang (tu tren): ", end="")
    for y in [0, 5, 20, 40, 60, 80, 90, 100, 110, 120, 140]:
        if y < h:
            print(f"y{y}={a[y].mean():.1f}(sd{a[y].std():.1f}) ", end="")
    print()
    print("  hang (tu duoi): ", end="")
    for y in [h - 1, h - 6, h - 20, h - 40, h - 60, h - 80, h - 90, h - 100, h - 110, h - 120]:
        if y >= 0:
            print(f"y{y}={a[y].mean():.1f}(sd{a[y].std():.1f}) ", end="")
    print()
    print("  cot  (tu trai): ", end="")
    for x in [0, 5, 20, 40, 60, 80, 90, 100, 110, 120]:
        if x < w:
            print(f"x{x}={a[:, x].mean():.1f}(sd{a[:, x].std():.1f}) ", end="")
    print()
    print("  cot  (tu phai): ", end="")
    for x in [w - 1, w - 6, w - 20, w - 40, w - 60, w - 80, w - 90, w - 100, w - 110, w - 120]:
        if x >= 0:
            print(f"x{x}={a[:, x].mean():.1f}(sd{a[:, x].std():.1f}) ", end="")
    print()
