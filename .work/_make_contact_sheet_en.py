import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

stills_dir = Path(".work/video3_EN_t04/stills")
stills = sorted(stills_dir.glob("shot_*.png"))

if not stills:
    print("No stills found!")
    exit(1)

cols = 6
rows = math.ceil(len(stills) / cols)
tw, th = 320, 180
pad = 10
header_h = 24

W = cols * tw + (cols + 1) * pad
H = rows * (th + header_h) + (rows + 1) * pad

sheet = Image.new("RGB", (W, H), (15, 17, 23))
draw = ImageDraw.Draw(sheet)

try:
    font = ImageFont.truetype("arial.ttf", 16)
except Exception:
    font = ImageFont.load_default()

for idx, p in enumerate(stills):
    r = idx // cols
    c = idx % cols
    x = pad + c * (tw + pad)
    y = pad + r * (th + header_h + pad)

    sid = p.stem.replace("shot_", "")
    draw.text((x + 4, y + 2), f"Shot {sid} (EN)", fill=(200, 210, 230), font=font)

    with Image.open(p) as img:
        thumb = img.resize((tw, th), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x, y + header_h))

out_path = Path("02_SAN_XUAT/Tap04_EN/contact_sheet_stills_t04_EN.png")
sheet.save(out_path, quality=90)
print(f"Contact sheet created: {out_path} ({len(stills)} stills, {W}x{H})")
