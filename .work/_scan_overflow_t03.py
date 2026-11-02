#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H9/H5: quet anh tinh xem co CHU nao cham/tran khung hay khong.

Chu tren hinh dung mau kem (242,239,233) -> nhan dien pixel co ca 3 kenh > 205.
Vung watermark (duoi phai) va mat owl (duoi trai) duoc loai de tranh nhieu.
"""
import sys
from pathlib import Path

from PIL import Image
import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
STILLS = Path(r"D:\TEST\Gax\amber-eyes\.work\video3_t03\stills")
W, H = 1920, 1080

BANDS = [
    ("phai", slice(W - 16, W), slice(0, 960)),
    ("trai", slice(0, 16), slice(0, 900)),
    ("tren", slice(0, W), slice(0, 6)),
    ("duoi", slice(0, W), slice(H - 6, H)),
]

bad = []
files = sorted(STILLS.glob("shot_*.png"))
for p in files:
    a = np.array(Image.open(p).convert("RGB"))
    hits = []
    for name, ys, xs in BANDS:
        reg = a[ys, xs]
        m = (reg.min(axis=2) >= 205)
        if m.sum() > 12:
            hits.append(f"{name}({int(m.sum())}px)")
    if hits:
        bad.append((p.stem, ", ".join(hits)))

print(f"Quet {len(files)} anh tinh (1920x1080)")
if bad:
    print(f"\n{len(bad)} anh co pixel CHU cham khung:")
    for sid, h in bad:
        print(f"  {sid:14s} {h}")
else:
    print("\nKhong anh nao co chu cham/tran khung.")
