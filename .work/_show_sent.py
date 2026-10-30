#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In noi dung cac cau theo mo can kiem, de doi chieu voi anh nen."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
els = {e["id"]: e for e in json.loads(
    Path(__file__).resolve().parents[1] / ".work" / "script_tap03.json".read_text(encoding="utf-8"))}

WANT = ["1.10", "2.07", "3.05", "4.02", "5.02", "1.13", "1.03"]
for eid in WANT:
    e = els.get(eid)
    if not e:
        continue
    print(f"\n===== {eid} (vai {e['role']}, {len(e['sentences'])} cau) =====")
    for s in e["sentences"]:
        print(f"  {s['id']}: {s['text']}")
