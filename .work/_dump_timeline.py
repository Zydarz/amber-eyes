#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent
for f in ("timeline_s_t05.json", "timeline_s_EN_t05.json", "timeline_s_JA_t05.json"):
    p = W / f
    if not p.exists():
        print(f, "MISSING"); continue
    d = json.loads(p.read_text(encoding="utf-8"))
    print("=" * 70)
    print(f, "keys:", list(d.keys()))
    print("  total:", d["total"], "· intro:", d.get("intro"))
    print("  items:", len(d["items"]))
    print("  item[0]:", json.dumps(d["items"][0], ensure_ascii=False))
    print("  item[1]:", json.dumps(d["items"][1], ensure_ascii=False))
    print("  item[-1]:", json.dumps(d["items"][-1], ensure_ascii=False))
    print("  markers:", len(d["markers"]))
    for m in d["markers"][:4]:
        print("   ", json.dumps(m, ensure_ascii=False))
    print("  marker types:", sorted({m.get("type") for m in d["markers"]}))
    print("  acts:", json.dumps(d.get("acts"), ensure_ascii=False)[:400])
