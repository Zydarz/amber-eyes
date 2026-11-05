#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — dump đầy đủ 89 shot (skeleton + câu JA + chữ VN) để viết lớp phủ JA."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent

sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
sent = json.loads((W / "_t04_sentences.json").read_text(encoding="utf-8"))
ja = sent["ja"]
chu = json.loads((W / "_t04_chu_vn.json").read_text(encoding="utf-8"))
beat = json.loads((W / "_t04_beat_vi.json").read_text(encoding="utf-8"))

shots = [r for r in sk["rows"] if r["kind"] == "shot"]
lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(shots)

for r in shots[lo:hi]:
    c = r["cells"]
    eid, a, b = r["spans"][0]
    ss = ja.get(eid, [])
    print(f"### {r['sid']}  (from {r['from']})  span={eid} #{a}-{b}")
    print(f"  Mẫu  : {c[3]}   | Nền: {c[4]} | Vai: {c[2]} | Nhân vật: {c[7]} | Ghi chú: {c[8]}")
    print(f"  ChữVN: {chu.get(r['sid'], '')}")
    print(f"  BeatVN: {c[6]}" + (f"   [OVERRIDE-> {beat[r['sid']]}]" if r["sid"] in beat else ""))
    for s in ss[a - 1:b]:
        print(f"    {s['id']} ({s['role']}) {s['text']}")
    print()
