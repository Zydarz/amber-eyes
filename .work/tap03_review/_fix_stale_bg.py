#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sửa lỗi tên ảnh không tồn tại trong manifest Tập 03 (B3): `t2_cellar` -> `t2_cell_medical`."""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
MD = ROOT / "02_SAN_XUAT" / "Tap03" / "Danh_Sach_Anh_Tap03.md"
BG = ROOT / "assets" / "bg"

raw = MD.read_text(encoding="utf-8")

# 1. doi ten anh khong ton tai
old = "· `t2_folder_tree` · `t2_cellar`"
new = "· `t2_folder_tree` · `t2_cell_medical`"
assert raw.count(old) == 1, f"khong tim thay '{old}'"
raw = raw.replace(old, new, 1)
print("  OK  t2_cellar -> t2_cell_medical")

# 2. kiem tra moi ten trong danh sach deu co that
import re
line = [l for l in raw.splitlines() if l.startswith("- **Tập 02**:")][0]
names = re.findall(r"`([a-z0-9_]+)`", line)
missing = [n for n in names if not (BG / f"{n}.png").exists()]
print(f"  danh sach Tập 02: {len(names)} ten, thieu: {missing if missing else 'khong co'}")
assert not missing, missing

MD.write_text(raw, encoding="utf-8")
print("Da ghi", MD)
