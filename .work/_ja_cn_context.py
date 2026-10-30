#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê MỌI chỗ có chữ Trung-only trong 29 file JA, kèm ngữ cảnh và đề xuất.

    py -3 .work/_ja_cn_context.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(HERE))
from _ja_scan_cn_only import CN2JP  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "01_KICH_BAN"

# quy tắc theo ngữ cảnh (cụm) -> thay thế Nhật
CTX = {
    "沟通": "意思疎通", "节奏": "リズム", "心理解码": "心理解コード",
    "辩护": "抗弁", "辩解": "弁明", "辩论": "論争", "争辩": "争い",
    "缓解": "緩和", "乐趣": "楽しみ", "抑郁": "うつ",
    "引进": "導入", "领导者": "リーダー", "引导": "誘導",
    "一段": "一段", "章节": "章", "节奏感": "リズム感",
    "乐意": "喜ぶ", "乐趣": "楽しみ", "音乐": "音楽",
}

# ký tự đơn lẻ -> ký tự Nhật
CHAR = dict(CN2JP)
# các chữ mà dạng giản thạch TRÙNG với shinjitai Nhật -> bỏ (không sửa)
for k in list(CHAR):
    if k == CHAR[k]:
        del CHAR[k]

print("Bang doi chua dung (key == value) -> bo qua:", [k for k in CN2JP if k == CN2JP[k]])
print()

total = 0
for i in range(1, 30):
    ep = "%02d" % i
    f = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not f.exists():
        continue
    for n, ln in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if not any(c in ln for c in CHAR):
            continue
        # các cụm cần xử lý riêng
        done = ln
        for cn, jp in CTX.items():
            done = done.replace(cn, jp)
        # các ký tự lẻ còn lại
        rest = sorted({c for c in done if c in CHAR})
        if not rest:
            continue
        # in từng vị trí
        for m in re.finditer("[" + "".join(CHAR) + "]", ln):
            c = m.group(0)
            s = max(0, m.start() - 12)
            print(f"Tap{ep} d{n}: ...{ln[s:m.start()+14]}...")
            print(f"        -> [{c}] : {CHAR[c]}   | U+{ord(c):04X}")
            total += 1
print(f"\nTONG {total} ky tu")
