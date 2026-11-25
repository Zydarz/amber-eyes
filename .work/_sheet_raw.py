# -*- coding: utf-8 -*-
"""Contact sheet nhanh cho 1 nhom anh raw (dung de soi chat luong engine)."""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent
pat = sys.argv[1]
out = sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6
CW = 320
CH = int(CW * 9 / 16)
PAD, LAB = 4, 24

files = sorted(HERE.glob(pat)) if not pathlib.Path(pat).is_absolute() else sorted(pathlib.Path(pat).parent.glob(pathlib.Path(pat).name))
if not files:
    print("khong co anh")
    sys.exit(1)
try:
    font = ImageFont.truetype("arial.ttf", 14)
except Exception:  # noqa: BLE001
    font = ImageFont.load_default()
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (CW + PAD), rows * (CH + LAB + PAD)), (8, 8, 10))
d = ImageDraw.Draw(sheet)
for i, p in enumerate(files):
    c, r = i % cols, i // cols
    x, y = c * (CW + PAD), r * (CH + LAB + PAD)
    sheet.paste(Image.open(p).convert("RGB").resize((CW, CH), Image.Resampling.LANCZOS), (x, y))
    d.text((x + 3, y + CH + 3), p.stem[:34], font=font, fill=(232, 232, 238))
sheet.save(out, quality=90)
print("%s  %dx%d  %d anh" % (out, sheet.size[0], sheet.size[1], len(files)))
