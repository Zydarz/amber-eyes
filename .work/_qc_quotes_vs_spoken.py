#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So 6 cau trich tren hinh voi cau THUC DOC (timeline) va kich ban VN."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it for it in tl["items"]}
shots = {s["id"]: s for s in json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]}

norm = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’()（）\-—–…]", "", t)

PAIRS = [
    ("3-21", "3.08#9", "3.08#10"),
    ("3-28", "3.11#5", "3.11#6"),
    ("4-08", "4.06#4", None),
    ("4-14", "4.08#7", None),
    ("4-15", "4.08#9", None),
    ("5-10", "5.04#8", None),
]
for sid, a, b in PAIRS:
    s = shots[sid]
    q = None
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            if k == "quote":
                q = v
    print("=" * 70)
    print(f"SHOT {sid} · cau shot = {s['sentences']}")
    print(f"  CHU TRICH tren hinh : {q!r}")
    for sid2 in [x for x in (a, b) if x]:
        print(f"  DOC ({sid2})        : {sent[sid2]['text']!r}")
    if q:
        txt = " ".join(sent[i]["text"] for i in s["sentences"])
        print(f"  -> chu trich co trong cau dang doc? {norm(q) in norm(txt)}")
        # gan nhat
        best = max(range(len(norm(txt)) - len(norm(q)) + 1) if len(norm(q)) <= len(norm(txt)) else [0],
                   key=lambda i: sum(1 for x, y in zip(norm(q), norm(txt)[i:i + len(norm(q))]) if x == y),
                   default=0)
        if len(norm(q)) <= len(norm(txt)):
            print(f"     do tuong doi giong nhat: {best}/{len(norm(q))}")

print("=" * 70)
print("DUONG DAN KICH BAN:")
for p in sorted((ROOT / "01_KICH_BAN").iterdir()):
    print("  ", p.name, [x.name for x in p.glob("*.md")][:2])
