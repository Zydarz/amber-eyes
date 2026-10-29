#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anh tinh (stills) co khop voi bang shot hien tai khong?

Moi shot duoc 1 khung o giua. Ke hoach A3 buoc 8 / A9.3.
Kiem: anh co nam trong khoang [start, end] cua shot tuong ung khong,
va do lech thoi gian giua moc giua shot va thoi diem thuc cua anh.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(r"D:\TEST\Gax\Audi\.work")
sh = json.loads((W / "shots_t02.json").read_text(encoding="utf-8"))
shots = sh["shots"]
stills = sorted((float(p.stem[1:]), p.name) for p in (W / "video3_t02" / "stills").glob("*.png"))

inside = outside = 0
off = []
for t, name in stills:
    cands = [s for s in shots if s["start"] - 0.35 <= t <= s["end"] + 0.35]
    if cands:
        inside += 1
        mid = (cands[0]["start"] + cands[0]["end"]) / 2
        off.append((round(t - mid, 2), cands[0]["id"], name))
    else:
        outside += 1
        off.append((None, "KHONG THUOC SHOT NAO", name))

print(f"anh tinh: {len(stills)} · shot: {len(shots)}")
print(f"anh nam trong mot shot: {inside} · khong thuoc shot nao: {outside}")
d = [o[0] for o in off if o[0] is not None]
if d:
    d.sort()
    print(f"lech thoi gian giua moc giua shot va anh: min {d[0]} s · max {d[-1]} s · TB {sum(d)/len(d):.2f} s")
big = [o for o in off if o[0] is not None and abs(o[0]) > 3]
print(f"anh lech > 3 s: {len(big)}")
for o in big[:15]:
    print("   ", o)
orph = [o for o in off if o[0] is None]
for o in orph[:10]:
    print("   orphan:", o)
