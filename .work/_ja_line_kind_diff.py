#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So chuỗi PHÂN LOẠI DÒNG (H1/H2/CUE/PAUSE/TEXT/BULLET/LINE) giữa VN và JA.

    py -3 .work/_ja_line_kind_diff.py 11
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

SKIP_PREFIX = ("**原文:**", "**Translated from:**", "**事実・法務チェック:**",
               "**Fact and legal review:**", "**원본:**", "**사실 및 법률 검토:**")


def cats(path):
    out = []
    for n, ln in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        s = ln.strip()
        if not s or s.startswith("<!--"):
            continue
        if s.startswith(SKIP_PREFIX):
            continue
        if s.startswith("## "):
            k = "H2"
        elif s.startswith("# "):
            k = "H1"
        elif re.match(r"^\*\*\[(SFX|BGM)\]:\*\*", s):
            k = "CUE"
        elif re.match(r"^\*\*\[(Nghỉ|Pause|정지|休止)", s):
            k = "PAUSE"
        elif re.match(r"^\*\*[^*]+\*\*", s):
            k = "TEXT"
        elif re.match(r"^[-*]\s+", s):
            k = "BULLET"
        elif s.startswith("|"):
            k = "TABLE"
        else:
            k = "LINE"
        out.append((n, k, s))
    return out


ep = sys.argv[1]
vn = M.canonical_vn(ep)
ja = HERE.parent / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
a, b = cats(vn), cats(ja)
print(f"VN {len(a)} dong · JA {len(b)} dong")

import difflib
sm = difflib.SequenceMatcher(a=[x[1] for x in a], b=[x[1] for x in b])
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    print(f"\n=== {tag}: VN[{i1}:{i2}] vs JA[{j1}:{j2}]")
    for k in range(i1, min(i2, i1 + 8)):
        print(f"   VN  d{k+1:4d} [{a[k][1]}] {a[k][2][:110]}")
    for k in range(j1, min(j2, j1 + 8)):
        print(f"   JA  d{k+1:4d} [{b[k][1]}] {b[k][2][:110]}")
