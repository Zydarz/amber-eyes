#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng contact sheet ảnh tĩnh Tập 03 cho một bản ngôn ngữ.

    py -3 .work/_mk_contact_t03.py [vi|en|ja]
"""
import json
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANG = sys.argv[1] if len(sys.argv) > 1 else "vi"
os.environ["AE_EP"] = "03"
os.environ["AE_LANG"] = {"vi": "", "en": "en", "ja": "ja"}[LANG]
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

SUF = {"vi": "", "en": "_EN", "ja": "_JA"}[LANG]
TAG = {"vi": "t03", "en": "t03_EN", "ja": "t03_JA"}[LANG]
STILLS = ED.w("video3") / "stills"
OUT = WORK / f"qc_t03_20261105" / f"contact_sheet_{LANG}"
OUT.mkdir(parents=True, exist_ok=True)
DST = ROOT / "02_SAN_XUAT" / f"Tap03{SUF}"

sh = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))
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

missing = []
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
        d.text((x + 4, y + TH + 4), f"{s['id']}  {s['end'] - s['start']:.1f}s  {s['bg']}",
               fill=(240, 220, 120), font=font)
    sheet.save(OUT / f"sheet_{i//PER + 1:02d}.png")

n = len(list(OUT.glob("sheet_*.png")))
print(f"[{LANG}] {n} contact sheet · {len(shots)} shot · thiếu ảnh: {missing}")

# ---- theo HỒI
acts = {}
for s in shots:
    acts.setdefault(s["id"].split("-")[0], []).append(s)
for act in sorted(acts):
    grp = acts[act]
    w = COLS * (TW + PAD) + PAD
    rows = (len(grp) + COLS - 1) // COLS
    h = rows * (TH + LAB + PAD) + PAD
    sheet = Image.new("RGB", (w, h), (16, 16, 20))
    d = ImageDraw.Draw(sheet)
    for k, s in enumerate(grp):
        p = STILLS / f"shot_{s['id']}.png"
        if not p.exists():
            continue
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x = PAD + (k % COLS) * (TW + PAD)
        y = PAD + (k // COLS) * (TH + LAB + PAD)
        sheet.paste(im, (x, y))
        d.text((x + 4, y + TH + 4), f"{s['id']}  {s['end'] - s['start']:.1f}s  {s['bg']}",
               fill=(240, 220, 120), font=font)
    name = DST / f"contact_sheet_{TAG}_act{act}.png"
    sheet.save(name)
    print(f"  {name}  ({len(grp)} shot)")
