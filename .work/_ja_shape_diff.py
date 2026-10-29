#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So chuỗi phần tử (kind) của bản VN và bản JA để tìm chỗ cấu trúc lệch.

    py -3 .work/_ja_shape_diff.py 11
"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
import parse_kichban as PK  # noqa: E402

ep = sys.argv[1]
vn = M.canonical_vn(ep)
ja = HERE.parent / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"

ve = PK.parse_file(vn)
je = PK.parse_file(ja)


def brief(e):
    t = (e.get("text") or "").replace("\n", " ")[:90]
    return f"{e['kind']:6s} | {t}"


print(f"VN: {len(ve)} phan tu   JA: {len(je)} phan tu")
i = j = 0
shown = 0
while i < len(ve) and j < len(je) and shown < 40:
    a, b = ve[i], je[j]
    if a["kind"] == b["kind"]:
        i += 1
        j += 1
        continue
    # lệch kind -> in ra cửa sổ để xem
    print(f"\n--- lech tai VN[{i}] JA[{j}]")
    for k in range(max(0, i - 2), min(len(ve), i + 5)):
        print(f"   VN[{k}] {brief(ve[k])}")
    for k in range(max(0, j - 2), min(len(je), j + 5)):
        print(f"   JA[{k}] {brief(je[k])}")
    shown += 1
    i += 1
    j += 1
