# -*- coding: utf-8 -*-
"""Chi so phan biet tot hon: 'do phu noi dung cuc bo'.
Tinh: tren o 16x16 px, tinh bien do cuc bo (max-min). O nao co bien do > nguong => co noi dung.
Gradient tron: bien do cuc bo ~0. Anh that: nhieu vung bien do cao."""
import os, sys
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"

def content_cov(path, tile=16, thr=24):
    a = np.asarray(Image.open(path).convert("L").resize((528, 297), Image.BILINEAR), dtype=np.float32)
    H, W = a.shape
    nt = 0
    for y in range(0, H - tile, tile):
        for x in range(0, W - tile, tile):
            b = a[y:y+tile, x:x+tile]
            nt += 1
            if b.max() - b.min() > thr:
                pass
    # vector hoa
    h, w = H // tile, W // tile
    t = a[:h*tile, :w*tile].reshape(h, tile, w, tile).transpose(0, 2, 1, 3).reshape(h, w, -1)
    rng = t.max(axis=2) - t.min(axis=2)
    return float((rng > thr).mean()) * 100

groups = {
    "MiniMax t2": ["t2_*.png"], "MiniMax t3": ["t3_*.png"], "MiniMax t5": ["t5_*.png"],
    "MiniMax t7": ["t7_*.png"],
    "Proc t8": ["t8_*.png"], "Proc t13": ["t13_*.png"], "Proc t20": ["t20_*.png"], "Proc t29": ["t29_*.png"],
}
res = {}
print(f"{'nhom':<14} {'n':>4} {'cover% mean':>12} {'p5':>8} {'p50':>8} {'p95':>8} {'max':>8}")
for name, pats in groups.items():
    files = []
    for p in pats:
        files += list(BG.glob(p))
    files = files[:40]
    v = np.array([content_cov(f) for f in files])
    res[name] = v
    print(f"{name:<14} {len(v):>4} {v.mean():>12.2f} {np.percentile(v,5):>8.2f} "
          f"{np.percentile(v,50):>8.2f} {np.percentile(v,95):>8.2f} {v.max():>8.2f}")

mini = np.concatenate([res[k] for k in res if k.startswith("MiniMax")])
proc = np.concatenate([res[k] for k in res if k.startswith("Proc")])
print()
print(f"  MiniMax  : min={mini.min():.2f}  p1={np.percentile(mini,1):.2f}  p5={np.percentile(mini,5):.2f}  median={np.median(mini):.2f}")
print(f"  Procedural: max={proc.max():.2f}  p95={np.percentile(proc,95):.2f}  p50={np.median(proc):.2f}")
print()
# nguong tach toi uu
cands = np.arange(0, 60, 0.5)
best = None
for th in cands:
    fp = (mini < th).mean()      # MiniMax bi quy sai (false positive)
    fn = (proc >= th).mean()      # procedural lot qua (false negative)
    if best is None or (fp + fn) < best[1]:
        best = (th, fp + fn, fp, fn)
print(f"  nguong toi uu: cover >= {best[0]:.1f}%  ->  MiniMax co 'noi dung' {100*(1-best[2]):.1f}% | procedural lot qua {100*best[3]:.1f}%")
