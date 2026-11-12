# -*- coding: utf-8 -*-
"""Do tong thoi gian 1 anh tinh: render(fi) + luu PNG. Tach thanh tung thanh phan."""
import os, sys, time, io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))
os.environ["AE_EP"] = "08"

import importlib
b = importlib.import_module("build_video3")

by_id = {s["id"]: s for s in b.SH}
IDS = ["1-02", "1-11", "2-05", "3-09", "4-14", "5-20", "5-41"]

print(f"{'shot':<7} {'render ms':>10} {'savePNG ms':>12} {'size MB':>8}")
tot_r = tot_s = 0
for sid in IDS:
    s = by_id.get(sid)
    if not s:
        continue
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)

    t0 = time.perf_counter()
    fr = b.render(fi)
    dt_r = (time.perf_counter() - t0) * 1000

    rgb = fr.convert("RGB")
    t0 = time.perf_counter()
    rgb.save(io.BytesIO(), format="PNG")
    dt_s = (time.perf_counter() - t0) * 1000
    mb = len(rgb.tobytes()) / 1e6

    tot_r += dt_r
    tot_s += dt_s
    print(f"{sid:<7} {dt_r:>10.0f} {dt_s:>12.0f} {mb:>8.2f}")

n = len(IDS)
print()
print(f"TB: render {tot_r/n:.0f} ms/shot + luu PNG {tot_s/n:.0f} ms/shot = {(tot_r+tot_s)/n:.0f} ms/anh")
print(f"   x223 shot x3 ngon ngu = {(tot_r+tot_s)/n*223*3/1000/60:.1f} phut")
print(f"   dung rieng phan luu PNG = {tot_s/n*223*3/1000/60:.1f} phut")
print(f"   dung rieng phan render = {tot_r/n*223*3/1000/60:.1f} phut")
