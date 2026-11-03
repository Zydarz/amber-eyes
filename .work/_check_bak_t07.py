#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra ban luu co dung ban goc (62 dong) truocc khi khoi phuc."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BAK = Path(r"D:/TEST/Gax/amber-eyes/.work/_cu/t07_shottable_147cu/KeHoach_Video_Tap07.md.bak")
t = BAK.read_text(encoding="utf-8-sig")
rows = [ln for ln in t.split("\n") if re.match(r"^\|\s*[1-5]-\d+\s*\|", ln)]
ids = [re.match(r"^\|\s*([1-5]-\d+)", ln).group(1) for ln in rows]
print(f"ban luu: {len(rows)} dong · id dau {ids[0]} · id cuoi {ids[-1]}")
print("co dong 1-15?", "1-15" in ids, "(khong co = ban goc 62 dong)")
print("co '147 cau' trong header?", "147 câu thoại" in t)
