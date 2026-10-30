# -*- coding: utf-8 -*-
"""Review độc lập của Mavis — trích khung giữa mỗi shot từ mp4 thành phẩm Tập 02.
Ghi vào .work/_qc_tap02_review/ (KHÔNG đụng vào thư mục QC của dự án).
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MASTER = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "Tap02_master.mp4"
OUT = WORK / "_qc_tap02_review"

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

sh = json.loads((WORK / "shots_t02.json").read_text(encoding="utf-8"))
shots = sh["shots"]
OUT.mkdir(parents=True, exist_ok=True)
FR = OUT / "frames"
FR.mkdir(exist_ok=True)

items = []
for s in shots:
    mid = (s["start"] + s["end"]) / 2
    p = FR / f"{s['id']}.png"
    if not p.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{mid:.3f}", "-i", str(MASTER),
                        "-frames:v", "1", str(p)], check=True)
    items.append((s["id"], mid, s, p))
print(f"lay {len(items)} khung")

COLS, ROWS = 4, 4
TW, TH = 480, 270
PER = COLS * ROWS
try:
    f_lab = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 20)
except OSError:
    f_lab = ImageFont.load_default()

sheets = (len(items) + PER - 1) // PER
index = []
for k in range(sheets):
    chunk = items[k * PER:(k + 1) * PER]
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 28)), (14, 14, 17))
    d = ImageDraw.Draw(sheet)
    for i, (sid, mid, s, p) in enumerate(chunk):
        im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
        x, y = (i % COLS) * TW, (i // COLS) * (TH + 28)
        sheet.paste(im, (x, y))
        d.text((x + 6, y + TH + 3),
               f"{sid} · {int(mid // 60)}:{mid % 60:05.2f} · {s['template']} · {s['bg']}",
               font=f_lab, fill=(242, 239, 233))
    out = OUT / f"sheet_{k + 1:02d}.png"
    sheet.save(out)
    index.append((out.name, [c[0] for c in chunk]))
    print(" ", out.name, "->", ", ".join(c[0] for c in chunk))
print("HOAN TAT")
