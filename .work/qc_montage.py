#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC MONTAGE — gộp nhiều ảnh thành **1 tờ** để soi bằng mắt tiết kiệm token.

Lý do (đo 12/11/2026, Tập 10): đọc 6 tờ contact sheet = 6 lần đưa ảnh vào context
(~1,5–2,2k token/ảnh) ⇒ tốn ~30–42k token chỉ để soi. 1 montage duy nhất = 1 lần đọc.

Dùng:
  py -3 .work/qc_montage.py --ep 10 --kind bg
  py -3 .work/qc_montage.py --ep 10 --kind stills --lang en
  py -3 .work/qc_montage.py --ep 10 --kind stills --lang vi --only 1-04,2-08
  py -3 .work/qc_montage.py --ep 10 --kind bg --cols 8 --cell 320

Ghi: .work/qc_montage/epXX_<kind>[_<lang>].jpg
"""
import argparse
import json
import pathlib
import re
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
W = ROOT / ".work"

ap = argparse.ArgumentParser()
ap.add_argument("--ep", required=True)
ap.add_argument("--kind", choices=["bg", "stills"], required=True)
ap.add_argument("--lang", default="vi")
ap.add_argument("--only", default="", help="danh sách id cách nhau bằng dấu phẩy")
ap.add_argument("--cols", type=int, default=8)
ap.add_argument("--cell", type=int, default=384, help="bề rộng ô (cao = cell*9/16)")
ap.add_argument("--list", default="", help="file json của qc_eyeball_list (khoá 'must') — chỉ ghép shot bắt buộc soi")
ap.add_argument("--font", type=int, default=0, help="cỡ chữ nhãn (0 = tự co theo ô)")
ap.add_argument("--out", default="")
a = ap.parse_args()

EP = a.ep
OUTDIR = W / "qc_montage"
OUTDIR.mkdir(parents=True, exist_ok=True)

try:
    f = ImageFont.truetype("arial.ttf", a.font or max(15, a.cell // 12))
except Exception:
    f = ImageFont.load_default()

only = {x.strip() for x in a.only.split(",") if x.strip()}

if a.list:
    p = pathlib.Path(a.list)
    if not p.exists():
        p = W / a.list
    data = json.loads(p.read_text(encoding="utf-8"))
    only |= {str(x) for x in (data.get("must") or data if isinstance(data, list) else data.get("must", []))}

if a.kind == "bg":
    files = sorted((ROOT / "assets" / "bg").glob(f"t{EP}_*.png"))
    label = lambda p: p.stem.replace(f"t{EP}_", "")          # noqa: E731
else:
    d = W / (f"video3_t{EP}" if a.lang == "vi" else f"video3_{a.lang.upper()}_t{EP}") / "stills"
    files = sorted(d.glob("shot_*.png"))
    label = lambda p: p.stem.replace("shot_", "")            # noqa: E731

if only:
    files = [p for p in files if label(p) in only]

if not files:
    print(f"khong co anh nao (kind={a.kind}, ep={EP})")
    sys.exit(1)

cols = max(1, min(a.cols, len(files)))
rows = (len(files) + cols - 1) // cols
cw = a.cell
ch = int(cw * 9 / 16)
pad = 4
lab = (a.font or max(15, a.cell // 12)) + 8
sheet = Image.new("RGB", (cols * (cw + pad), rows * (ch + lab + pad)), (8, 8, 10))
dr = ImageDraw.Draw(sheet)
for i, p in enumerate(files):
    c, r = i % cols, i // cols
    im = Image.open(p).convert("RGB").resize((cw, ch), Image.LANCZOS)
    x, y = c * (cw + pad), r * (ch + lab + pad)
    sheet.paste(im, (x, y))
    dr.text((x + 3, y + ch + 3), label(p), font=f, fill=(232, 232, 238))

name = a.out or f"ep{EP}_{a.kind}" + ("" if a.kind == "bg" else f"_{a.lang}")
out = OUTDIR / f"{name}.jpg"
sheet.save(out, quality=88)
print(f"ok {out.relative_to(ROOT)} · {sheet.size} · {len(files)} anh · "
      f"{rows} hang x {cols} cot")
