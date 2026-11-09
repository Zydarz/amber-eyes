#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap07 — dump new script structure (elements, roles, sentences) for all 3 languages."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

KB = {
    "vi": "01_KICH_BAN/Tap07/kichban_tap07_23102026.md",
    "en": "01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md",
    "ja": "01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md",
}
data = {}
for lang, rel in KB.items():
    els = parse_file(str(ROOT / rel))
    data[lang] = els

print("=== VI element structure ===")
for e in data["vi"]:
    if e["kind"] == "LOI":
        sids = [s["id"] for s in e["sentences"]]
        print(f'  {e["id"]:>6} role={e["role"]:<3} n={len(sids):<3} {sids[0]}..{sids[-1]}  dir="{e.get("direction","")}"')
    else:
        print(f'  {e["id"]:>6} [{e["kind"]}] {e.get("desc","")[:60]}')

print()
print("=== EN / JA parity (element id + sentence count) ===")
bad = 0
for i in range(len(data["vi"])):
    ev, ee, ej = data["vi"][i], data["en"][i], data["ja"][i]
    if ev["id"] != ee["id"] or ev["id"] != ej["id"]:
        print(f"  ID MISMATCH at {i}: {ev['id']} / {ee['id']} / {ej['id']}")
        bad += 1
        continue
    if ev["kind"] != "LOI":
        continue
    nv = len(ev["sentences"])
    ne = len(ee["sentences"])
    nj = len(ej["sentences"])
    if not (nv == ne == nj):
        print(f"  COUNT MISMATCH {ev['id']}: vi={nv} en={ne} ja={nj}")
        bad += 1
print(f"  mismatches: {bad}")

print()
print("=== role distribution (VI) ===")
roles = {}
for e in data["vi"]:
    if e["kind"] == "LOI":
        roles[e["role"]] = roles.get(e["role"], 0) + len(e["sentences"])
print("  ", roles)
print("  total sentences:", sum(roles.values()))

print()
print("=== act element ranges ===")
for lang in ("vi",):
    cur = None
    for e in data[lang]:
        if e["act"] != cur:
            cur = e["act"]
            print(f"  act {cur}: starts {e['id']}")
