#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Don manifest: bo dong stale + mo lai dong pending cho code can tai lai.

Usage: py -3 .work/_map_fix.py <code>...          # xoa dong manifest theo ma
       py -3 .work/_map_fix.py --unuse <code>...   # bo code khoi state['used']
"""
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
MAP = ROOT / ".work" / "yt_map.tsv"
STATE = ROOT / ".work" / "yt_watch_state.json"

args = sys.argv[1:]
mode = args[0] if args else ""
codes = args[1:] if mode.startswith("--") else args

if mode == "--unuse":
    st = json.loads(STATE.read_text(encoding="utf-8"))
    before = len(st.get("used", []))
    st["used"] = [c for c in st.get("used", []) if c not in codes]
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"used: {before} -> {len(st['used'])} (removed {sorted(set(codes))})")
elif mode:
    lines = MAP.read_text(encoding="utf-8-sig").splitlines()
    kept, dropped = [], []
    for i, l in enumerate(lines, 1):
        p = l.split("\t")
        if len(p) >= 2 and p[1].strip() in codes and l.strip():
            dropped.append((i, p[0], p[1]))
        else:
            kept.append(l)
    MAP.write_text("\n".join(kept) + "\n", encoding="utf-8")
    print(f"manifest: {len(lines)} -> {len(kept)} dong")
    for d in dropped:
        print(f"  DROPPED line{d[0]}: {d[1]} -> {d[2]}")
else:
    print(__doc__)
