#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — in câu JA theo RUN (mốc dấu câu) để chọn mảnh chữ liên tục."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent

sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
sent = json.loads((W / "_t04_sentences.json").read_text(encoding="utf-8"))
ja = sent["ja"]
chu = json.loads((W / "_t04_chu_vn.json").read_text(encoding="utf-8"))
bvi = json.loads((W / "_t04_beat_vi.json").read_text(encoding="utf-8"))

shots = [r for r in sk["rows"] if r["kind"] == "shot"]

if sys.argv[1] == "beats":
    print("=== BEAT có trích dẫn (phải override) ===")
    for r in shots:
        c = r["cells"][6]
        if '"' in c:
            print(f"  {r['sid']}: {c}   [VN-override: {bvi.get(r['sid'], '-')}]")
    print()
    print("=== TẤT CẢ shot có beat ===")
    for r in shots:
        c = r["cells"][6]
        if c.strip() not in ("", "—"):
            print(f"  {r['sid']}: {c}")
    sys.exit(0)

lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi = int(sys.argv[3]) if len(sys.argv) > 3 else len(shots)

for r in shots[lo:hi]:
    eid, a, b = r["spans"][0]
    print(f"### {r['sid']}  [{r['cells'][3]}]  {eid} #{a}-{b}")
    print(f"  VN: {chu.get(r['sid'], '')}")
    for s in ja.get(eid, [])[a - 1:b]:
        # đánh dấu ranh giới run = ký tự không phải \w
        marked = re.sub(r"([^\w\s])", r"|\1|", s["text"])
        print(f"  {s['id']}: {marked}")
    print()
