"""Do nut thot cua render() trong build_video3.py (Tap06).

Muc dich: biet frame 1080p ton bao lau -> quyet dinh co nen tach build nhieu
phan hay ton optimize. Chi doc, khong ghi file thanh pham.
"""
import cProfile
import io
import pstats
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_video3 as B  # noqa: E402

FPS = B.FPS
TOTAL = B.TOTAL

# 60 frame deu trai deu qua toan bo timeline
N = 60
idxs = [int(TOTAL * FPS * (i + 0.5) / N) for i in range(N)]

# --- do tong thoi gian thuan (khong profiler) ---
t0 = time.perf_counter()
for fi in idxs:
    B.render(fi)
dt = time.perf_counter() - t0
per = dt / N
print(f"[prof] {N} frame / {dt:.2f}s -> {per * 1000:.1f} ms/frame")
print(f"[prof] 1 worker: {60 / per:.1f} frame/phut")
print(f"[prof] 6 worker (uoc luong): {6 * 60 / per:.0f} frame/phut")
print(f"[prof] 37751 frame / 6 worker: {37751 / (6 * 60 / per) / 60:.1f} phut")

# --- cProfile de tim ham nong ---
pr = cProfile.Profile()
pr.enable()
for fi in idxs[:30]:
    B.render(fi)
pr.disable()
s = io.StringIO()
pstats.Stats(pr, stream=s).sort_stats("cumulative").print_stats(28)
print(s.getvalue()[:9000])
