#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So bang shot (KeHoach Tap06 muc 6) voi script hien tai (154 cau).

In:  - cac sentence id ma bang shot tham chieu
Out: - sentence id trong script chua duoc shot nao cover
      - sentence id trong bang shot khong ton tai trong script
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
PLAN = ROOT / "02_SAN_XUAT" / "Tap06" / "KeHoach_Video_Tap06.md"

script = json.loads((WORK / "script_tap06.json").read_text(encoding="utf-8-sig"))

# ---- script: element -> danh sach cau (id, vai, text)
cur = {}          # "1.02#1" -> dict(role, text, el)
order = []        # thu tu cau trong script
for el in script:
    eid = el["id"]
    for i, s in enumerate(el.get("sentences") or [], start=1):
        sid = f"{eid}#{i}"
        role = s.get("role") or el.get("role") or "?"
        cur[sid] = {"role": role, "text": (s.get("text") or "").strip(), "el": eid}
        order.append(sid)

print(f"Script: {len(script)} element, {len(cur)} cau")

# ---- plan: dong bang shot
lines = PLAN.read_text(encoding="utf-8-sig").splitlines()
rows = []
for ln in lines:
    if not ln.startswith("|"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) < 8:
        continue
    if not re.fullmatch(r"\d-\d\d", cells[0]):
        continue
    rows.append(cells)

print(f"Bang shot: {len(rows)} dong")

# mo rong "1.02#2`-`#3" -> 1.02#2, 1.02#3
RANGE = re.compile(r"`(\d\.\d+)#(\d+)`\s*[–-]\s*`#(\d+)`")
SINGLE = re.compile(r"`(\d\.\d+)#(\d+)`")
ID_ONLY = re.compile(r"`(\d\.\d+)`")


def expand(cell):
    out = []
    for m in RANGE.finditer(cell):
        e, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        out.extend(f"{e}#{i}" for i in range(a, b + 1))
    # bo phan da expand
    rest = RANGE.sub("", cell)
    for m in SINGLE.finditer(rest):
        out.append(f"{m.group(1)}#{m.group(2)}")
    for m in ID_ONLY.finditer(rest):
        out.append(m.group(1))
    return out


covered = {}
for cells in rows:
    ids = expand(cells[1])
    for sid in ids:
        covered.setdefault(sid, []).append(cells[0])

print(f"Shot cover: {len(covered)} id duy nhat")

missing = [s for s in order if s not in covered]
ghost = [s for s in covered if s not in cur]
dup = {s: v for s, v in covered.items() if len(v) > 1}

print("\n=== CAU TRONG SCRIPT CHUA CO SHOT ===")
for s in missing:
    print(f"  {s:10s} [{cur[s]['role']:2s}] {cur[s]['text'][:95]}")

print("\n=== ID TRONG BANG SHOT KHONG TON TAI TRONG SCRIPT ===")
for s in sorted(ghost):
    print(f"  {s:10s} (shot {','.join(covered[s])})")

if dup:
    print("\n=== ID BI SHOT TRUNG ===")
    for s, v in sorted(dup.items()):
        print(f"  {s:10s} -> {v}")

# ---- so vai: shot row co khop vai voi script khong
print("\n=== SAI VAI (cung element, shot row 'Vai' khong khop) ===")
for cells in rows:
    row_role = cells[2]
    if row_role in ("—", "-", ""):
        continue
    for sid in expand(cells[1]):
        if sid in cur and cur[sid]["role"] != row_role:
            print(f"  shot {cells[0]:6s} row vai={row_role:2s} script vai={cur[sid]['role']:2s}  {sid}")
            break

# ---- xuat bang trai nghiem
out = WORK / "_t06_shotmap.json"
out.write_text(
    json.dumps({"current": cur, "order": order, "covered": covered}, ensure_ascii=False, indent=1),
    encoding="utf-8",
)
print(f"\nDa ghi {out}")
