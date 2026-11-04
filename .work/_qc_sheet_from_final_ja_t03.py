#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trích khung từ chính file THÀNH PHẨM Tap03_JA_master.mp4 → contact sheet để soi mắt.

H9 áp dụng cho video thật: xác nhận hình trong mp4 đúng nền / đúng chữ tiếng Nhật /
badge đúng vai / không tràn chữ / không lộ mặt.
"""
import io
import subprocess
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MP4 = ROOT / "02_SAN_XUAT" / "Tap03_JA" / "xuat_ban" / "Tap03_JA_master.mp4"
OUT = W / "_qc_sheets_ja_t03"
OUT.mkdir(parents=True, exist_ok=True)

PICKS = [
    ("t=12s · intro", 12.0),
    ("t=30s · 1-01", 30.0),
    ("t=420s · hồi 1", 420.0),
    ("t=900s · hồi 2", 900.0),
    ("t=1250s · hồi 3", 1250.0),
    ("t=1600s · hồi 4", 1600.0),
    ("t=1780s · hồi 5", 1780.0),
    ("t=1921s · thẻ kết", 1920.9),
]

tiles = []
for label, t in PICKS:
    fr = subprocess.run([str(FF), "-v", "error", "-ss", f"{t:.3f}", "-i", str(MP4),
                         "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                        capture_output=True).stdout
    if not fr:
        print("KHONG lay duoc khung", label)
        continue
    im = Image.open(io.BytesIO(fr)).convert("RGB").resize((640, 360), Image.LANCZOS)
    tiles.append((label, im))
    print(f"  {label:22s} -> ok")

cols, tw, th = 2, 640, 360
rows = (len(tiles) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * th), (12, 12, 16))
for i, (lab, im) in enumerate(tiles):
    sheet.paste(im, ((i % cols) * tw, (i // cols) * th))
p = OUT / "sheet_from_final_mp4.png"
sheet.save(p)
print(f"DA LUU: {p}  ({sheet.size[0]}x{sheet.size[1]})")
print("Chu thu tu (2 cot, doc hang):")
for i, (lab, _) in enumerate(tiles):
    print(f"  {i+1}. {lab}  (hang {i//cols+1}, cot {i%cols+1})")
