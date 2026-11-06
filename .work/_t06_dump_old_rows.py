#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — in cau cu bang shot cu: ID, Cau, Mau, Nen, Nv (de so sanh khoi tao moi)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
t = (ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", t, re.M)
sec = t[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
rows = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
print(f"{len(rows)} dong")
for l in rows:
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    print(f"{c[0]:<6} | {c[1][:34]:<34} | {c[3][:14]:<14} | {c[4][:30]:<30} | {c[7][:16]}")
print()
print("--- dong cuoi (the) ---")
print(rows[-1])
