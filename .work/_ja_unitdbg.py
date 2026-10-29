#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem chi tiết unit: kind, vi, prefix cho các dòng rơi về chế độ 'line'."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

targets = {("02", "u0181"), ("02", "u0187"), ("04", "u0084"), ("04", "u0172"),
           ("05", "u0170")}
for i in range(1, 30):
    ep = f"{i:02d}"
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    for u in units:
        if (ep, u["id"]) in targets:
            print(f"Tap{ep} {u['id']} kind={u['kind']} prefix={u.get('prefix')!r} "
                  f"n={u.get('n')} quote_lead={u.get('quote_lead')}")
            print(f"   vi  = {u['vi']!r}")
            print(f"   note= {u['note']}")
            print()
