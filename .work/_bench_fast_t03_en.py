#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem nhan finishing() toi uu BIT-IDENTICAL cho EN Tap03 (A11 #102) — ban nhe, 20 frame that
+ 20 mang ngau nhien, de chay nhanh. Chan ghi neu khong giong byte."""
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("AE_EP", "03")
os.environ.setdefault("AE_LANG", "en")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402

import build_video3 as B  # noqa: E402

ORIG = B.finishing
_V3 = {"v": None}


def make_fast_finishing():
    def fast(arr, fi):
        if _V3["v"] is None:
            ORIG(arr, fi)                       # khoi tao VIGNETTE/GRAIN/ABUF trong ban goc
            _V3["v"] = np.repeat(B.VIGNETTE, 3, axis=2).copy()
        a = arr.astype(np.float32)
        np.multiply(a, _V3["v"], out=a)
        np.add(a, B.GRAIN[fi % 6], out=a)
        red = a[:, :, 0].copy()
        a[:, 1:, 0] = red[:, :-1]
        np.clip(a, 0, 255, out=a)
        return a.astype(np.uint8)
    return fast


fast = make_fast_finishing()
N = 20
idxs = sorted({int(B.TOTAL * B.FPS * (i + 0.5) / N) for i in range(N)})

bad = 0
maxdiff = 0
for fi in idxs:
    arr = np.random.randint(0, 256, (B.H, B.W, 3), dtype=np.uint8)
    a, b = ORIG(arr, fi), fast(arr, fi)
    if not np.array_equal(a, b):
        bad += 1
        maxdiff = max(maxdiff, int(np.abs(a.astype(np.int16) - b.astype(np.int16)).max()))
    arr2 = np.asarray(B.render(fi).convert("RGB"))
    a2, b2 = ORIG(arr2, fi), fast(arr2, fi)
    if not np.array_equal(a2, b2):
        bad += 1
        maxdiff = max(maxdiff, int(np.abs(a2.astype(np.int16) - b2.astype(np.int16)).max()))
print(f"[check] checked={len(idxs) * 2} mismatches={bad} maxdiff={maxdiff}")
if bad:
    raise SystemExit("CHAN - finishing toi uu KHONG bit-identical")
print("[check] OK BIT-IDENTICAL")

arr = np.asarray(B.render(idxs[0]).convert("RGB"))
for name, fn in (("goc", ORIG), ("fast", fast)):
    fn(arr, 0)
    t = time.perf_counter()
    for k in range(20):
        fn(arr, k)
    print(f"[perf] finishing {name:5}: {(time.perf_counter() - t) / 20 * 1000:.1f} ms/frame")
