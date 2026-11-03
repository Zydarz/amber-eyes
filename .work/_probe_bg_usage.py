#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anh nen nao CHUA dung trong bang shot Tap07 (de chon cho shot tach moi)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

plan = (ROOT / "02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md").read_text(encoding="utf-8-sig")
used = {}
for ln in plan.split("\n"):
    m = re.match(r"^\|\s*([1-5]-\d+)\s*\|", ln)
    if not m:
        continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    c += [""] * (9 - len(c))
    bgs = re.findall(r"`(t7_[^`]+)`", c[4])
    for b in bgs:
        used.setdefault(b, []).append(c[0])

allbg = {p.stem for p in (ROOT / "assets/bg").glob("t7_*.png")}
print(f"nen co tren dia: {len(allbg)} · nen dung trong bang: {len(used)}")
print()
print("=== NEN CHUA DUNG ===")
for b in sorted(allbg - set(used)):
    print("  ", b)
print()
print("=== NEN DUNG >1 LAN ===")
for b, ids in sorted(used.items()):
    if len(ids) > 1:
        print(f"  {b}: {ids}")
print()
print("=== dem lien tiep theo nen ===")
seq = []
for ln in plan.split("\n"):
    m = re.match(r"^\|\s*([1-5]-\d+)\s*\|", ln)
    if not m:
        continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    c += [""] * (9 - len(c))
    bgs = re.findall(r"`(t7_[^`]+)`", c[4])
    seq.append((c[0], bgs[0] if bgs else None))
run, prev = 1, None
for sid, b in seq:
    if b == prev:
        run += 1
    else:
        if run > 1:
            print(f"  {prev}: {run} shot lien tiep")
        run, prev = 1, b
if run > 1:
    print(f"  {prev}: {run} shot lien tiep")
