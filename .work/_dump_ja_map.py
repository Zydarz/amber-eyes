#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
from parse_kichban import parse_file

els = parse_file("01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md")
idx = {e["id"]: {s["id"]: s["text"] for s in e.get("sentences", [])}
       for e in els if e["kind"] == "LOI"}
sk = json.loads(Path(".work/_t05_skeleton.json").read_text(encoding="utf-8"))
for r in sk["rows"]:
    if r["kind"] != "shot":
        continue
    ids = [f"{eid}#{k}" for eid, a, b in r["spans"] for k in range(a, b + 1)]
    print(f"{r['sid']} | " + " + ".join(idx[i.split('#')[0]][i] for i in ids))
