#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Debug phat hien vien tren 1 file (dung file goc trong _raw)."""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
p = Path(sys.argv[1])
im = Image.open(p).convert("L")
a = np.asarray(im, np.float32)
h, w = a.shape
print(f"{p.name}  {w}x{h}")

row_std = a.std(axis=1)
col_std = a.std(axis=0)
row_mean = a.mean(axis=1)
col_mean = a.mean(axis=0)

print("row_std[:12] =", np.round(row_std[:12], 2))
print("row_std[-12:] =", np.round(row_std[-12:], 2))
print("col_std[:12] =", np.round(col_std[:12], 2))
print("col_std[-12:] =", np.round(col_std[-12:], 2))
print("row_mean[:12] =", np.round(row_mean[:12], 1))
print("col_mean[:12] =", np.round(col_mean[:12], 1))
print("col_mean[-12:] =", np.round(col_mean[-12:], 1))


def run(seq):
    n = 0
    for v in seq:
        if v < 6.0:
            n += 1
        else:
            break
    return n


print("run top   =", run(row_std))
print("run bottom=", run(row_std[::-1]))
print("run left  =", run(col_std))
print("run right =", run(col_std[::-1]))
