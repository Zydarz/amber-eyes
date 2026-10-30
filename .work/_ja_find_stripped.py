#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tìm tên riêng tiếng Việt bị MẤT DẤU trong bản JA (vd Nguyễn Hải Dương -> Nguyen Hai Duong).

Quy ước nhà: tên riêng giữ nguyên chữ Latin GỐC, kể cả dấu tiếng Việt.
Cách phát hiện: lấy mọi cụm chữ hoa >=2 từ trong bản VN có dấu tiếng Việt,
rồi kiểm tra xem bản JA có dạng BỎ DẤU của tên đó không.

    py -3 .work/_ja_find_stripped.py
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

VN_EXTRA = set("ăâđêôơưĂÂĐÊÔƠƯ")
RX_CAPS = re.compile(r"\b([A-ZÀ-ỸĐ][A-Za-zÀ-ỹĐđ'’-]+(?:\s+[A-ZÀ-ỸĐ][A-Za-zÀ-ỹĐđ'’-]+)*)\b")


def strip_diac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


rows = []
for i in range(1, 30):
    ep = "%02d" % i
    vn_path = M.canonical_vn(ep)
    ja_path = Path(__file__).resolve().parents[1] / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not vn_path.exists() or not ja_path.exists():
        continue
    vn = vn_path.read_text(encoding="utf-8")
    ja = ja_path.read_text(encoding="utf-8")
    seen = set()
    for m in RX_CAPS.finditer(vn):
        name = m.group(1).strip(" .,;:'’-")
        if " " not in name or name in seen:
            continue
        if not any(c in VN_EXTRA for c in name):
            continue                      # không có dấu VN -> tên Latin/Korean bình thường
        seen.add(name)
        plain = strip_diac(name)
        if plain == name:
            continue
        if name in ja:
            continue                      # đã giữ đúng dấu
        if plain in ja:
            rows.append((ep, name, plain, ja.count(plain)))

print(f"=== TEN RIENG VN BI MAT DAU (JA) : {len(rows)} muc ===")
for ep, name, plain, n in rows:
    print(f"  Tap{ep}: '{name}'  ->  JA dang '{plain}'  (x{n})")
