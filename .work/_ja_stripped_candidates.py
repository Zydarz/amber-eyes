#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê các mảnh tên riêng tiếng Việt bị BỎ DẤU trong bản JA (danh sách ứng viên).

Nguyên tắc: trong bản VN, mọi từ Việt có dấu viết HOA ĐẦU CÂU (vd "Nguyễn",
"Dương", "Bình") là tên riêng -> bản JA phải giữ nguyên dấu.

    py -3 .work/_ja_stripped_candidates.py
"""
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

VN_EXTRA = set("ăâđêôơưĂÂĐÊÔƠƯ")
RX_WORD_VN = re.compile(r"[A-Za-zÀ-ỹĐđ]+")
RX_LAT_JA = re.compile(r"(?<![A-Za-zÀ-ỹĐđ])[A-Za-zÀ-ỹĐđ]{2,}(?![A-Za-zÀ-ỹĐđ])")


def strip_diac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


rows = []
for i in range(1, 30):
    ep = "%02d" % i
    vp = M.canonical_vn(ep)
    jp = Path(r"D:\TEST\Gax\Audi\01_KICH_BAN") / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not vp.exists() or not jp.exists():
        continue
    vn = vp.read_text(encoding="utf-8")
    ja = jp.read_text(encoding="utf-8")

    # các từ Việt có dấu, viết HOA ĐẦU CÂU trong bản VN
    names = {}
    for m in RX_WORD_VN.finditer(vn):
        w = m.group(0)
        if len(w) < 2 or not any(c in VN_EXTRA for c in w):
            continue
        prev = vn[max(0, m.start() - 1):m.start()]
        if prev and (prev[-1].isalpha() or prev[-1] == "-"):
            continue                        # đang ở giữa một từ khác
        names.setdefault(w, 0)

    for w in sorted(names):
        plain = strip_diac(w)
        if plain == w:
            continue
        n_plain = len(RX_LAT_JA.findall(plain)) and len(
            re.findall(r"(?<![A-Za-zÀ-ỹĐđ])" + re.escape(plain) + r"(?![A-Za-zÀ-ỹĐđ])", ja))
        n_diac = len(re.findall(r"(?<![A-Za-zÀ-ỹĐđ])" + re.escape(w) + r"(?![A-Za-zÀ-ỹĐđ])", ja))
        if n_plain and n_plain > n_diac:
            rows.append((ep, w, plain, n_plain, n_diac))

print(f"=== {len(rows)} ung vien ===")
for ep, w, plain, npl, ndi in rows:
    print(f"  Tap{ep}: '{w}' (dau {ndi}) -> '{plain}' (mat dau {npl})")
