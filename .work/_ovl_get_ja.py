#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trợ giúp: in các câu JA theo mã element (vd: 1.03) từ script_tap02_JA.json."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).resolve().parent
script = json.loads((W / "script_tap02_JA.json").read_text(encoding="utf-8"))
S = {}
order = []
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]
            order.append(s["id"])

if len(sys.argv) > 1 and sys.argv[1] == "--list":
    for sid in order:
        print(sid)
    sys.exit(0)

for arg in sys.argv[1:]:
    if "–" in arg or "-" in arg and arg.replace("-", "").isdigit():
        pass
    hits = [sid for sid in order if sid.split("#")[0] == arg]
    for sid in hits:
        print(f"[{sid}] {S[sid]}")
    if not hits:
        print(f"[{arg}] (khong tim thay)")
