#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phân tích hình dạng 29 kịch bản VN: dòng thoại có bao nhiêu câu, có ** không, kết thúc bằng gì."""
import re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M

cnt = Counter()
examples = {}
for i in range(1, 30):
    ep = f"{i:02d}"
    units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    for u in units:
        if u["kind"] == "RAW":
            continue
        if u["kind"] in ("TEXT", "BULLET", "LABELED") and u["id"] in in_turn:
            v = u["vi"]
            has_mark = ("**" in v) or ("*" in v)
            ends_colon = v.rstrip().endswith(":")
            ends_dash = v.rstrip().endswith("–") or v.rstrip().endswith("-")
            n = u.get("n", 0)
            parts = M.split_sentences(v)
            key = (u["kind"], n, "mark" if has_mark else "-",
                   "colon" if ends_colon else ("dash" if ends_dash else "-"))
            cnt[key] += 1
            examples.setdefault(key, (ep, u["id"], v[:150], parts))
        else:
            cnt[(u["kind"], "-", "-", "-")] += 1

for k in sorted(cnt, key=lambda x: (str(x[0]), str(x[1]))):
    print(f"{str(k):60s} {cnt[k]}")

print("\n=== VÍ DỤ ===")
for k, (ep, uid, v, parts) in sorted(examples.items(), key=lambda x: str(x[0])):
    if k[0] in ("TEXT", "BULLET", "LABELED"):
        print(f"\n{k}  [{ep} {uid}]")
        print("  VI:", v)
        print("  parts:", parts)
