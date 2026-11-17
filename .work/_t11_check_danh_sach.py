#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đối chiếu Danh_Sach_Anh_Tap11.md với bảng shot thực tế + file trên đĩa."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "02_SAN_XUAT" / "Tap11" / "Danh_Sach_Anh_Tap11.md"

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
text = DOC.read_text(encoding="utf-8")

# 1) mã nền nằm trong doc
codes = set(re.findall(r"\bt11_[a-z0-9_]+\b", text))
print(f"1) doc nhac toi {len(codes)} ma nen")

# 2) ma nen thuc su dung trong bang shot VI
sh = json.loads((ROOT / ".work" / "shots_t11.json").read_text(encoding="utf-8"))["shots"]
used = {s["bg"] for s in sh if s["bg"].startswith("t11_")}
print(f"2) bang shot VI dung {len(used)} ma nen")
print(f"   thieu trong doc: {sorted(used - codes)}")
print(f"   thua trong doc : {sorted(codes - used)}")

# 3) file tren dia
ondisk = {p.stem for p in (ROOT / "assets" / "bg").glob("t11_*.png")}
print(f"3) tren dia {len(ondisk)} file")
print(f"   nen tren dia khong co trong bang shot: {sorted(ondisk - used)}")

# 4) dong dau tieu
for line in text.split("\n")[:12]:
    if line.strip():
        print("   |", line.strip()[:150])
