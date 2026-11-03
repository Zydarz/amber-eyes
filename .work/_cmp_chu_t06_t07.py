#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sanh cot 'Chu' cua Tap06 va Tap07: kiem tra co lay nguyen van tu cau hay la caption."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for tag, p in (("TAP06", r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md"),
               ("TAP07", r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md")):
    t = open(p, encoding="utf-8-sig").read()
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", t, re.M)
    sec = t[m.end():]
    print("=" * 90)
    print(tag)
    print("=" * 90)
    n = 0
    for ln in sec.splitlines():
        if re.match(r"\|\s*[1-5]-\d+", ln):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            c += [""] * (9 - len(c))
            print(f"{c[0]:>5} [{c[3]:<16}] CHU: {c[5][:150]}")
            n += 1
        if n >= 14:
            break
    print()
