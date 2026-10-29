#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A9.3 — lấy 1 khung giữa mỗi shot TẬP 02 TỪ CHÍNH FILE MP4 THÀNH PHẨM,
rồi ghép contact sheet 16 ảnh/tờ để soi bằng mắt.

Chạy sau khi package.py --mux xong:
    python .work/_qc_tap02_frames.py
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MASTER = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"
STILLS = WORK / "video3_t02" / "stills"
OLD = WORK / "video3_t02" / "stills_0909"
OUT = WORK / "qc_tap02"

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

sh = json.loads((WORK / "shots_t02.json").read_text(encoding="utf-8"))
shots = sh["shots"]
if not MASTER.exists():
    raise SystemExit(f"chua co {MASTER}")
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "frames").mkdir(exist_ok=True)

# giu lai anh tinh cu (bang timeline truoc 18:08) de doi chieu
if STILLS.exists() and not OLD.exists():
    shutil.move(str(STILLS), str(OLD))
STILLS.mkdir(parents=True, exist_ok=True)

print(f"lay {len(shots)} khung giua moi shot tu {MASTER.name} ...")
paths = []
for s in shots:
    mid = (s["start"] + s["end"]) / 2
    p = STILLS / f"{s['id']}.png"
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{mid:.3f}",
                    "-i", str(MASTER), "-frames:v", "1", str(p)], check=True)
    paths.append((s["id"], mid, p))
print("xong.")

# contact sheet 4x4
COLS, ROWS = 4, 4
TW, TH = 480, 270
PER = COLS * ROWS
try:
    f_lab = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 22)
except OSError:
    f_lab = ImageFont.load_default()

sheets = (len(paths) + PER - 1) // PER
for k in range(sheets):
    chunk = paths[k * PER:(k + 1) * PER]
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 30)), (14, 14, 17))
    d = ImageDraw.Draw(sheet)
    for i, (sid, mid, p) in enumerate(chunk):
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x = (i % COLS) * TW
        y = (i // COLS) * (TH + 30)
        sheet.paste(im, (x, y))
        d.text((x + 8, y + TH + 4), f"{sid}  ·  {int(mid//60)}:{mid % 60:06.3f}",
               font=f_lab, fill=(242, 239, 233))
    out = OUT / f"sheet_{k + 1:02d}.png"
    sheet.save(out)
    print("  ", out.name, "-", ", ".join(c[0] for c in chunk))
print(f"HOAN TAT: {len(paths)} khung, {sheets} to contact sheet -> {OUT}")
