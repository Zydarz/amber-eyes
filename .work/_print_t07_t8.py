#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In text 4.02, 5.04#1-4, 5.04#11-15 + caption T8 trong bang shot Tap07."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

s = json.loads((ROOT / ".work/script_tap07.json").read_text(encoding="utf-8-sig"))
for el in s:
    if el["id"] in ("4.02", "1.06"):
        for x in el.get("sentences", []):
            print(f"{x['id']:>8} [{el.get('role','?'):>3}] {x['text']}")
        print()

print("=== caption T8 trong bang shot ===")
plan = (ROOT / "02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md").read_text(encoding="utf-8-sig")
for ln in plan.split("\n"):
    if re.match(r"^\|\s*(5-0[4-8])\s*\|", ln):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        c += [""] * (9 - len(c))
        print(f"{c[0]} | cau={c[1]} | mau={c[3]}")
        print(f"   chu: {c[5]}")
        print(f"   nen: {c[4]}")
