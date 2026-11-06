#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — in EPISODES['06'] co nhung muc nao khoa theo ID shot (combo/inset/bg2/n_element)."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import edition as ED  # noqa: E402

EP = ED.EPISODES["06"]
for k in ("combo", "inset", "bg2", "n_element", "roles", "sub_tags"):
    v = EP.get(k)
    if not v:
        print(f"{k}: (rong)")
        continue
    print(f"--- {k} ({len(v)}) ---")
    if isinstance(v, dict):
        for kk, vv in v.items():
            print(f"   {kk} -> {vv}")
    else:
        print("   ", v)
print()
print("--- EPISODES['06'] tat ca khoa ---")
for k in EP:
    if k in ("combo", "inset", "bg2", "n_element"):
        continue
    print(f"   {k} = {EP[k]}")
