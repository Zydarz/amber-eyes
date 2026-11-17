# -*- coding: utf-8 -*-
"""Tập 12 — crop siêu gần các vùng nghi có chữ (kiểm chứng cuối)."""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t12" / "zoom3"
OUT.mkdir(parents=True, exist_ok=True)

# (tên, (x0,y0,x1,y1) theo tỉ lệ 0-1 của ảnh gốc 2112x1188)
CROPS = [
    ("testimony_room_single_chair", (0.55, 0.35, 0.75, 0.60)),
    ("urgent_appeal_dark_office", (0.25, 0.30, 0.95, 0.75)),
    ("memorial_stone_candles_dawn", (0.00, 0.10, 0.55, 0.75)),
    ("call_to_action_muted_desk", (0.20, 0.15, 0.90, 0.75)),
]
for name, (x0, y0, x1, y1) in CROPS:
    im = Image.open(BG / f"t12_{name}.png")
    w, h = im.size
    box = (int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))
    c = im.crop(box)
    # upscale 1.5x cho dễ đọc
    c = c.resize((int(c.width * 1.5), int(c.height * 1.5)), Image.Resampling.LANCZOS)
    c.save(OUT / f"{name}.png")
    print(f"ok {name} {box} -> {c.size}")
