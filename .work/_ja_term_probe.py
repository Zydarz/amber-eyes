#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tìm câu VN chứa cụm thuật ngữ và in ra câu JA tương ứng."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from ja_glossary import TERMS  # noqa: E402

ep = sys.argv[1]
phrases = sys.argv[2:]
cache = json.loads((M.WORK / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}

for u in units:
    if u["kind"] not in ("TEXT", "BULLET") or u["id"] not in in_turn:
        continue
    for ph in phrases:
        if ph not in u["vi"]:
            continue
        parts = M.splittable(u)
        if parts:
            got = [cache.get(f"{u['id']}#{k}", {}).get("ja", "") for k in range(len(parts))]
            ja = "".join(got)
        else:
            ja = cache.get(f"{u['id']}#L", {}).get("ja", "")
        print(f"\n=== {u['id']}  [{ph}]")
        print(f"  VN: {u['vi'][:260]}")
        print(f"  JA: {ja[:260]}")

print("\n--- glossary liên quan ---")
for vi, ja_t in TERMS.items():
    if any(p in vi for p in phrases) or any(p in ja_t for p in phrases):
        print(f"   {vi!r} -> {ja_t!r}")
