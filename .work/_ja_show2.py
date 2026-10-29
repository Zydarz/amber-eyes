#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem chính xác 2 mục Tap28/Tap16 cần kiểm tra."""
import json
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
        out[u["id"]] = u["vi"]
    return out


for ep, keys in [("28", ["u0043", "u0044", "u0045", "u0046", "u0047"]),
                 ("16", ["u0006", "u0007", "u0008", "u0009"])]:
    jb = jobs_for(ep)
    cache = json.loads((HERE / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
    print(f"########## Tap{ep}")
    for k, v in cache.items():
        ja = v.get("ja", "") if isinstance(v, dict) else ""
        if not isinstance(ja, str):
            continue
        if "Hội" in ja or "Chuột" in ja or "Áo" in ja:
            print(f"  [{k}]")
            print(f"     VN: {jb.get(k, '')[:300]}")
            print(f"     JA: {ja[:300]}")
    print()
