# -*- coding: utf-8 -*-
"""Phong to cac khung ngi nghi (trich tu mp4 thanh pham) de kiem tra chat luong hinh."""
import subprocess
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
VID = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"
OUT = WORK / "_qc_tap02_review" / "zoom"
OUT.mkdir(parents=True, exist_ok=True)

JOBS = [
    # (ten, giay, crop box (left, top, right, bottom) hoac None)
    ("cuoi_1596.80", 1596.80, None),
    ("cuoi_1597.60", 1597.60, None),
    ("cuoi_1599.00", 1599.00, None),
    ("cuoi_1601.00", 1601.00, None),
    ("cuoi_1604.00", 1604.00, None),
    ("cuoi_1605.60", 1605.60, None),
    ("s3_16_text", 728.39, (250, 560, 1500, 900)),
    ("s2_11_list", 735.86, (900, 520, 1750, 820)),
    ("s1_18_top", 181.36, (0, 0, 1920, 420)),
    ("s5_26_text", 1577.92, (500, 520, 1700, 800)),
    ("s5_28_text", 1593.84, (400, 480, 1500, 780)),
    ("s5_01_bottom", 1265.11, (300, 880, 1700, 1060)),
    ("s1_25_title", 254.74, (100, 600, 1500, 900)),
    ("s3_24_text", 835.99, (250, 500, 1400, 800)),
]

for name, t, crop in JOBS:
    raw = OUT / f"{name}.png"
    if not raw.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(VID),
                        "-frames:v", "1", str(raw)], check=True)
    im = Image.open(raw).convert("RGB")
    if crop:
        im = im.crop(crop)
        im = im.resize((im.width, im.height), Image.LANCZOS)
    outp = OUT / f"{name}_z.png"
    im.save(outp)
    print(f"{name}: t={t} size={im.size} -> {outp.name}")
print("XONG")
