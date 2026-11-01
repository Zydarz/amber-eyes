#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So shot cu (25/10, audio MiniMax) vs shot moi (31/10, audio Higgs) — canh bao nhip."""
import json
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parents[1] / ".work"
old = json.loads((WORK / "_cu" / sys.argv[1]).read_text(encoding="utf-8-sig"))
new = json.loads((WORK / "shots_EN_t02.json").read_text(encoding="utf-8-sig"))
O = {s["id"]: s for s in old["shots"]}
N = {s["id"]: s for s in new["shots"]}

print(f"OLD total {old['total']:.1f}s  ({len(old['shots'])} shot)")
print(f"NEW total {new['total']:.1f}s  ({len(new['shots'])} shot)")
print()
print("--- SHOT DAU/CHUOT DOC KHAC (|delta| > 0.5s) ---")
rows = []
for sid, n in N.items():
    o = O.get(sid)
    if not o:
        print(f"  {sid}: MOI")
        continue
    do, dn = o["end"] - o["start"], n["end"] - n["start"]
    if abs(dn - do) > 0.5:
        rows.append((dn - do, sid, do, dn))
for d, sid, do, dn in sorted(rows, key=lambda r: -abs(r[0])):
    print(f"  {sid:<6} {do:6.1f}s -> {dn:6.1f}s   ({d:+6.1f}s)")
print(f"  ... tong {len(rows)} shot thay doi")

print()
print("--- VI PHAM H10 (shot ngoai 3..15s) ---")
for label, D in (("OLD", O), ("NEW", N)):
    bad = sorted(((s["end"] - s["start"], s["id"]) for s in D.values()))
    under = [(d, i) for d, i in bad if d < 3.0]
    over = [(d, i) for d, i in bad if d > 15.0]
    print(f"  {label}: {len(under)} shot < 3s · {len(over)} shot > 15s")
    for d, i in over:
        print(f"      > 15s : {i}  {d:.1f}s   sentences={N[i]['sentences'][:3]}"
              f"{'...' if len(N[i]['sentences'])>3 else ''}  template={N[i]['template']}")
    if label == "NEW":
        print("      < 3s (danh sach):", ", ".join(f"{i}:{d:.1f}" for d, i in under))

print()
print("--- COT TEXT / SEGS thay doi giua cu va moi? ---")
diff = [sid for sid in N if sid in O and
        (O[sid].get("segments") != N[sid].get("segments") or
         O[sid].get("template") != N[sid].get("template") or
         O[sid].get("bg") != N[sid].get("bg") or
         O[sid].get("beats") != N[sid].get("beats") or
         O[sid].get("role") != N[sid].get("role"))]
print("  khac:", diff or "KHONG — noi dung shot giong het cu (chi doi thoi luong)")

print()
print("--- SHOT 3-01 chi tiet ---")
for label, D in (("OLD", O), ("NEW", N)):
    s = D["3-01"]
    print(f"  {label}: {s['start']:.2f} -> {s['end']:.2f}  ({s['end']-s['start']:.1f}s)")
    print(f"        sentences={s['sentences']}")
    print(f"        template={s['template']} bg={s['bg']} role={s['role']}")
    print(f"        segments={s['segments']}")
