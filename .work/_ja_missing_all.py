#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê các mục cache còn THIẾU cho mọi tập + lý do lỗi.

    py -3 .work/_ja_missing_all.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

CACHE = HERE / "ja_cache"
total_missing = 0
for i in range(1, 30):
    ep = f"{i:02d}"
    cp = CACHE / f"tap{ep}.json"
    cache = {}
    if cp.exists():
        cache = json.loads(cp.read_text(encoding="utf-8"))
    try:
        units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
    except Exception as e:
        print(f"Tap{ep}: lỗi đọc VN ({e})")
        continue
    in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}
    need = set()
    for u in units:
        if u["kind"] == "RAW":
            continue
        if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
            parts = M.splittable(u)
            if parts:
                need |= {f"{u['id']}#{k}" for k in range(len(parts))}
            else:
                need.add(f"{u['id']}#L")
        else:
            need.add(u["id"])
    have = {k for k in cache if isinstance(k, str) and not k.startswith("_")}
    miss = sorted(need - have)
    if miss:
        total_missing += len(miss)
        errs = cache.get("_err", {})
        print(f"\nTap{ep}: THIẾU {len(miss)}/{len(need)} mục")
        for k in miss:
            print(f"   {k}: {errs.get(k, '(chưa có lý do)')[:150]}")
print(f"\n==> Tổng mục thiếu: {total_missing}")
