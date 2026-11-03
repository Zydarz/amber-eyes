#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In 3 dong cuoi cua Tap06 (mau the ket) + bang mau phuc vu + timeline total."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

for tag, f in (("TAP06", "Tap06"), ("TAP07", "Tap07")):
    p = ROOT / "02_SAN_XUAT" / f / f"KeHoach_Video_{f}.md"
    t = p.read_text(encoding="utf-8-sig")
    rows = []
    for ln in t.split("\n"):
        if re.match(r"^\|\s*[1-5]-\d+\s*\|", ln):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            c += [""] * (9 - len(c))
            rows.append(c)
    print("=" * 100)
    print(tag, f"({len(rows)} dong)")
    for c in rows[-3:]:
        print(f"  {c[0]:>5} | cau={c[1]:<24} | vai={c[2]:<3} | mau={c[3]:<14} | nen={c[4][:44]:<44}")
        print(f"         chu={c[5][:120]}")
        print(f"         beat={c[6][:60]} | nv={c[7]} | tr={c[8]}")

print()
print("=== timeline_s_t07.json ===")
tl = json.loads((ROOT / ".work/timeline_s_t07.json").read_text(encoding="utf-8-sig"))
print("total:", tl["total"], "| items:", len(tl["items"]), "| markers:", len(tl["markers"]))
print("item0:", json.dumps(tl["items"][0], ensure_ascii=False))
print("item-1:", json.dumps(tl["items"][-1], ensure_ascii=False))
print("markers:", [m.get("id") for m in tl["markers"]])

print()
print("=== acting_tap07.json: vai/giong theo element ===")
ac = json.loads((ROOT / ".work/acting_tap07.json").read_text(encoding="utf-8-sig"))
if isinstance(ac, dict):
    for k, v in list(ac.items())[:4]:
        print(f"  {k}: {json.dumps(v, ensure_ascii=False)[:300]}")
    keys = list(ac.keys())
else:
    keys = []
for el in ("1.07#1", "1.07#5", "4.03#1", "4.03#3", "1.10#1", "1.12#1"):
    if isinstance(ac, dict) and el in ac:
        print(f"  {el}: {json.dumps(ac[el], ensure_ascii=False)[:260]}")
