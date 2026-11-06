#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
from parse_kichban import parse_file

W = Path(".work")
old = json.loads((W / "timeline_s_t05.json").read_text(encoding="utf-8"))
new = parse_file("01_KICH_BAN/Tap05/kichban_tap05_23102026.md")

print("=== kịch bản MỚI: thứ tự element ===")
for e in new:
    extra = ""
    if e.get("kind") != "LOI":
        extra = f"  [{e.get('kind')} {e.get('bgm') or e.get('sfx') or ''}]"
    n = len(e.get("sentences", []))
    ch = sum(len(s["text"]) for s in e.get("sentences", []))
    print(f"  {e['id']:<6} {e.get('kind'):<5} role={e.get('role') or '-':<3} sent={n:<3} chars={ch:<5}{extra}")

print("\n=== timeline CŨ: element -> span ===")
sp = {}
for it in old["items"]:
    e = it["element"]
    if e not in sp:
        sp[e] = [it["start"], it["end"], 0, 0]
    sp[e][1] = it["end"]
    sp[e][2] += 1
    sp[e][3] += len(it["text"])
for e, v in sp.items():
    print(f"  {e:<6} start={v[0]:>8.2f} end={v[1]:>8.2f} dur={v[1]-v[0]:>7.2f} n={v[2]:<3} chars={v[3]}")

print("\n=== markers CŨ ===")
for m in old["markers"]:
    print(" ", json.dumps(m, ensure_ascii=False)[:150])
