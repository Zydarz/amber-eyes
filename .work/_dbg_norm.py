#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

W = ROOT / ".work"
idx = {}
for el in parse_file(str(ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026.md")):
    if el["kind"] == "LOI":
        idx[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


eid = sys.argv[1]
frag = sys.argv[2]
a = int(sys.argv[3])
b = int(sys.argv[4])
ctx = " ".join(t for _, t in idx[eid][a - 1:b])
print("FRAG :", repr(norm(frag)))
print("CTX  :", repr(norm(ctx)))
fw = norm(frag).split()
cw = norm(ctx).split()
hit = False
for i in range(len(cw) - len(fw) + 1):
    if cw[i:i + len(fw)] == fw:
        hit = True
        print("MATCH tại", i)
        break
if not hit:
    for i, w in enumerate(cw):
        if w == fw[0]:
            print("  cùng từ đầu tại", i, "->", cw[i:i + len(fw)], "vs", fw)
