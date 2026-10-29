#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thống kê: bao nhiêu dòng thoại tách được thành câu, bao nhiêu rơi về chế độ 'line'."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

total_line = 0
total_units = 0
fallback = []
for i in range(1, 30):
    ep = f"{i:02d}"
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    n_line = 0
    n_sent = 0
    for u in units:
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            total_units += 1
            parts = M.splittable(u)
            if parts:
                n_sent += len(parts)
            else:
                n_line += 1
                fallback.append((ep, u["id"], u.get("n", 0), u["vi"][:90]))
    total_line += n_line
    print(f"Tap{ep}: câu tách riêng={n_sent:4d} · dòng dịch-cả-dòng={n_line:3d}")

print(f"\nTỔNG: {total_units} dòng thoại · {total_line} rơi về 'line' "
      f"({total_line * 100 // max(total_units,1)}%)")
print(f"\n--- {len(fallback)} dòng rơi về 'line' ---")
for ep, uid, n, vi in fallback:
    print(f"  Tap{ep} {uid} n={n} :: {vi}")
