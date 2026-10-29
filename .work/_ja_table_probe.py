#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem các dòng bảng (TABLE) và số ô của chúng trong bản VN."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

for ep in (sys.argv[1:] or ["01"]):
    units = M.parse_units(M.canonical_vn(ep))
    print(f"\n===== Tap{ep}: các dòng bảng =====")
    for u in units:
        if u["kind"] != "TABLE":
            continue
        cells = u["vi"].split("\t")
        print(f"  {u['id']}: {len(cells)} ô")
        for c in cells:
            print(f"      | {c[:90]}")
