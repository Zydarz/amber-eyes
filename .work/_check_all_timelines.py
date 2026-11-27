#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra tat ca timeline Tap04 (15 file) xem co dong NOI SUY / MATCH YEU khong."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / ld
    for n in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
        p = d / f"timeline_{n.lower()}.json"
        if not p.exists():
            print(f"{ld:9} {n} MISSING")
            continue
        tl = json.loads(p.read_text(encoding="utf-8"))
        bad = [t["id"] for t in tl if t.get("interp") or t.get("match_ratio", 1) < 0.6]
        end = max(t["end"] for t in tl)
        print(f"{ld:9} {n} lines={len(tl):2} end={end:6.2f} bad={bad}")
