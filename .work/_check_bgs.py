# -*- coding: utf-8 -*-
"""Check assets/bg/ for Tap06 backgrounds."""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

BG_DIR = Path("assets/bg")
vn_plan = Path("02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md").read_text(encoding="utf-8")
import re
bgs = set()
for line in vn_plan.splitlines():
    m = re.findall(r'`(t6_[a-z0-9_]+)`', line)
    for b in m:
        bgs.add(b)

print(f"Total unique backgrounds in Tap06: {len(bgs)}")
missing = []
for b in sorted(bgs):
    p_png = BG_DIR / f"{b}.png"
    p_jpg = BG_DIR / f"{b}.jpg"
    p_webp = BG_DIR / f"{b}.webp"
    if not (p_png.exists() or p_jpg.exists() or p_webp.exists()):
        missing.append(b)
    else:
        # print existing extension
        ext = ".png" if p_png.exists() else (".jpg" if p_jpg.exists() else ".webp")
        # print(f"OK: {b}{ext}")

if missing:
    print(f"MISSING {len(missing)} backgrounds:")
    for m in missing:
        print(f"  - {m}")
else:
    print("ALL Tap06 BACKGROUNDS EXIST ON DISK!")
