#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In nguồn VN của các mục cần sửa tay."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import make_ja_scripts as M  # noqa: E402


def jobs_for(ep):
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    out = {}
    for u in units:
        if u["kind"] == "RAW":
            continue
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            if parts:
                for k, p in enumerate(parts):
                    out[f"{u['id']}#{k}"] = p
                continue
            out[f"{u['id']}#L"] = u["vi"]
            continue
        if u["kind"] == "TABLE":
            out[u["id"]] = u["vi"]
            continue
        out[u["id"]] = u["vi"]
    return out


for ep, k in [("18", "u0273"), ("20", "u0277"), ("21", "u0122"),
              ("22", "u0122"), ("24", "u0122")]:
    print(f"--- Tap{ep} {k}")
    print(jobs_for(ep).get(k))
    print()
