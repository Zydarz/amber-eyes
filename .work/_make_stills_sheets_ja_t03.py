#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contact sheet ảnh tĩnh JA Tap03 (H9) — 1 trang/hồi + 1 trang tổng hợp."""
import json
import math
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
STILLS = ROOT / ".work" / "video3_JA_t03" / "stills"
OUT = ROOT / ".work" / "_qc_sheets_ja_t03"
SHOTS = json.loads((ROOT / ".work" / "shots_JA_t03.json").read_text(encoding="utf-8-sig"))["shots"]
ROLE = {"H": "HOST", "D": "SOR", "C": "PSY", "N1": "N1", "N2": "N2"}

cols, tw, th, pad, header_h = 4, 480, 270, 12, 30
font = ImageFont.truetype("arial.ttf", 16)

stills = sorted(STILLS.glob("shot_*.png"))
if not stills:
    sys.exit("khong co anh tinh")
meta = {s["id"]: s for s in SHOTS}

groups = {}
for p in stills:
    sid = p.stem.replace("shot_", "")
    groups.setdefault(sid.split("-")[0], []).append(p)

OUT.mkdir(parents=True, exist_ok=True)
for act in sorted(groups):
    lst = groups[act]
    rows = math.ceil(len(lst) / cols)
    W = cols * tw + (cols + 1) * pad
    H = rows * (th + header_h) + (rows + 1) * pad
    sheet = Image.new("RGB", (W, H), (15, 17, 23))
    draw = ImageDraw.Draw(sheet)
    for i, p in enumerate(lst):
        r, c = i // cols, i % cols
        x = pad + c * (tw + pad)
        y = pad + r * (th + header_h + pad)
        sid = p.stem.replace("shot_", "")
        s = meta.get(sid, {})
        role = ROLE.get(s.get("role") or "", "-")
        ns = len(s.get("sentences") or [])
        draw.text((x + 4, y + 3), f"Shot {sid} | {role} | {ns} cau | T{s.get('template') or '-'}",
                  fill=(210, 220, 240), font=font)
        with Image.open(p) as im:
            sheet.paste(im.resize((tw, th), Image.Resampling.LANCZOS), (x, y + header_h))
    out = OUT / f"sheet_act{act}.png"
    sheet.save(out)
    print(f"act {act}: {len(lst)} anh -> {out.name} ({W}x{H})")

cols2, tw2, th2 = 6, 320, 180
rows2 = math.ceil(len(stills) / cols2)
W2 = cols2 * tw2 + (cols2 + 1) * pad
H2 = rows2 * (th2 + header_h) + (rows2 + 1) * pad
sheet2 = Image.new("RGB", (W2, H2), (15, 17, 23))
d2 = ImageDraw.Draw(sheet2)
for i, p in enumerate(stills):
    r, c = i // cols2, i % cols2
    x = pad + c * (tw2 + pad)
    y = pad + r * (th2 + header_h + pad)
    sid = p.stem.replace("shot_", "")
    s = meta.get(sid, {})
    d2.text((x + 4, y + 3), f"{sid} {ROLE.get(s.get('role') or '', '-')}",
            fill=(210, 220, 240), font=font)
    with Image.open(p) as im:
        sheet2.paste(im.resize((tw2, th2), Image.Resampling.LANCZOS), (x, y + header_h))
sheet2.save(OUT / "sheet_all.png")
print(f"tong hop: {len(stills)} anh -> sheet_all.png ({W2}x{H2})")
print("xong")
