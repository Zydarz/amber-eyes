#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung contact sheet tu anh tinh Tap 02 de duyet noi dung va bo cuc."""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
STILLS = WORK / "video3_t02" / "stills"
OUT = WORK / "qc_t02_20261105" / "contact_sheet"
OUT.mkdir(parents=True, exist_ok=True)

sh = json.loads((WORK / "shots_t02.json").read_text(encoding="utf-8"))
shots = sh["shots"]

COLS, ROWS = 3, 3
TW = 620
TH = int(TW * 1080 / 1920)
LAB, PAD = 30, 10
PER = COLS * ROWS

try:
    font = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 20)
except Exception:
    font = ImageFont.load_default()

sheets = []
for i in range(0, len(shots), PER):
    chunk = shots[i:i + PER]
    w = COLS * (TW + PAD) + PAD
    h = ROWS * (TH + LAB + PAD) + PAD
    sheet = Image.new("RGB", (w, h), (16, 16, 20))
    d = ImageDraw.Draw(sheet)
    for k, s in enumerate(chunk):
        p = STILLS / f"shot_{s['id']}.png"
        if not p.exists():
            continue
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x = PAD + (k % COLS) * (TW + PAD)
        y = PAD + (k // COLS) * (TH + LAB + PAD)
        sheet.paste(im, (x, y))
        dur = s["end"] - s["start"]
        d.text((x + 4, y + TH + 4), f"{s['id']}  {dur:.1f}s  {s['bg']}", fill=(240, 220, 120), font=font)
    name = OUT / f"sheet_{i//PER + 1:02d}.png"
    sheet.save(name)
    sheets.append(name)
    print(name)

print(f"\n{len(sheets)} contact sheet · {len(shots)} shot")
