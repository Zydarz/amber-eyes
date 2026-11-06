#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
from parse_kichban import parse_file

WANT = {"3.07", "3.08", "3.09", "3.10", "3.11"}
for tag, kb in [("VN", "01_KICH_BAN/Tap05/kichban_tap05_23102026.md"),
                ("EN", "01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md"),
                ("JA", "01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md")]:
    els = parse_file(kb)
    print("=" * 78)
    print(tag)
    for e in els:
        if e["id"] in WANT:
            print(f" EL {e['id']} {e['kind']} role={e.get('role')} dir={e.get('direction')!r}")
            for s in e.get("sentences", []):
                print(f"   {s['id']}: {s['text']}")
