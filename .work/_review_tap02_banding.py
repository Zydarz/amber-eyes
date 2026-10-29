# -*- coding: utf-8 -*-
"""Kiem tra cuoi: (1) khung day du cu 3 shot, (2) do dai mau/banding tren nen toi."""
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(r"D:\TEST\Gax\Audi\.work")
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
VID = Path(r"D:\TEST\Gax\Audi\02_SAN_XUAT\Tap02\xuat_ban\Tap02_master.mp4")
D = WORK / "_qc_tap02_review" / "zoom"
D.mkdir(parents=True, exist_ok=True)


def grab(t, name):
    p = D / f"full_{name}.png"
    if not p.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(VID),
                        "-frames:v", "1", str(p)], check=True)
    return Image.open(p).convert("RGB")


# ---------- 1. khung day du ----------
frames = [(254.74, "s1_25"), (433.60, "s2_11_dau"), (1265.11, "s5_01")]
ims = []
for t, n in frames:
    im = grab(t, n)
    im = im.resize((900, 506), Image.LANCZOS)
    ims.append((f"{n} @ {t}s", im))
sheet = Image.new("RGB", (900, 3 * (506 + 26)), (20, 20, 24))
dr = ImageDraw.Draw(sheet)
try:
    f = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 20)
except OSError:
    f = ImageFont.load_default()
y = 0
for lab, im in ims:
    sheet.paste(im, (0, y + 26))
    dr.text((6, y + 2), lab, font=f, fill=(255, 220, 120))
    y += im.height + 26
sheet.save(D / "full_montage.png")
print("->", D / "full_montage.png")

# ---------- 2. banding: do buoc mau tren vung nen toi gradient ----------
def banding(img, box, label):
    a = np.asarray(img.crop(box)).astype(np.int16)
    gray = a.mean(axis=2)
    # lay mot hang ngang va cot doc, dem cac buoc nhay mau
    h, w = gray.shape
    steps = []
    for r in range(0, h, max(1, h // 40)):
        row = gray[r]
        steps.append(np.abs(np.diff(row)))
    steps = np.concatenate(steps)
    steps = steps[steps > 0]
    big = int((steps >= 3).sum())
    print(f"{label}: buoc mau trung binh={steps.mean():.2f} · max={steps.max():.0f} · "
          f"so buoc >=3 cap = {big}/{len(steps)} ({100*big/max(1,len(steps)):.1f}%) · "
          f"so cap mau dung = {len(np.unique(gray.astype(np.uint8)))}")


im5 = grab(1265.11, "s5_01")
banding(im5, (300, 60, 1900, 200), "nen toi phong toi (5-01, vung den phia tren)")
banding(im5, (1150, 620, 1900, 1000), "nen toi goc phai (5-01)")
im1 = grab(254.74, "s1_25")
banding(im1, (100, 120, 1900, 330), "nen sang tren (1-25, xe + tuyet)")
