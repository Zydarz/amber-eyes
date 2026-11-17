#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chia 136 nền Tập 11 thành 9 tờ montage 16 ô (4x4) để soi 100 % mà vẫn đọc được chữ.

Lý do: ảnh đưa vào context bị resize theo cạnh dài ≤ ~1568 px ⇒ ô phải ≥ ~384 px
sau resize. 4 cột x 4 hàng, ô 512 px ⇒ sau resize ô ≈ 390 px.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t11" / "sheets"
OUT.mkdir(parents=True, exist_ok=True)

names = sorted(p.stem.replace("t11_", "") for p in BG.glob("t11_*.png"))
PER = 16
sheets = []
for i in range(0, len(names), PER):
    chunk = names[i:i + PER]
    tag = f"s{i // PER + 1:02d}"
    f = OUT / f"list_{tag}.json"
    f.write_text(json.dumps({"must": chunk}, ensure_ascii=False, indent=1), encoding="utf-8")
    sheets.append({"tag": tag, "n": len(chunk), "file": str(f)})

(OUT / "sheets.json").write_text(json.dumps(sheets, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(names)} nen -> {len(sheets)} to")
for s in sheets:
    print(f"  {s['tag']}: {s['n']} o")
