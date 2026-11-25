#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In từng job của một tập kèm nội dung câu được gán, để rà tay ảnh ↔ lời.
Dùng: py -3 .work/review_bg_ep.py XX [hồi] [--full]"""
import sys, json, importlib.util
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).parent
spec = importlib.util.spec_from_file_location("q", W / "qc_bg_mapping.py"); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
n = int(sys.argv[1]); act = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else None
full = "--full" in sys.argv
T = {s["id"]: s["text"] for e in q.pk.parse_file(q.script_file(n)) for s in (e.get("sentences") or [])}
for i, x in enumerate(json.load(open(W / f"bg_jobs_tap{n:02d}.json", encoding="utf-8")), 1):
    if act and x["act"] != act: continue
    cs = [c for c in x["sentences"].split(",") if c]
    txt = " / ".join(T[c][:(300 if full else 110)] for c in cs)
    print(f'[{i}] {x["name"].split("_",2)[2][:46]} ({x["sentences"]})\n   LỜI: {txt}\n   ẢNH: {x["prompt"][:(300 if full else 140)]}')
