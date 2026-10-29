#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đếm số theo quy ước châu Âu trong bản VN (1.600 = 1600, 0,13 = 0.13)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

THOU = re.compile(r"\d{1,3}(?:\.\d{3})+")
DEC = re.compile(r"\d+,\d+")
tot = 0
for i in range(1, 30):
    ep = f"{i:02d}"
    vn = M.canonical_vn(ep).read_text(encoding="utf-8")
    th = set(THOU.findall(vn))
    de = set(DEC.findall(vn))
    if th or de:
        tot += len(th) + len(de)
        print(f"  tap{ep}: ngan {sorted(th)[:6]} · thap phan {sorted(de)[:6]}")
print(f"\nTONG: {tot} so theo quy uoc Chau Au trong 29 tap")
