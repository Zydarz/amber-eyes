# -*- coding: utf-8 -*-
"""Tập 12 — QC kích thước + đủ file cho 152 nền theo H25."""
import json
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
JOBS = ROOT / ".work/bg_jobs_tap12_v2.json"

jobs = json.loads(JOBS.read_text(encoding="utf-8"))
missing, bad, ok = [], [], 0
for j in jobs:
    f = BG / f"{j['name']}.png"
    if not f.exists():
        missing.append(j["name"])
        continue
    with Image.open(f) as im:
        if im.size != (2112, 1188):
            bad.append((j["name"], im.size))
        else:
            ok += 1
extra = sorted(p.stem for p in BG.glob("t12_*.png") if p.stem not in {j["name"] for j in jobs})

print(f"job trong bg_jobs_tap12_v2.json : {len(jobs)}")
print(f"đúng kích thước 2112x1188       : {ok}")
print(f"thiếu file                      : {len(missing)} {missing[:8]}")
print(f"sai kích thước                  : {len(bad)} {bad[:8]}")
print(f"file t12_* thừa (không có job)  : {len(extra)} {extra[:8]}")

# đếm tổng số file nền T12 trên đĩa
allfiles = sorted(p.name for p in BG.glob("t12_*.png"))
print(f"\ntổng file assets/bg/t12_*.png trên đĩa: {len(allfiles)}")
sys.exit(1 if (missing or bad or extra) else 0)
