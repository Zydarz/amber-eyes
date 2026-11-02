"""Contact sheet ảnh tĩnh Tập 03 — tách theo HỒI, kích thước lớn để đọc chữ trên hình (H9).

4 cột, thumbnail 480x270, ghi tên shot + thứ tự.
"""
import math
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
STILLS = ROOT / ".work" / "video3_t03" / "stills"
OUT = ROOT / "02_SAN_XUAT" / "Tap03"

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
        draw.text((x + 4, y + 3), p.stem.replace("shot_", "Shot "),
                  fill=(210, 220, 240), font=font)
        with Image.open(p) as im:
            sheet.paste(im.resize((tw, th), Image.Resampling.LANCZOS), (x, y + header_h))
    out = OUT / f"contact_sheet_t03_act{act}.png"
    sheet.save(out)
    print(f"act {act}: {len(lst)} anh -> {out.name} ({W}x{H})")

# tong hop 1 trang (6 cot) de danh muc nhanh
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
    d2.text((x + 4, y + 3), p.stem.replace("shot_", "Shot "), fill=(210, 220, 240), font=font)
    with Image.open(p) as im:
        sheet2.paste(im.resize((tw2, th2), Image.Resampling.LANCZOS), (x, y + header_h))
out2 = OUT / "contact_sheet_stills_t03.png"
sheet2.save(out2)
print(f"tong hop: {len(stills)} anh -> {out2.name} ({W2}x{H2})")
print("xong")
