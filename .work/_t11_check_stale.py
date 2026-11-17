# -*- coding: utf-8 -*-
"""Kiểm tra ảnh nền Tập 11 theo ngày sinh: file cũ (Real-ESRGAN 13/11) còn sót?"""
import json
from datetime import date, datetime
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
BG = ROOT / "assets" / "bg"
jobs = {j["name"]: j for j in json.loads((ROOT / ".work/bg_jobs_tap11_v3.json").read_text(encoding="utf-8"))}

rows = []
for n in jobs:
    p = BG / f"{n}.png"
    if not p.exists():
        continue
    mt = datetime.fromtimestamp(p.stat().st_mtime)
    rows.append((n, mt.strftime("%Y-%m-%d"), p.stat().st_size))

from collections import Counter
print("theo ngày:", Counter(r[1] for r in rows))
print("\n--- file KHÔNG phải 16/11 (2026) ---")
stale = [r for r in rows if r[1] != "2026-11-16"]
for n, d, s in sorted(stale, key=lambda x: x[1]):
    print(f"  {d}  {n}  ({s/1e6:.1f} MB)")
print(f"\ntổng file cũ (cần sinh lại nếu là ảnh Real-ESRGAN): {len(stale)}")
