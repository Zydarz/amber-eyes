#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In ra nội dung VN của các mục đang lỗi (để thiết kế cách sửa).

    py -3 .work/_ja_bad_dump.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
from ja_split import split_dialogue_sentences  # noqa: E402

BAD = {
    "01": ["u0067#2", "u0074#1"],
    "04": ["u0191#0"],
    "05": ["u0008", "u0170#L"],
    "07": ["u0010"],
    "08": ["u0038"],
    "10": ["u0070"],
    "11": ["u0010", "u0060"],
    "15": ["u0009"],
    "17": ["u0009"],
    "18": ["u0009"],
    "20": ["u0233#0"],
}

for ep, keys in BAD.items():
    units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
    byid = {u["id"]: u for u in units}
    print(f"\n############ Tap{ep}")
    for k in keys:
        uid, _, sub = k.partition("#")
        u = byid.get(uid)
        if not u:
            print(f"  {k}: KHÔNG THẤY unit")
            continue
        print(f"\n  --- {k}  kind={u['kind']} n={u.get('n')}")
        if sub == "L":
            print(f"      VI(Line): {u['vi'][:700]}")
        elif sub.isdigit() and u["kind"] in ("TEXT", "BULLET"):
            parts = split_dialogue_sentences(u["vi"])
            print(f"      VI(part): {parts[int(sub)][:700]}")
        else:
            print(f"      VI: {u['vi'][:700]}")
