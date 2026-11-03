#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sanh: vai that trong script Tap07 + caption 'Tap 06' cua Tap06 + qua tang ke."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

s7 = json.loads((ROOT / ".work/script_tap07.json").read_text(encoding="utf-8-sig"))
print("=== vai thật trong script_tap07.json ===")
seen = {}
for el in s7:
    seen.setdefault((el["id"], el.get("kind"), el.get("role")), 0)
    seen[(el["id"], el.get("kind"), el.get("role"))] += len(el.get("sentences") or [])
for (eid, kind, role), n in seen.items():
    if role != "H":
        print(f"  {eid:<8} kind={kind:<6} role={role!r:<8} n={n}")

print()
print("=== tap07: so lan xuat hien vai ===")
c = {}
for el in s7:
    for x in el.get("sentences") or []:
        c[el.get("role")] = c.get(el.get("role"), 0) + 1
print(" ", c)

print()
print("=== Tap06: dong cuoi (the ket) + chu co 'Tap 06' ===")
t6 = (ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md").read_text(encoding="utf-8-sig")
rows6 = []
for ln in t6.split("\n"):
    if re.match(r"^\|\s*[1-5]-\d+\s*\|", ln):
        cc = [x.strip() for x in ln.strip().strip("|").split("|")]
        cc += [""] * (9 - len(cc))
        rows6.append(cc)
for cc in rows6[-3:]:
    print(f"  {cc[0]} | cau={cc[1]} | chu={cc[5][:130]}")
print("  so dong co chua 'Tap 06':")
for cc in rows6:
    if re.search(r"Tập\s*06|TAP\s*06", cc[5]):
        print(f"    {cc[0]} | cau={cc[1]} | chu={cc[5][:110]}")

print()
print("=== Tap07: dong cuoi ===")
t7 = (ROOT / "02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md").read_text(encoding="utf-8-sig")
rows7 = []
for ln in t7.split("\n"):
    if re.match(r"^\|\s*[1-5]-\d+\s*\|", ln):
        cc = [x.strip() for x in ln.strip().strip("|").split("|")]
        cc += [""] * (9 - len(cc))
        rows7.append(cc)
for cc in rows7:
    if re.search(r"Tập\s*07|TẬP\s*07", cc[5]):
        print(f"  {cc[0]} | cau={cc[1]} | chu={cc[5][:130]}")

print()
print("=== Tap06: chu chua 'Tap 05/06/07' bat ky ===")
for cc in rows6:
    for m in re.findall(r"Tập\s*\d+", cc[5]):
        print(f"  {cc[0]} | {m} | cau={cc[1]}")
