#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tìm vị trí của anchor (tiền tố 5-8 ký tự) trong chuỗi thực, rồi in ra
đoạn thực tế kèm codepoint để chép đúng rule."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).parent

CASES = [
    ("18", "u0255#0", "暗い存在として見"),
    ("22", "u0276#0", "次の사건"),
    ("25", "u0030#0", "GROUND"),
    ("25", "u0252#0", "常に自分"),
    ("29", "u0060#0", "衝撃的사건"),
    ("29", "u0063#0", "强烈な化学薬品"),
]

for ep, key, anchor in CASES:
    d = json.loads((HERE / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
    ja = d[key]["ja"]
    i = ja.find(anchor)
    if i < 0:
        # thử tìm bằng anchor không có phần Hangul
        a2 = anchor.split("사")[0].split("G")[0][:4]
        i = ja.find(a2)
        print(f"=== Tap{ep} {key}: anchor '{anchor}' KHONG co; fallback '{a2}' tai {i}")
        if i < 0:
            print("   ja =", repr(ja))
            print()
            continue
    seg = ja[i:i + 34]
    print(f"=== Tap{ep} {key}  anchor tai {i}")
    print("   seg:", " ".join(f"{c}(U+{ord(c):04X})" for c in seg))
    print("   txt:", seg)
    print()
