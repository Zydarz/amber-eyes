#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chẩn đoán các mục cache '#L' (dòng nhiều câu): JA còn đủ số câu không?

    py -3 .work/_ja_line_diag.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from ja_split import ja_sentences  # noqa: E402

CACHE = HERE / "ja_cache"
VN = HERE.parent / "01_KICH_BAN"

tot = 0
trunc = 0
for p in sorted(CACHE.glob("tap*.json")):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        continue
    bad = [k for k in d if isinstance(k, str) and k.endswith("#L")]
    if not bad:
        continue
    print(f"\n=== {p.name} ===")
    for k in bad:
        ja = d[k].get("ja", "")
        ns = ja_sentences(ja)
        if isinstance(ns, list):
            ns = len(ns)
        tot += 1
        flag = ""
        if ns <= 1:
            flag = "  <<< CÓ KHẢ NĂNG BỊ RÚT CÒN 1 CÂU"
            trunc += 1
        print(f"  {k}: JA có {ns} câu{flag}")
        print(f"     JA: {ja[:160]}")
print(f"\nTổng {tot} mục #L · nghi rút còn 1 câu: {trunc}")
