#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tờ soi mắt riêng cho 47 ảnh vừa sinh lại (theo .work/_qc_flags_t37_39.json).

Dùng: py -3 .work/_qc_sheet_regen.py
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "qc_montage"
FLAGS = ROOT / ".work" / "_qc_flags_t37_39.json"

data = json.loads(FLAGS.read_text(encoding="utf-8"))
items = [(int(f["ep"]), f["name"], f.get("reason", "")) for f in data["flags"]]

CW, PAD, LAB = 512, 6, 44
CH = int(CW * 9 / 16)
ROW = CH + LAB + PAD
COLS, PER = 4, 16

try:
    font = ImageFont.truetype("arial.ttf", 21)
except Exception:
    font = ImageFont.load_default()

OUT.mkdir(parents=True, exist_ok=True)
miss = [n for _, n, _ in items if not (BG / f"{n}.png").exists()]
print(f"Tong 47 anh can soi. Thieu file: {len(miss)}")
if miss:
    for m in miss:
        print("  THIEU:", m)

for part in range(0, len(items), PER):
    chunk = items[part:part + PER]
    rows = (len(chunk) + COLS - 1) // COLS
    sheet = Image.new("RGB", (COLS * (CW + PAD), rows * ROW), (10, 10, 12))
    dr = ImageDraw.Draw(sheet)
    for i, (ep, name, reason) in enumerate(chunk):
        c, r = i % COLS, i // COLS
        p = BG / f"{name}.png"
        if not p.exists():
            continue
        im = Image.open(p).convert("RGB").resize((CW, CH), Image.LANCZOS)
        x, y = c * (CW + PAD), r * ROW
        sheet.paste(im, (x, y))
        label = f"t{ep} {name.replace(f't{ep}_', '')}"
        dr.text((x + 4, y + CH + 3), label[:60], font=font, fill=(240, 240, 245))
        dr.text((x + 4, y + CH + 24), reason[:60], font=font, fill=(255, 190, 120))
    out = OUT / f"regen_{part // PER:02d}.jpg"
    sheet.save(out, quality=90)
    print(f"ok {out.name} {sheet.size} {len(chunk)} anh")
