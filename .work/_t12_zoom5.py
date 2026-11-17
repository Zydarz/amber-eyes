# -*- coding: utf-8 -*-
"""Tập 12 — crop chính xác mặt máy reel-to-reel + góc tường có vết sổ xước."""
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t12" / "zoom5"
OUT.mkdir(parents=True, exist_ok=True)

CROPS = [
    ("reel_to_reel_archive_recorder", "panel", (0.375, 0.575, 0.575, 0.640), 6),
    ("reel_to_reel_archive_recorder", "wall", (0.700, 0.130, 0.820, 0.360), 4),
]
for name, tag, (x0, y0, x1, y1), k in CROPS:
    im = Image.open(BG / f"t12_{name}.png")
    w, h = im.size
    c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    c = c.resize((int(c.width * k), int(c.height * k)), Image.Resampling.LANCZOS)
    c.save(OUT / f"{name}_{tag}.png")
    print(f"ok {name}_{tag} -> {c.size}")
