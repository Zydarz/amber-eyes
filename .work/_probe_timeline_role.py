#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra vai trong timeline Tap07 + script tao timeline + srt."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

tl = json.loads((ROOT / ".work/timeline_s_t07.json").read_text(encoding="utf-8-sig"))
roles = {}
for it in tl["items"]:
    roles.setdefault(it["role"], []).append(it["id"])
print("vai trong timeline:")
for r, ids in roles.items():
    print(f"  {r!r}: {len(ids)} cau · {ids[0]} .. {ids[-1]}")

print()
print("=== file .work co 'timeline' ===")
for p in sorted((ROOT / ".work").glob("*timeline*")):
    print("  ", p.name, p.stat().st_size)

print()
print("=== script tao timeline: dong 'role' ===")
for p in sorted((ROOT / ".work").glob("*timeline*.py")):
    for i, ln in enumerate(p.read_text(encoding="utf-8-sig", errors="replace").split("\n"), 1):
        if "role" in ln and ("N_ELEMENT" in ln or "n_element" in ln or "get(" in ln):
            print(f"  {p.name}:{i}: {ln.strip()}")

print()
print("=== srt hien tai (2 cue dau) ===")
srt = (ROOT / "02_SAN_XUAT/Tap07/xuat_ban/Tap07.srt").read_text(encoding="utf-8-sig")
print("\n".join(srt.split("\n")[:12]))
blocks = [b for b in srt.strip().split("\n\n")]
print("so cue:", len(blocks))
print("cue cuoi:")
print(blocks[-1])
