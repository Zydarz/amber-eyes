#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quet LEGIBILITY tren 83 anh tinh T04 (H9): chu trang tren nen sang = chim.

T1 ve headline o dai y=420..560, sub o y=690..780, x=96..1600 (hoac x=560..1700
khi co bust). Gradient GRAD chi lam toi vung duoi ~y=594 nen dai headline
KHONG duoc che - neu nen do sang >170 thi chu trang chet.

Cach do (khong can render lai):
  - lay pixel vung chu, tinh lum
  - nen sang = ty le pixel lum>170
  - chu trang = ty le pixel lum>235
  - coi la "chim" khi nen sang >= 22% VA chu trang >= 1.5% (ky tu chu viet day
    tren nen sang)
Xuat: .work/_cu/stills_check/legibility_t04.csv
"""
import csv
import pathlib
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
SD = ROOT / ".work" / "video3_t04" / "stills"
OUT = ROOT / ".work" / "_cu" / "stills_check" / "legibility_t04.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)

BANDS = [("head", (96, 400, 1620, 580)), ("sub", (96, 660, 1620, 800)),
         ("headR", (560, 400, 1700, 580))]

rows = []
for p in sorted(SD.glob("shot_*.png")):
    sid = p.stem.replace("shot_", "")
    im = Image.open(p).convert("L")
    best = None
    for name, box in BANDS:
        band = im.crop(box)
        px = list(band.getdata())
        n = len(px)
        bright = sum(1 for v in px if v > 170) / n
        white = sum(1 for v in px if v > 235) / n
        # diem "chim" = nen sang lon + chu trang viet tren nen do
        score = bright * white
        rec = (score, name, bright, white)
        if best is None or rec[0] > best[0]:
            best = rec
    score, name, bright, white = best
    flag = "CHIM" if (bright >= 0.22 and white >= 0.015) else ""
    rows.append((sid, name, round(bright, 3), round(white, 4), round(score, 4), flag))

rows.sort(key=lambda r: -r[4])
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["shot", "band", "pct_bright", "pct_white", "score", "flag"])
    w.writerows(rows)

print("Top 18 theo score (nen sang x chu trang):")
for r in rows[:18]:
    print("  %-6s %-6s bright=%5.1f%% white=%5.2f%% score=%.4f %s"
          % (r[0], r[1], r[2] * 100, r[3] * 100, r[4], r[5]))
print("\nSO BI NHAN 'CHIM':", sum(1 for r in rows if r[5]))
print("->", OUT)
