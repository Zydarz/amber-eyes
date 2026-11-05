"""Contact sheet ảnh tĩnh — tách theo HỒI, kích thước lớn để ĐỌC CHỮ trên hình (H9).

Dùng khi cần soi bằng mắt: 4 cột, thumbnail 480x270, tên shot + số thứ tự.

Dung:
    py -3 .work/_make_stills_sheets_by_act_t04.py vi
    py -3 .work/_make_stills_sheets_by_act_t04.py en
    py -3 .work/_make_stills_sheets_by_act_t04.py ja
"""
import math
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]

LANGS = {
    "vi": (".work/video3_t04/stills", "02_SAN_XUAT/Tap04", "contact_sheet_t04_act"),
    "en": (".work/video3_EN_t04/stills", "02_SAN_XUAT/Tap04_EN", "contact_sheet_t04_EN_act"),
    "ja": (".work/video3_JA_t04/stills", "02_SAN_XUAT/Tap04_JA", "contact_sheet_t04_JA_act"),
}
LANG = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
if LANG not in LANGS:
    sys.exit(f"ngon ngu khong hop le: {LANG} (vi|en|ja)")
STILLS = ROOT / LANGS[LANG][0]
OUT = ROOT / LANGS[LANG][1]
PREFIX = LANGS[LANG][2]

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
    out = OUT / f"{PREFIX}{act}.png"
    sheet.save(out)
    print(f"[{LANG}] act {act}: {len(lst)} anh -> {out.name} ({W}x{H})")
print("xong")
