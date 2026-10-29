#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo tác động bản vá 'cho phép tách câu khi marker cân bằng ở mức DÒNG'.

Cũ: splittable() từ chối nếu parts_balanced() sai (marker mở ở câu này, đóng ở câu sau).
Mới: cho phép, vì parse_kichban xoá ** và * TRƯỚC khi tách câu => marker bọc cả dòng
     vẫn cho đúng số câu, miễn là tổng số marker trên dòng cân bằng.

    py -3 .work/_ja_patch_impact.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
from ja_split import split_dialogue_sentences, parts_balanced  # noqa: E402


def markers_balanced(line: str) -> bool:
    """Tổng số ** và * trên dòng có cân bằng không (theo kiểu đếm của check_sentence)."""
    if line.count("**") % 2:
        return False
    if (line.count("*") - line.count("**")) % 2:
        return False
    return True


tot_line = 0
tot_flip = 0
for i in range(1, 30):
    ep = "%02d" % i
    try:
        units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
    except Exception as e:
        print(ep, "LOI", e)
        continue
    flips = []
    for u in units:
        if u["kind"] not in ("TEXT", "BULLET"):
            continue
        parts = split_dialogue_sentences(u["vi"])
        if not parts or len(parts) != u.get("n", 0):
            continue                     # vẫn không tách được -> giữ nguyên line mode
        if parts_balanced(parts):
            continue                     # đã tách được sẵn
        if not markers_balanced(u["vi"]):
            continue                     # tổng marker lệch -> KHÔNG cho phép
        flips.append((u["id"], len(parts), u["vi"][:90]))
    if flips:
        tot_line += sum(1 for u in units if u["kind"] in ("TEXT", "BULLET")
                        and (split_dialogue_sentences(u["vi"]) is None
                             or len(split_dialogue_sentences(u["vi"])) != u.get("n", 0)))
        tot_flip += len(flips)
        print(f"Tap{ep}: {len(flips)} dòng sẽ chuyển line -> dialogue")
        for uid, n, vi in flips:
            print(f"    {uid}  n={n}  {vi}")
print(f"\nTONG: {tot_flip} dòng chuyển chế độ (toàn bộ 29 tập)")
