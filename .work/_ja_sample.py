#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rà chất lượng tiếng Nhật: in cặp câu VN/JA ngẫu nhiên để đọc tay.

    py -3 .work/_ja_sample.py 6 12        # 6 câu mẫu từ Tap12
    py -3 .work/_ja_sample.py 4 8 03 07   # nhiều tập
"""
import random
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
from ja_split import split_dialogue_sentences  # noqa: E402

random.seed(20261024)
args = sys.argv[1:]
n = int(args[0]) if args and args[0].isdigit() else 5
eps = args[1:] if args and args[0].isdigit() else args

for ep in eps:
    ja_p = HERE.parent / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not ja_p.exists():
        print(f"Tap{ep}: chưa có file JA")
        continue
    units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    cache = {}
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if cp.exists():
        import json
        cache = json.loads(cp.read_text(encoding="utf-8"))
    pairs = []
    for u in units:
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            if not parts:
                continue
            for k, p in enumerate(parts):
                ja = cache.get(f"{u['id']}#{k}", {}).get("ja", "")
                if ja:
                    pairs.append((p, ja))
    if not pairs:
        print(f"Tap{ep}: không có cặp câu")
        continue
    print(f"\n{'='*70}\nTap{ep} — {len(pairs)} câu, lấy {min(n, len(pairs))} mẫu")
    for vi, ja in random.sample(pairs, min(n, len(pairs))):
        print(f"\n  VN: {vi[:230]}")
        print(f"  JA: {ja[:230]}")
