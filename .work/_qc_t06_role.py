#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So VAI: script CU (165) vs script MOI (154) va bang shot hien tai."""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
PLAN = ROOT / "02_SAN_XUAT" / "Tap06" / "KeHoach_Video_Tap06.md"


def load(p):
    d = json.loads(Path(p).read_text(encoding="utf-8-sig"))
    out = {}
    for el in d:
        out[el["id"]] = (el.get("role") or "?", len(el.get("sentences") or []))
    return out


old = load(WORK / "_cu" / "t06_OLD165" / "script_tap06_OLD165.json")
new = load(WORK / "script_tap06.json")

print("=== VAI DOI GIUA CU VA MOI ===")
changed = []
for e in sorted(set(old) | set(new), key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]))):
    o, n = old.get(e), new.get(e)
    if o and n and o[0] != n[0]:
        changed.append((e, o, n))
        print(f"  {e}: {o[0]} -> {n[0]}   (so cau {o[1]} -> {n[1]})")
if not changed:
    print("  (khong doi)")

# ---- bang shot hien tai: vai theo tung dong
rows = []
for ln in PLAN.read_text(encoding="utf-8-sig").splitlines():
    m = re.match(r"^\|\s*([1-5]-\d+)\s*\|", ln.strip())
    if m:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)

print(f"\n=== VAI TUNG DONG SHOT vs SCRIPT ({len(rows)} dong) ===")
RANGE = re.compile(r"`(\d\.\d+)#(\d+)`\s*[–-]\s*`#(\d+)`")
SINGLE = re.compile(r"`(\d\.\d+)#(\d+)`")
ID_ONLY = re.compile(r"`(\d\.\d+)`")


def expand(cell):
    out = []
    for m in RANGE.finditer(cell):
        e, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        out.extend(f"{e}#{i}" for i in range(a, b + 1))
    rest = RANGE.sub("", cell)
    for m in SINGLE.finditer(rest):
        out.append(f"{m.group(1)}#{m.group(2)}")
    for m in ID_ONLY.finditer(rest):
        out.append(m.group(1))
    return out


sent_role = {}
for el, (role, _n) in new.items():
    sent_role[el] = role

bad = []
for cells in rows:
    sid, cues, vai = cells[0], cells[1], cells[2]
    if vai in ("—", "-", ""):
        continue
    ids = expand(cues)
    roles = {sent_role[i.split("#")[0]] for i in ids if i.split("#")[0] in sent_role}
    # N trong script = N1 (Kim Byers) hoac N2 (Mike Albrecht); N khac nhau theo element
    plan_norm = vai.strip()
    script_norm = "/".join(sorted(roles))
    # so sanh: plan N1 -> script N ; plan N2 -> script N
    if plan_norm.startswith("N"):
        okk = (roles == {"N"} and (plan_norm == "N1") == ("4.04" not in [i.split("#")[0] for i in ids]))
    else:
        okk = (script_norm == plan_norm)
    if not okk:
        bad.append((sid, cues, plan_norm, script_norm, ids))

for sid, cues, pr, sr, ids in bad:
    print(f"  {sid:6s} cues={cues:28s} plan_vai={pr:3s} script_vai={sr:3s}  ({', '.join(ids)})")
print(f"\n=> {len(bad)} dong sai vai")
