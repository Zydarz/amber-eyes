# -*- coding: utf-8 -*-
"""Tim chi so phan biet 'nen co noi dung canh' (AI) vs 'nen gradient thu tuc' (procedural).
Y tuong: do mat do canh (edge density) + do phan tap bien cuc bo."""
import os, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"

def metrics(path):
    im = Image.open(path).convert("L").resize((528, 297), Image.BILINEAR)
    a = np.asarray(im, dtype=np.float32)
    gx = np.abs(np.diff(a, axis=1))
    gy = np.abs(np.diff(a, axis=0))
    edge = float((gx > 12).mean() + (gy > 12).mean()) / 2
    lap = np.asarray(im.filter(ImageFilter.FIND_EDGES), dtype=np.float32)
    return edge, float(lap.std()), float(a.std())

groups = {
    "MiniMax (t2-t7)": ["t2_*.png", "t3_*.png", "t4_*.png", "t5_*.png", "t6_*.png", "t7_*.png"],
    "Procedural (t8-t29)": ["t8_*.png", "t9_*.png", "t13_*.png", "t14_*.png", "t20_*.png", "t29_*.png"],
}

print(f"{'nhom':<24} {'n':>4} {'edge%':>8} {'lapStd':>8} {'std':>8}  {'edge p5':>8} {'edge p95':>9}")
for name, pats in groups.items():
    files = []
    for p in pats:
        files += list(BG.glob(p))
    files = files[:120]
    rows = [metrics(f) for f in files]
    e = np.array([r[0] for r in rows]) * 100
    l = np.array([r[1] for r in rows])
    s = np.array([r[2] for r in rows])
    print(f"{name:<24} {len(rows):>4} {e.mean():>8.3f} {l.mean():>8.2f} {s.mean():>8.2f}"
          f"  {np.percentile(e,5):>8.3f} {np.percentile(e,95):>9.3f}")
    # nhom con lai
    if "Procedural" in name:
        proc = e
    else:
        mini = e

print()
print("=== Phan biet? ===")
try:
    print(f"  MiniMax  edge%: min={mini.min():.3f} p5={np.percentile(mini,5):.3f} median={np.median(mini):.3f}")
    print(f"  Procedur edge%: max={proc.max():.3f} p95={np.percentile(proc,95):.3f} median={np.median(proc):.3f}")
    print(f"  Nguong tach (duong chan giong nhat): {max(mini.min(), np.percentile(mini,5)):.3f}% .. {min(proc.max(), np.percentile(proc,95)):.3f}%")
    print(f"  => khoang cho phep dung nguong: {np.percentile(mini,99):.3f}% (99% MiniMax) tren; {np.percentile(proc,1):.3f}% (1% procedural) duoi")
except NameError:
    pass
