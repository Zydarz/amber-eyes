#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trich frame tu video CUOI de kiem chung bang mat: sua loi tofu + the ket + khop loi."""
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = W / "_cu" / "ja_t02_zoom"
OUT.mkdir(parents=True, exist_ok=True)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MP4 = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp4"
# (giay, nhan)
FRAMES = [
    (41.0, "shot_1-05_46sai_FIX"),
    (1784.85, "the_ket_AMBER_EYES"),
    (1258.0, "shot_4-17_quyet_dinh"),
    (654.0, "shot_3-16_2_hang"),
]
paths = []
for ts, name in FRAMES:
    p = OUT / f"vid_{name}.png"
    r = subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{ts:.3f}", "-i", str(MP4),
                        "-frames:v", "1", str(p)], capture_output=True, text=True)
    print(f"  {name:<26} t={ts:>8.2f}s rc={r.returncode} {'OK' if p.exists() else 'FAIL'}")
    if p.exists():
        paths.append(p)

# sheet 2x2
ims = []
for p in paths:
    im = Image.open(p).resize((760, 428), Image.Resampling.LANCZOS)
    ims.append(im)
if ims:
    sheet = Image.new("RGB", (760 * 2 + 30, 428 * 2 + 30), (15, 17, 23))
    for i, im in enumerate(ims):
        sheet.paste(im, (10 + (i % 2) * 770, 10 + (i // 2) * 438))
    out = OUT / "vid_verify_sheet.png"
    sheet.save(out)
    print("->", out, sheet.size)
