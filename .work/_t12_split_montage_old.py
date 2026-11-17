#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 12 — chia 83 nền CŨ (có sẵn từ trước) thành 6 tờ montage 16 ô để soi 100 %.

Vòng 1 chỉ soi 69 nền MỚI; 83 nền có sẵn từ trước chưa được soi lại toàn bộ.
4 cột x 4 hàng, ô 512 px ⇒ ô ≈ 390 px sau resize (A11 #172).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t12" / "sheets_old"
OUT.mkdir(parents=True, exist_ok=True)

ALL = json.loads((ROOT / ".work/bg_jobs_tap12_v2.json").read_text(encoding="utf-8"))
NEW = {j["name"] for j in
       json.loads((ROOT / ".work/bg_jobs_tap12_new69.json").read_text(encoding="utf-8"))}
names = sorted(j["name"].replace("t12_", "") for j in ALL if j["name"] not in NEW)
missing = [n for n in names if not (BG / f"t12_{n}.png").exists()]
if missing:
    print(f"THIEU {len(missing)} anh: {missing[:10]}")

PER = 16
sheets = []
for i in range(0, len(names), PER):
    chunk = names[i:i + PER]
    tag = f"o{i // PER + 1:02d}"
    f = OUT / f"list_{tag}.json"
    f.write_text(json.dumps({"must": chunk}, ensure_ascii=False, indent=1), encoding="utf-8")
    sheets.append({"tag": tag, "n": len(chunk), "file": str(f)})

(OUT / "sheets.json").write_text(json.dumps(sheets, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(names)} nen cu -> {len(sheets)} to")
for s in sheets:
    print(f"  {s['tag']}: {s['n']} o")
