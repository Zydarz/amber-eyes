#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trợ giúp: in CHỮ VN + BEAT VN + số cụm `ở "…"` cho từng shot của bảng VN."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
vn = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn) if i > i0 and l.startswith("**Tổng:"))

script = json.loads((ROOT / ".work/script_tap02_JA.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


want = sys.argv[1] if len(sys.argv) > 1 else ""
with_ctx = "--ctx" in sys.argv
n = 0
for l in vn[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    sid = m.group(1)
    if want and not sid.startswith(want):
        continue
    n += 1
    c = l.strip().strip("|").split("|")
    ids = sents(c[1])
    ph = re.findall(r'ở "([^"]+)"', c[6])
    print(f"{sid} | cell={c[1].strip()} | nph={len(ph)} {ph}")
    print(f"    CHU : {c[5].strip()}")
    print(f"    BEAT: {c[6].strip()}")
    if with_ctx:
        ctx = " ".join(S.get(x, "") for x in ids)
        print(f"    CTX : {ctx}")
print(f"-- {n} shots --")
