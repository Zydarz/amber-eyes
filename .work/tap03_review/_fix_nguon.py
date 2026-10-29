#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sửa mã câu đã dịch trong bảng nguồn Tập 03 (kịch bản viết lại => mã câu dịch)."""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

MD = Path(r"D:\TEST\Gax\Audi\02_SAN_XUAT\Tap03\xuat_ban\nguon_tham_khao.md")
raw = MD.read_text(encoding="utf-8")

FIX = [
    ("`1.09#1`",  "`1.10#1`",  1),   # dòng "609A Ord Drive" -> thuộc element 1.10
    ("`1.09#10`", "`1.10#10`", 1),   # dòng "Ngăn tôi lại"   -> thuộc element 1.10
    ("`1.09`",    "`1.10`",    1),   # phụ lục: quote "Stop me..." -> thuộc element 1.10
    ("`1.12#7`",  "`1.13#7`",  1),   # dòng VICAP           -> thuộc element 1.13
]

for old, new, n in FIX:
    c = raw.count(old)
    assert c == n, f"'{old}' xuat hien {c} lan, mong doi {n}"
    raw = raw.replace(old, new)
    print(f"  OK  {old} -> {new}  ({c})")

# them ghi chu: bang nguon da duoc dong bo lai 23/10
old_note = "## GHI CHÚ NHANH"
new_note = """## GHI CHÚ NHANH

> **Mã câu trong bảng này đã đồng bộ lại 23/10/2026** sau khi kịch bản được viết lại (21 lỗi fact + 1 567 từ bổ sung) — mã element/câu đã dịch nên 3 dòng ban đầu trỏ nhầm (`1.09#1` → `1.10#1`, `1.09#10` → `1.10#10`, `1.12#7` → `1.13#7`)."""
assert raw.count(old_note) == 1
raw = raw.replace(old_note, new_note, 1)
print("  OK  them ghi chu dong bo ma cau")

MD.write_text(raw, encoding="utf-8")
print(f"\nDa ghi {MD}")
