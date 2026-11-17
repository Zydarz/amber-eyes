# -*- coding: utf-8 -*-
"""Tập 12 — crop siêu gần vùng nghi còn chữ sau vòng 2."""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t12" / "zoom4"
OUT.mkdir(parents=True, exist_ok=True)

CROPS = [
    ("reel_to_reel_archive_recorder", (0.37, 0.70, 0.67, 0.79), 4),
    ("old_radio_receiver_dark", (0.20, 0.45, 0.80, 0.85), 2),
    ("state_department_empty_corridor", (0.55, 0.25, 1.00, 0.75), 2),
    ("sinking_bundles_muddy_road", (0.30, 0.55, 0.95, 1.00), 2),
]
for name, (x0, y0, x1, y1), k in CROPS:
    im = Image.open(BG / f"t12_{name}.png")
    w, h = im.size
    c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    c = c.resize((int(c.width * k), int(c.height * k)), Image.Resampling.LANCZOS)
    c.save(OUT / f"{name}.png")
    print(f"ok {name} -> {c.size}")
