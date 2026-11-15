import json
import math
import os
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
jobs = json.load(open(WORK / "bg_jobs_tap15.json", encoding="utf-8"))

w_thumb = 352
h_thumb = 198
cols = 7
rows = math.ceil(len(jobs) / cols)
pad = 10

cs_w = cols * (w_thumb + pad) + pad
cs_h = rows * (h_thumb + pad + 25) + pad
canvas = Image.new("RGB", (cs_w, cs_h), (18, 18, 20))
draw = ImageDraw.Draw(canvas)

for idx, j in enumerate(jobs):
    r = idx // cols
    c = idx % cols
    x = pad + c * (w_thumb + pad)
    y = pad + r * (h_thumb + pad + 25)
    img_path = ROOT / "assets" / "bg" / f"{j['name']}.png"
    if img_path.exists():
        with Image.open(img_path) as im:
            thumb = im.resize((w_thumb, h_thumb), Image.Resampling.LANCZOS)
            canvas.paste(thumb, (x, y))
    draw.text((x + 4, y + h_thumb + 4), f"#{idx+1:02d} {j['name'][:25]}", fill=(200, 200, 200))

out_cs = ROOT / "02_SAN_XUAT" / "Tap15" / "contact_sheet_t15.png"
canvas.save(out_cs)
print("Saved contact sheet successfully:", out_cs)
