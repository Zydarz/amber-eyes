#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung contact sheet tu 110 anh tinh cua EN Tap03 de soi bang mat (H9/H2).

Sheet 4x4, moi o ghi shot id + moc thoi gian + template.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
SD = W / "video3_EN_t03" / "stills"
OUT = W / "qc_en_t03_stills"
OUT.mkdir(parents=True, exist_ok=True)

shots = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["shots"]
try:
    fl = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 20)
except OSError:
    fl = ImageFont.load_default()

COLS, ROWS, TW, TH, PER = 4, 4, 470, 264, 16
missing = []
sheets = (len(shots) + PER - 1) // PER
for k in range(sheets):
    chunk = shots[k * PER:(k + 1) * PER]
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 28)), (14, 14, 17))
    d = ImageDraw.Draw(sheet)
    for i, s in enumerate(chunk):
        p = SD / f"shot_{s['id']}.png"
        if not p.exists():
            missing.append(s["id"])
            continue
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x, y = (i % COLS) * TW, (i // COLS) * (TH + 28)
        sheet.paste(im, (x, y))
        mid = (s["start"] + s["end"]) / 2
        d.text((x + 6, y + TH + 3), f"{s['id']} | {int(mid // 60)}:{mid % 60:05.2f} | {s['template']}"
               f"{s['variant']} | {s['bg']}", font=fl, fill=(242, 239, 233))
    out = OUT / f"stills_{k + 1:02d}.png"
    sheet.save(out)
    print("sheet", out)

n = len(list(SD.glob("shot_*.png")))
print(f"\nanh tinh: {n} file · thieu {len(missing)} {missing[:10]}")
print(f"sheet: {sheets} · thu muc {OUT}")
