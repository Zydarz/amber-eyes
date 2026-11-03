#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In noi dung cac element yeu cau de chon nen khop loi (H3)."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

S = json.loads(open(r"D:/TEST/Gax/amber-eyes/.work/script_tap07.json",
                    encoding="utf-8-sig").read())
WANT = ["1.09", "1.11", "1.12", "1.13", "2.02", "2.03", "2.08", "3.02", "3.04",
        "4.10", "5.02", "5.03", "5.04"]
for el in S:
    if el["id"] in WANT:
        for x in el.get("sentences", []):
            print(f"{x['id']:>8} [{el.get('role','?'):>3}] {x['text']}")
        print()
