#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đếm từ nhạy cảm (danh sách cấm YouTube) xuất hiện trong lời dẫn bản JA,
và cho biết từ tương đương có trong bản VN không."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from _qc_ja import BANNED_JA  # noqa: E402

tot = 0
for i in range(1, 30):
    ep = f"{i:02d}"
    p = M.KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not p.exists():
        continue
    ja = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
    vn = M.canonical_vn(ep).read_text(encoding="utf-8")
    rows = []
    for w, vn_src, safe in BANNED_JA:
        probe = ja
        for s in safe:
            probe = probe.replace(s, "")
        if w not in probe:
            continue
        in_vn = bool(vn_src) and vn_src in vn
        rows.append((w, vn_src, in_vn))
    if rows:
        tot += len(rows)
        print(f"  tap{ep}: " + " · ".join(
            f"{w}({src}{'' if invn else ' ← JA tự thêm'})" for w, src, invn in rows))
print(f"\nTONG: {tot} truong hop")
