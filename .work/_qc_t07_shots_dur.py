#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra shots_t07.json: so shot, do dai tung shot, so cau moi thieu."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

sh = json.loads((ROOT / ".work/shots_t07.json").read_text(encoding="utf-8-sig"))
shots = sh["shots"]
print(f"shots_t07.json: {len(shots)} shot · total={sh['total']}")

plan = (ROOT / "02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md").read_text(encoding="utf-8-sig")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
plan_rows = [ln for ln in sec.split("\n") if re.match(r"\|\s*[1-5]-\d+", ln)]
print(f"dong trong bang shot: {len(plan_rows)}")
pid = [re.match(r"^\|\s*([1-5]-\d+)", ln).group(1) for ln in plan_rows]
sid = [s["id"] for s in shots]
print("thieu trong shots.json:", [i for i in pid if i not in sid])
print("thua trong shots.json:", [i for i in sid if i not in pid])

print()
print("=== do dai shot (>15 s = vu H10) ===")
for s in shots:
    d = s["end"] - s["start"]
    flag = "  <-- >15s" if d > 15 else ("  <-- <3s" if d < 3 else "")
    print(f"  {s['id']:>5} {d:6.1f}s  n={len(s['sentences'])}  "
          f"{s['role'] or '-':<3} {s['template'] or '-':<4} {s['bg'][:40]:<40}{flag}")

print()
print("=== timeline cau 5.04 ===")
tl = json.loads((ROOT / ".work/timeline_s_t07.json").read_text(encoding="utf-8-sig"))
for it in tl["items"]:
    if it["id"].startswith("5.04"):
        print(f"  {it['id']:>9} {it['end']-it['start']:6.2f}s  [{it['start']:.2f} → {it['end']:.2f}]")
