#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — in cot 'Chu' cu bang shot cu (mau chu tren hinh) de doi chieu van phong."""
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
for l in rows:
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    print(f"{c[0]} :: {c[5]}")
