#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem cau truc Tap03: element / vai / so cau / trich dan."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"D:\TEST\Gax\Audi\.work\script_tap03.json")
els = json.loads(src.read_text(encoding="utf-8"))

n_loi = 0
n_sent = 0
words = 0
for e in els:
    if e["kind"] == "LOI":
        n_loi += 1
        n_sent += len(e["sentences"])
        words += sum(s["words"] for s in e["sentences"])
        t = e["text"][:76].replace("\n", " ")
        print(f"{e['id']:<8}{e['role']:<4}{len(e['sentences']):>3}sent  {t}")
    else:
        d = e.get("desc", "")
        print(f"{e['id']:<8}--   {e['kind']:<6} {d[:60]}")
print("-" * 70)
print(f"LOI (luot) = {n_loi} · cau = {n_sent} · tu = {words}")
roles = {}
for e in els:
    if e["kind"] == "LOI":
        roles.setdefault(e["role"], []).append(e["id"])
for r, ids in roles.items():
    print(f"  vai {r}: {len(ids)} luot -> {', '.join(ids)}")
