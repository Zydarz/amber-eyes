#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm chứng bộ tách câu trên toàn bộ 29 kịch bản."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M
from ja_split import split_dialogue_sentences

bad, total, nmark = [], 0, 0
for i in range(1, 30):
    ep = f"{i:02d}"
    units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    for u in units:
        if u["kind"] not in ("TEXT", "BULLET") or u["id"] not in in_turn:
            continue
        total += 1
        v = u["vi"]
        if "*" in v:
            nmark += 1
        parts = split_dialogue_sentences(v)
        if parts is None or len(parts) != u.get("n", 0):
            bad.append((ep, u["id"], u["kind"], u.get("n"),
                        len(parts) if parts else 0, v[:170], parts))

print(f"dòng thoại: {total} (có marker: {nmark}) · LỆCH: {len(bad)}")
for ep, uid, k, n, m, v, parts in bad[:20]:
    print(f"\n[{ep} {uid}] {k} n={n} tách ra {m}")
    print("  VI:", v)
    print("  parts:", parts)
sys.exit(1 if bad else 0)
