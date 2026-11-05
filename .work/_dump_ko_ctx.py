#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump per-shot context: shot id, VN sentence cell, VN beat cell, KO sentences."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
OUT = (W / "_dump_ko_ctx.txt").open("w", encoding="utf-8")


def p(*a):
    OUT.write(" ".join(str(x) for x in a) + "\n")


script = json.loads((W / "script_tap02_KO.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

vn_lines = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_lines) if i > i0 and l.startswith("**Tổng:"))

for l in vn_lines[i0:i1 + 1]:
    p("RAW:", l)


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


p("=" * 100)
n = 0
for l in vn_lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    sid = m.group(1)
    c = l.strip().strip("|").split("|")
    n += 1
    ids = sents(c[1])
    p(f"\n### {sid} | COT-CAU: {c[1].strip()}")
    p(f"  VN CHU : {c[5].strip()}")
    p(f"  VN BEAT: {c[6].strip()}")
    for x in ids:
        p(f"  KO {x}: {S.get(x, '<<MISSING>>')}")
p(f"\nTOTAL SHOT ROWS: {n}")
OUT.close()
print(f"ok rows={n}")
