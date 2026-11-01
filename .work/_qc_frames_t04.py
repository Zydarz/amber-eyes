#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trich khung tu video CUOI va khop voi anh tinh — kiem chuc H9/H13/H14 o kha cuoi.

- doc timeline + shots (thoi gian that)
- trich khung giua moi shot tu file .mp4 cuoi
- ghep lai contact sheet de SOI BANG MAT
- canh bao shot nao khung den (nen thieu) hoac khung toi (khong giu duoc mau nen)

Chay: py -3 .work/_qc_frames_t04.py --ep 04 [--file .../Tap04_master.mp4]
"""
import argparse
import json
import pathlib
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

ap = argparse.ArgumentParser()
ap.add_argument("--ep", default="04")
ap.add_argument("--file", default=None)
ap.add_argument("--every", type=int, default=1, help="chi lay 1/ N shot")
a = ap.parse_args()
ep = a.ep

sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

final = pathlib.Path(a.file) if a.file else (
    ROOT / "02_SAN_XUAT" / f"Tap{ep}" / "xuat_ban" / f"Tap{ep}_master.mp4")
shots = json.loads(ED.w("shots.json").read_text(encoding="utf-8-sig"))["shots"]
out = WORK / f"_qc_frames_t{ep}"
out.mkdir(parents=True, exist_ok=True)
for p in out.glob("*.png"):
    p.unlink()

picks = [s for i, s in enumerate(shots) if i % a.every == 0]
tiles = []
for s in picks:
    t = (s["start"] + s["end"]) / 2
    png = out / f"f_{s['id']}.png"
    r = subprocess.run([str(FF), "-v", "error", "-ss", f"{t:.3f}", "-i", str(final),
                        "-frames:v", "1", "-y", str(png)], capture_output=True, text=True)
    if not png.exists() or png.stat().st_size < 5000:
        print(f"  [LOI] {s['id']} @ {t:.1f}s khong trich duoc khung")
        continue
    tiles.append((s["id"], t, png))
print(f"trich {len(tiles)}/{len(picks)} khung tu {final.name}")

cols, tw, th, pad, hh = 5, 380, 214, 10, 24
rows = (len(tiles) + cols - 1) // cols
W = cols * tw + (cols + 1) * pad
H = rows * (th + hh) + (rows + 1) * pad
sheet = Image.new("RGB", (W, H), (15, 17, 23))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("arial.ttf", 16)
except Exception:
    font = ImageFont.load_default()
for i, (sid, t, png) in enumerate(tiles):
    r, c = i // cols, i % cols
    x = pad + c * (tw + pad)
    y = pad + r * (th + hh + pad)
    d.text((x + 3, y + 3), f"{sid}  t={t:.1f}s", fill=(200, 212, 235), font=font)
    with Image.open(png) as im:
        sheet.paste(im.resize((tw, th), Image.Resampling.LANCZOS), (x, y + hh))
outp = ROOT / "02_SAN_XUAT" / f"Tap{ep}" / f"qc_frames_t{ep}.png"
outp.parent.mkdir(parents=True, exist_ok=True)
sheet.save(outp)
print("->", outp, sheet.size)
