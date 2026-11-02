#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lay dong bang shot cua plan VN (de dich lai chu tren hinh sang JA hien hanh)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

lines = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8-sig").splitlines()
i0 = next(i for i, l in enumerate(lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(lines) if i > i0 and l.startswith("**Tổng:"))
IDS = ["1-24", "1-25", "1-28", "2-11", "2-17", "3-02", "3-09", "3-13", "3-20", "3-21",
       "3-25", "3-27", "3-28", "4-08", "4-12", "4-13", "4-14", "4-15", "5-08", "5-10", "5-24"]
for l in lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if m and m.group(1) in IDS:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        print(f"== {c[0]} | cau {c[1]} | vai {c[2]} | mau {c[3]} | nen {c[4]}")
        print(f"   CHU  : {c[5]}")
        print(f"   BEAT : {c[6]}")
        print(f"   GHI  : {c[7]}")
        print()
