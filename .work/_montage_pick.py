#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghép montage các nền CỐ ĐỊNH (không theo tập) để chọn nền cho trailer.

Dùng: py -3 .work/_montage_pick.py
Ghi:  .work/qc_montage/pick_trailer.jpg
"""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / ".work" / "qc_montage"
OUT.mkdir(parents=True, exist_ok=True)

NAMES = [
    "pinboard", "interrogation", "clinical", "corridor", "records", "podcast_desk",
    "spotlight", "brain_desk", "void", "fog", "hands", "glass_box",
    "two_shadows", "phone_dark", "cage", "prison_window", "court_dawn", "fog_deedee",
    "t11_amber_eyes_redflag_intro", "t11_closing_dossier_stamp",
    "t29_amber_eyes_closing_dossier_dahmer", "t10_amber_eyes_closing_dossier_colleen",
]

CELL, COLS = 640, 4
font = ImageFont.truetype("arial.ttf", 22)
items = []
for n in NAMES:
    p = ROOT / "assets" / "bg" / f"{n}.png"
    if not p.exists():
        print("!! thiếu:", n)
        continue
    im = Image.open(p).convert("RGB")
    h = int(CELL * im.height / im.width)
    items.append((n, im.resize((CELL, h), Image.LANCZOS)))

rows = (len(items) + COLS - 1) // COLS
row_h = [max(it[1].height for it in items[r * COLS:(r + 1) * COLS]) for r in range(rows)]
sheet = Image.new("RGB", (COLS * CELL, sum(row_h) + rows * 34), (18, 18, 22))
d = ImageDraw.Draw(sheet)
y = 0
for r in range(rows):
    for c, (n, im) in enumerate(items[r * COLS:(r + 1) * COLS]):
        x = c * CELL
        sheet.paste(im, (x, y + 34))
        d.text((x + 8, y + 6), n, font=font, fill=(255, 210, 120))
    y += row_h[r] + 34
dst = OUT / "pick_trailer.jpg"
sheet.save(dst, quality=88)
print("wrote", dst, sheet.size)
