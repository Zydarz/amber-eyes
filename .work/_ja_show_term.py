#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tìm dòng VN chứa 'cảnh tỉnh' / 'bài học' và dòng JA tương ứng."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import make_ja_scripts as M  # noqa: E402

for ep in ("14", "19"):
    src = M.canonical_vn(ep)
    units = M.assign_turn_counts(M.parse_units(src))
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    import json
    cache = json.loads((HERE / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
    print(f"########## Tap{ep}")
    for u in units:
        if u["kind"] == "RAW":
            continue
        txt = u.get("vi", "") or ""
        if "cảnh tỉnh" not in txt and "bài học" not in txt.lower():
            continue
        ids = [u["id"]]
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            ids = [f"{u['id']}#{k}" for k in range(len(parts))] if parts else [f"{u['id']}#L"]
        for i in ids:
            ja = cache.get(i, {}).get("ja", "")
            print(f"  [{i}] kind={u['kind']}")
            print(f"     VN: {txt[:160]}")
            print(f"     JA: {ja[:160]}")
    print()
