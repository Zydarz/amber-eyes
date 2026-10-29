#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem tiêu đề HỒI (ACT) của bản VN + tìm dòng tương ứng với lỗi."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

for ep in sys.argv[1:]:
    p = M.canonical_vn(ep)
    print(f"\n### Tap{ep}  <- {p.name}")
    for i, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        s = l.strip()
        if s.startswith("## "):
            print(f"  {i:4d}| {s[:200]}")
        if ep == "06" and ("mặt hề" in s or "mặt nạ" in s or "hề" in s):
            print(f"  {i:4d}| {s[:300]}")
