#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In câu theo câu của các element cần neo (mốc) cho bảng âm thanh Tập 03."""
import json

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
els = json.load(open(p, encoding="utf-8"))
byid = {e["id"]: e for e in els}

want = ["1.03", "1.05", "1.07", "1.10", "1.12", "2.02", "2.04", "2.06", "2.07",
        "2.08", "2.09", "3.02", "3.04", "3.05", "3.07", "3.08", "3.10", "3.11",
        "4.02", "4.04", "4.05", "4.07", "4.08", "5.02", "5.04", "5.05", "5.06",
        "5.08", "5.10"]

for i in want:
    e = byid.get(i)
    if not e:
        continue
    print(f"\n--- {i} [{e['kind']} {e.get('role','')}] ---")
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            print(f"  {s['id']:<9} {s['text'][:118]}")
    else:
        print(f"  {e.get('desc','')[:160]}")
