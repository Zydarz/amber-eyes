# -*- coding: utf-8 -*-
"""Tập 12 — in bảng shot (sid, câu, mã nền) để kiểm tra ánh xạ."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PAT = re.compile(r"`(t\d+_[a-z0-9_]+)`")
CAU = re.compile(r"`([^`]+)`")

rows = []
for line in open("02_SAN_XUAT/Tap12/KeHoach_Video_Tap12.md", encoding="utf-8"):
    m = re.match(r"^\|\s*([1-5]-\d+)\s*\|(.*)$", line.rstrip())
    if not m:
        continue
    c = [x.strip() for x in m.group(2).split("|")]
    bg = PAT.search(c[3] if len(c) > 3 else "")
    cau = CAU.search(c[0])
    rows.append((m.group(1), cau.group(1) if cau else c[0], bg.group(1) if bg else c[3]))

pref = sys.argv[1] if len(sys.argv) > 1 else ""
for r in rows:
    if r[1].startswith(pref) or pref == "all":
        print(f"{r[0]:6s} {r[1]:10s} {r[2]}")
