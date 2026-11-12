# -*- coding: utf-8 -*-
"""Tim chi so tu dong phan biet 'nen co noi dung canh' vs 'nen gradient thu tuc'.
Ung vien: entropy luminance, occupied range, so 'sac xam' (bang mau pha).
Cho phep rule co cong 'DO' chu khong chi 'soi bang mat'."""
import os, sys
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"

def feat(path):
    im = Image.open(path).convert("RGB").resize((528, 297), Image.BILINEAR)
    a = np.asarray(im, dtype=np.float32)
    L = 0.299*a[:,:,0] + 0.587*a[:,:,1] + 0.114*a[:,:,2]
    h = np.histogram(L, bins=64, range=(0,255))[0].astype(np.float64)
    p = h / h.sum()
    ent = float(-(p[p>0] * np.log2(p[p>0])).sum())
    # sắc xám: số bậc xám khác nhau đang dùng
    used = int((p > 0.002).sum())
    # dải sáng chiếm
    rng = float(np.percentile(L, 99) - np.percentile(L, 1))
    # tương phản cục bộ trung bình (độ "có hình")
    gx = np.abs(np.diff(L, axis=1)).mean()
    gy = np.abs(np.diff(L, axis=0)).mean()
    return ent, used, rng, float(gx+gy)

groups = {
    "MiniMax t2": ["t2_*.png"], "MiniMax t3": ["t3_*.png"], "MiniMax t5": ["t5_*.png"],
    "MiniMax t6": ["t6_*.png"], "MiniMax t7": ["t7_*.png"],
    "Proc t8": ["t8_*.png"], "Proc t9": ["t9_*.png"], "Proc t13": ["t13_*.png"],
    "Proc t14": ["t14_*.png"], "Proc t20": ["t20_*.png"], "Proc t29": ["t29_*.png"],
}
print(f"{'nhom':<13} {'n':>4} {'entropy':>9} {'sacXam':>8} {'daiSang':>9} {'grad':>8}")
store = {}
for name, pats in groups.items():
    files = []
    for p in pats: files += list(BG.glob(p))
    files = files[:35]
    v = np.array([feat(f) for f in files])
    store[name] = v
    print(f"{name:<13} {len(v):>4} {v[:,0].mean():>9.3f} {v[:,1].mean():>8.1f} "
          f"{v[:,2].mean():>9.1f} {v[:,3].mean():>8.2f}")

mini = np.concatenate([v for k, v in store.items() if k.startswith("MiniMax")])
proc = np.concatenate([v for k, v in store.items() if k.startswith("Proc")])
print()
for i, nm in enumerate(["entropy", "sacXam", "daiSang", "grad"]):
    m, p_ = mini[:, i], proc[:, i]
    # nguong tach toi uu tren tung chi so
    best = None
    for th in np.unique(np.concatenate([m, p_])):
        fp = (m < th).mean(); fn = (p_ >= th).mean()
        if best is None or fp + fn < best[1]: best = (th, fp+fn, fp, fn)
    print(f"  {nm:<9} MiniMax median={np.median(m):7.2f} p5={np.percentile(m,5):7.2f} | "
          f"Proc median={np.median(p_):7.2f} p95={np.percentile(p_,95):7.2f} | "
          f"nguong toi uu {best[0]:7.2f} -> MiniMax pass {100*(1-best[2]):5.1f}% | Proc lot qua {100*best[3]:5.1f}%")
