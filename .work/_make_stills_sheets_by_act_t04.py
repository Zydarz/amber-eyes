"""Contact sheet 84 anh — tach theo HOI, kich thuoc lon de DOC CHU tren hinh (H9).

Dung khi can soi bang mat: 4 cot, thumbnail 480x270, ten shot + so thu tu.
"""
import math
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
STILLS = ROOT / ".work" / "video3_t04" / "stills"
OUT = ROOT / "02_SAN_XUAT" / "Tap04"

cols, tw, th, pad, header_h = 4, 480, 270, 12, 26
try:
    font = ImageFont.truetype("arial.ttf", 18)
except Exception:
    font = ImageFont.load_default()

stills = sorted(STILLS.glob("shot_*.png"))
if not stills:
    sys.exit("khong co anh tinh")

groups = {}
for p in stills:
    sid = p.stem.replace("shot_", "")
    act = sid.split("-")[0]
    groups.setdefault(act, []).append(p)

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
        draw.text((x + 4, y + 3), p.stem.replace("shot_", "Shot "), fill=(210, 220, 240), font=font)
        with Image.open(p) as im:
            sheet.paste(im.resize((tw, th), Image.Resampling.LANCZOS), (x, y + header_h))
    out = OUT / f"contact_sheet_t04_act{act}.png"
    sheet.save(out)
    print(f"act {act}: {len(lst)} anh -> {out.name} ({W}x{H})")
print("xong")
