#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua 2-05/2-06: trong T8, ' · ' la dau tach MUC — ngay '7 · 5 · 1972' bi tach thanh 3 muc.
Moi muc phai la 1 cum tu (va dung tu khi cau do doc)."""
import sys
from pathlib import Path

PLAN = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\KeHoach_Video_Tap03.md")
text = PLAN.read_text(encoding="utf-8-sig")

FIXES = [
    ("| 2-05 | `2.04#3`–`#4` | H | T8 | `t3_santacruz_street` | *Ngày 7 · 5 · 1972: Mary Ann Pesce & Anita Luchessa (18 tuổi) · Nhốt người kia vào cốp xe*",
     "| 2-05 | `2.04#3`–`#4` | H | T8 | `t3_santacruz_street` | *Ngày 7 tháng 5 năm 1972 · Mary Ann Pesce & Anita Luchessa (18 tuổi) · Nhốt người kia vào cốp xe*"),
    ("| 2-06 | `2.04#5`–`#6` | H | T8 | `t3_case_photos` | *Ngày 14 · 9 · 1972: Aiko Koo (15 tuổi) · Ngày 7 · 1 · 1973: Cindy Schall (18 tuổi)*",
     "| 2-06 | `2.04#5`–`#6` | H | T8 | `t3_case_photos` | *Ngày 14 tháng 9 năm 1972 · Aiko Koo (15 tuổi) · Ngày 7 tháng 1 năm 1973 · Cindy Schall (18 tuổi)*"),
]

fail = 0
for old, new in FIXES:
    n = text.count(old)
    if n != 1:
        print(f"[FAIL x{n}]: {old[:120]}")
        fail += 1
        continue
    text = text.replace(old, new)
    print(f"[OK ] {new.split('|')[1].strip()}")

if fail:
    print("\nKHONG ghi file.")
    sys.exit(1)
PLAN.write_text(text, encoding="utf-8")
print("\nDa ghi.")
