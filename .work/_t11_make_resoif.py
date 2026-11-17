#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng montage soi lại 32 nền vừa sinh lại (bỏ chữ) — 2 tờ, ô 700 px.

Ô 700 px ⇒ sau khi resize (cạnh dài ≤ ~1568) ô còn ~530 px ⇒ đọc được chữ nhỏ.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t11" / "sheets"

V = json.loads((ROOT / ".work" / "_t11" / "violations_t11.json").read_text(encoding="utf-8"))
names = [v["name"].replace("t11_", "") for v in V]
names = [n for n in names if (BG / f"t11_{n}.png").exists()]
print(f"{len(names)} nen can soi lai")

PER = 8
for i in range(0, len(names), PER):
    chunk = names[i:i + PER]
    tag = f"re{i // PER + 1:02d}"
    f = OUT / f"list_{tag}.json"
    f.write_text(json.dumps({"must": chunk}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  {tag}: {len(chunk)} o -> {f.name}")
