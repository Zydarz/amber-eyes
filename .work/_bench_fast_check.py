"""Kiem chung + do toc finishing() toi uu so voi ban goc (Tap06)."""
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402

import build_video3 as B  # noqa: E402
from _bench_render_t06 import make_fast_finishing  # noqa: E402

ORIG = B.finishing
fast = make_fast_finishing()

idxs = sorted({int(B.TOTAL * B.FPS * (i + 0.5) / 120) for i in range(120)})

# ---- 1. BIT-IDENTICAL: du random + du frame that ----
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
print(f"[check] checked={len(idxs) * 2} mismatches={bad} maxdiff={maxdiff}")
if bad:
    raise SystemExit("CHẶN - finishing toi uu KHONG bit-identical")
print("[check] OK  BIT-IDENTICAL")

# ---- 2. TOC DO (chi finishing, tren array that) ----
arr = np.asarray(B.render(idxs[0]).convert("RGB"))
for name, fn in (("goc", ORIG), ("fast", fast)):
    fn(arr, 0)
    t = time.perf_counter()
    for k in range(25):
        fn(arr, k)
    dt = (time.perf_counter() - t) / 25
    print(f"[perf] finishing {name:5}: {dt * 1000:.1f} ms/frame")
