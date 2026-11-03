#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do toc do render: kich thuoc 6 part + uoc luong, suy ra fps va thoi gian con lai."""
import os
import time
from pathlib import Path

D = Path("D:/TEST/Gax/amber-eyes/.work/video3_EN_t03")
TOTAL_FRAMES = 49398
FPS = 30


def sizes():
    out = {}
    for p in sorted(D.glob("part_*.mp4")):
        try:
            out[p.name] = os.path.getsize(p)
        except OSError:
            out[p.name] = 0
    return out


a = sizes()
t0 = time.time()
time.sleep(90)
b = sizes()
dt = time.time() - t0

grown = sum(b.values()) - sum(a.values())
mbps = grown / dt / 1e6
print(f"cua so 90 s: +{grown/1e6:.1f} MB ({mbps:.2f} MB/s)")
for k in b:
    print(f"  {k}: {b[k]/1e6:8.1f} MB  (+{(b[k]-a.get(k,0))/1e6:6.1f})")
print(f"tong: {sum(b.values())/1e6:.1f} MB")
# 3000 kbit/s * 6 stream => 2.25 MB/s neu chay het toc do
# uoc luong video theo bitrate: 49398 frame / 30 = 1646.6 s * 0.375 MB/s = 617 MB
est_total_mb = TOTAL_FRAMES / FPS * 0.375 * 6
print(f"uoc luong mong doi ~{est_total_mb:.0f} MB")
if mbps > 0.05:
    rem = (est_total_mb - sum(b.values()) / 1e6) / mbps
    print(f"con lai ~{rem/60:.1f} phut")
