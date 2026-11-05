#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng contact sheet từ ảnh tĩnh Tập 02 (đa ngôn ngữ VN / EN / JA / KO).

Dùng: $env:AE_LANG='ja'; $env:AE_EP='02'; py -3 .work/_mk_contact_langs.py
"""
import json
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

os.environ.setdefault("AE_EP", "02")
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

LANG = "EN" if ED.EN else ("JA" if ED.JA else ("KO" if ED.KO else "VN"))
STILLS = ED.w("video3") / "stills"
OUT = WORK / f"qc_t02_{LANG.lower()}_20261105" / "contact_sheet"
OUT.mkdir(parents=True, exist_ok=True)

SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))
shots = SH["shots"]

COLS, ROWS = 3, 3
TW = 620
TH = int(TW * 1080 / 1920)
LAB, PAD = 30, 10
PER = COLS * ROWS

try:
    font = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 20)
except Exception:
    font = ImageFont.load_default()

missing = []
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
            missing.append(s["id"])
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

print(f"{LANG}: {len(sheets)} contact sheet · {len(shots)} shot -> {OUT}")
if missing:
    print("THIEU ANH:", missing)
