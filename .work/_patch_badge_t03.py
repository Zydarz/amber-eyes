#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua badge: khung phai vua chu vai (N1 'TRUC BAN CANH SAT SANTA CRUZ' bi cat).

File build_video3.py dung ket thuong "\r\r\n" -> phai giu nguyen khi ghi lai.
"""
import sys
from pathlib import Path

P = Path(r"D:\TEST\Gax\amber-eyes\.work\build_video3.py")
raw = P.read_bytes()
src = raw.decode("utf-8")
NL = "\r\r\n"

OLD = NL.join([
    "def badge_base(role, dim=False, label=None):",
    "    w_, h_ = 470, 124",
    "    im = Image.new(\"RGBA\", (w_, h_), (0, 0, 0, 0))",
    "    d = ImageDraw.Draw(im)",
    "    d.rounded_rectangle([0, 0, w_ - 1, h_ - 1], radius=18, fill=C[\"slate\"] + (217,), outline=ROLE_COLOR[role] + (160,), width=2)",
    "    p0 = cast_img(role, \"P0\", (88, 88))",
    "    im.alpha_composite(p0, (16, 18))",
    "    name, title = ROLE_NAME[role]",
    "    d.text((120, 16), name, font=F_LAB(24), fill=ROLE_COLOR[role] + (255,))",
    "    d.text((120, 46), label or title, font=F_SUB(20), fill=C[\"muted\"] + (255,))",
])

NEW = NL.join([
    "def badge_base(role, dim=False, label=None):",
    "    name, title = ROLE_NAME[role]",
    "    sub = label or title",
    "    # H9: khung badge phai vua chu — vai N1 (\"TRỰC BAN CẢNH SÁT SANTA CRUZ\") dai hon",
    "    # 350 px nen chu bi cat. Do rong khung theo chu dai nhat.",
    "    w_txt = max(F_LAB(24).getlength(name), F_SUB(20).getlength(sub))",
    "    w_, h_ = max(470, int(120 + w_txt + 22)), 124",
    "    im = Image.new(\"RGBA\", (w_, h_), (0, 0, 0, 0))",
    "    d = ImageDraw.Draw(im)",
    "    d.rounded_rectangle([0, 0, w_ - 1, h_ - 1], radius=18, fill=C[\"slate\"] + (217,), outline=ROLE_COLOR[role] + (160,), width=2)",
    "    p0 = cast_img(role, \"P0\", (88, 88))",
    "    im.alpha_composite(p0, (16, 18))",
    "    d.text((120, 16), name, font=F_LAB(24), fill=ROLE_COLOR[role] + (255,))",
    "    d.text((120, 46), sub, font=F_SUB(20), fill=C[\"muted\"] + (255,))",
])

n = src.count(OLD)
if n != 1:
    print(f"[FAIL] khop {n} lan (can 1)")
    sys.exit(1)
src = src.replace(OLD, NEW)
with open(P, "w", encoding="utf-8", newline="") as f:
    f.write(src)

chk = P.read_bytes()
print("[OK ] da sua badge_base")
print("     BOM:", chk[:3].hex(), "| CRLF:", chk.count(b"\r\r\n"), "| LF:", chk.count(b"\n"))
