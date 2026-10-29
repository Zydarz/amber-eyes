#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét cache: ô bảng có chứa newline (model đổi <br> thành xuống dòng).

    py -3 .work/_ja_scan_table_nl.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

total = 0
for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    cache = json.loads(cp.read_text(encoding="utf-8"))
    units = M.parse_units(M.canonical_vn(ep))
    tbl = {u["id"] for u in units if u["kind"] == "TABLE"}
    hits = []
    for k, v in cache.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        if k not in tbl:
            continue
        ja = v.get("ja", "") or ""
        if "\n" in ja or "\r" in ja:
            hits.append((k, ja))
    if hits:
        total += len(hits)
        print(f"Tap{ep}: {len(hits)} o bang co newline")
        for k, ja in hits:
            print(f"   {k}: {ja[:150]!r}")
print(f"\nTONG {total} muc can sua")
