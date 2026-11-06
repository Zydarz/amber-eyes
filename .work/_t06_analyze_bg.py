#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — phan tich nen: biet nen t6_ nao CHUA dung trong bang shot cu."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
BT = chr(96)

allbg = {p.stem for p in (ROOT / "assets/bg").glob("t6_*.png")}
t = (ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md").read_text(encoding="utf-8")
used = set(re.findall(BT + r"(t6_[a-z0-9_]+)" + BT, t))

print(f"nen t6_ tong: {len(allbg)} · da dung trong bang shot cu: {len(used)}")
print("\nCHUA DUNG (ung vien cho noi dung moi):")
for b in sorted(allbg - used):
    print("   ", b)
print("\nNen chung (khong t6_) co the dung them:")
for b in sorted(p.stem for p in (ROOT / "assets/bg").glob("*.png")
                if not p.stem.startswith("t")):
    print("   ", b)
