#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trich frame DUNG giua shot (theo shots_JA_t02.json) cho cac shot da sua font."""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = W / "_cu" / "ja_t02_zoom"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MP4 = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp4"
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
smap = {s["id"]: s for s in shots}

TARGETS = ["1-05", "5-04", "5-05", "2-10", "1-01"]
ims = []
for sid in TARGETS:
    s = smap.get(sid)
    if not s:
        continue
    ts = (s["start"] + s["end"]) / 2
    p = OUT / f"vidshot_{sid}.png"
    r = subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{ts:.3f}", "-i", str(MP4),
                        "-frames:v", "1", str(p)], capture_output=True, text=True)
    print(f"  {sid}: t={ts:.2f}s rc={r.returncode}")
    if p.exists():
        im = Image.open(p).crop((0, 150, 1920, 950)).resize((900, 375), Image.Resampling.LANCZOS)
        ims.append((sid, im))

if ims:
    W_ = 900
    H_ = 375
    sheet = Image.new("RGB", (W_, (H_ + 22) * len(ims)), (15, 17, 23))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype("arial.ttf", 15)
    except Exception:
        f = ImageFont.load_default()
    y = 0
    for sid, im in ims:
        d.text((6, y + 3), f"SHOT {sid}", fill=(210, 220, 240), font=f)
        sheet.paste(im, (0, y + 20))
        y += H_ + 22
    out = OUT / "vid_tofu_fix_sheet.png"
    sheet.save(out)
    print("->", out, sheet.size)
