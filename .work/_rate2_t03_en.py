#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do fps thuc cu bo render + phan bo bo nho."""
import os
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path("D:/TEST/Gax/amber-eyes/.work")
D = W / "video3_EN_t03"
TOTAL_MB = 617.0
TOTAL_FRAMES = 49398


def proc_cpu():
    out = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-Process python,ffmpeg -ErrorAction SilentlyContinue | "
         "Select-Object Id,ProcessName,CPU,WorkingSet64 | ConvertTo-Json -Compress"],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    return out.stdout


def parse(js):
    import json
    try:
        d = json.loads(js)
    except Exception:
        return []
    if isinstance(d, dict):
        d = [d]
    return d


a = parse(proc_cpu())
t0 = time.time()
time.sleep(45)
b = parse(proc_cpu())
dt = time.time() - t0

amap = {r["Id"]: r for r in a}
rows = []
for r in b:
    prev = amap.get(r["Id"])
    if not prev:
        continue
    dc = float(r["CPU"]) - float(prev["CPU"])
    if dc > 0.5:
        rows.append((r["ProcessName"], r["Id"], dc / dt, r["WorkingSet64"] / 1e6))
tot_cpu = sum(x[2] for x in rows)
print(f"cua so {dt:.0f} s · {len(rows)} tien trinh dang chay · tong CPU = {tot_cpu:.2f} core")
for n, i, c, ws in sorted(rows, key=lambda x: -x[2]):
    print(f"  {n:8} pid={i:<6} {c:5.2f} core  {ws:7.0f} MB")
print(f"RAM dung boi render: {sum(x[3] for x in rows):.0f} MB")
print(f"core logic may: 12")

# size -> frames
tot = sum(os.path.getsize(p) for p in D.glob("part_*.mp4"))
print(f"part total {tot/1e6:.1f} MB / ~{TOTAL_MB:.0f} MB = {100*tot/1e6/TOTAL_MB:.1f}%")
