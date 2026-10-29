#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đối chiếu bộ đếm câu của pipeline JA với parser chính (parse_kichban.py)."""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

WORK = Path(__file__).parent
OUT = WORK / "_ja_count_cmp.txt"
lines, bad = [], 0

for i in range(1, 30):
    ep = f"{i:02d}"
    src = M.canonical_vn(ep)
    out = WORK / f"_ja_parse_{ep}.json"
    subprocess.run([sys.executable, str(WORK / "parse_kichban.py"), str(src), str(out)],
                   check=True, capture_output=True)
    els = json.loads(out.read_text(encoding="utf-8"))
    official = sum(len(e["sentences"]) for e in els if e["kind"] == "LOI")
    turns = sum(1 for e in els if e["kind"] == "LOI")

    units = M.assign_turn_counts(M.parse_units(src))
    mine = 0
    n_text = 0
    for u in units:
        if u.get("n", 0):
            mine += u["n"]
            n_text += 1
    role_like = sum(1 for u in units if u["kind"] == "TEXT" and u["vi"].startswith("**"))
    d = mine - official
    flag = "OK " if d == 0 else "LECH"
    if d:
        bad += 1
    lines.append(f"{flag} Tap{ep} | parser={official} câu ({turns} lượt) | JA-dem={mine} | "
                 f"dòng thoại={n_text} | dòng giống-vai={role_like} | lệch={d}")
    out.unlink()

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"{29 - bad}/29 tập khớp · -> {OUT}")
