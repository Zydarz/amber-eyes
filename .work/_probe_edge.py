#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In profile canh 0..40 cua 1 anh de xac dinh vi tri duong net khung ve."""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
name = sys.argv[1]
a = np.asarray(Image.open(Path(r"D:\TEST\Gax\Audi\assets\bg") / f"{name}.png").convert("L"), np.float32)
h, w = a.shape
rows, cols = a.mean(axis=1), a.mean(axis=0)
print(f"=== {name} {w}x{h} ===")
print("hang  0..40 :", " ".join(f"{i}:{rows[i]:.0f}" for i in range(0, 41)))
print("hang -40..0 :", " ".join(f"{h-1-i}:{rows[h-1-i]:.0f}" for i in range(0, 41)))
print("cot   0..40 :", " ".join(f"{i}:{cols[i]:.0f}" for i in range(0, 41)))
print("cot  -40..0 :", " ".join(f"{w-1-i}:{cols[w-1-i]:.0f}" for i in range(0, 41)))
