#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit caption 73 shot: doi chieu CHU TREN HINH voi CAU trong kich ban.
In: shot | caption | cac cau phu | trich danh (neu co)
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

data = json.loads((ROOT / ".work/script_tap06.json").read_text(encoding="utf-8-sig"))
S = {s["id"]: s["text"] for el in data if el.get("kind") == "LOI"
     for s in el.get("sentences", [])}

plan = (ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md").read_text(encoding="utf-8-sig")
rows = []
for L in plan.splitlines():
    if not L.startswith("| ") or "|" not in L:
        continue
    c = [x.strip() for x in L.split("|")]
    if len(c) < 6:
        continue
    m = re.match(r"^(\d+-\d+)$", c[1])
    if not m:
        continue
    rows.append((m.group(1), c[3], c[6] if len(c) > 6 else ""))

print(f"so shot: {len(rows)}\n")
for sid, vai, cap in rows:
    ids = re.findall(r"`([^`]+)`", cap)
    cap_txt = re.sub(r"`[^`]+`", "", cap).strip()
    sents = []
    for i in ids:
        if i in S:
            sents.append(f"{i}: {S[i]}")
        else:
            for a, b in re.findall(r"(`?[0-9.]+#\d+`?)", cap):
                pass
    print(f"[{sid}] {cap_txt}")
    for s in sents:
        print(f"      {s[:250]}")
    print()
