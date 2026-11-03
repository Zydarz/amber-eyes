#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In từng câu CŨ (165) và MỚI (154) của 11 element đổi số câu, để map theo NỘI DUNG."""
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OLD = Path(r"D:/TEST/Gax/amber-eyes/.work/_cu/t06_OLD165/script_tap06_OLD165.json")
NEW = Path(r"D:/TEST/Gax/amber-eyes/.work/script_tap06.json")

CHANGED = ["1.06", "1.08", "1.09", "1.14", "3.05", "3.07",
           "3.09", "3.10", "4.08", "5.02", "5.04"]


def flat(p):
    d, o = {}, []
    for el in json.loads(Path(p).read_text(encoding="utf-8-sig")):
        for i, x in enumerate(el.get("sentences") or [], 1):
            sid = f"{el['id']}#{i}"
            d[sid] = (el.get("role") or x.get("role") or "?",
                      (x.get("text") or "").strip())
            o.append(sid)
    return d, o


od, oo = flat(OLD)
nd, no = flat(NEW)

for e in CHANGED:
    print(f"\n{'='*100}\nELEMENT {e}\n{'='*100}")
    print("--- CU (165) ---")
    for s in oo:
        if s.startswith(e + "#"):
            r, t = od[s]
            print(f"  {s:8s} [{r:2s}] {t}")
    print("--- MOI (154) ---")
    for s in no:
        if s.startswith(e + "#"):
            r, t = nd[s]
            print(f"  {s:8s} [{r:2s}] {t}")
