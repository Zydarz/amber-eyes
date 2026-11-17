# -*- coding: utf-8 -*-
"""Tập 12 — chia 58 biến thể (29 nền × 2) thành 4 tờ montage 16 ô để soi.

Mỗi tờ 4x4 ô 512 px ⇒ ô ~390 px sau resize (A11 #172).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
STAGE = ROOT / ".work" / "_t12" / "old29"
OUT = ROOT / ".work" / "_t12" / "sheets_old29"
OUT.mkdir(parents=True, exist_ok=True)

JOBS = json.loads((ROOT / ".work/bg_jobs_tap12_old29.json").read_text(encoding="utf-8"))
names = [j["name"].replace("t12_", "") for j in JOBS]
missing = [n for n in names if not (STAGE / f"t12_{n}.png").exists()]
print(f"bien the: {len(names)} · chua ve: {len(missing)}")

PER = 16
sheets = []
for i in range(0, len(names), PER):
    chunk = names[i:i + PER]
    tag = f"g{i // PER + 1:02d}"
    f = OUT / f"list_{tag}.json"
    f.write_text(json.dumps({"must": chunk}, ensure_ascii=False, indent=1), encoding="utf-8")
    sheets.append({"tag": tag, "n": len(chunk), "file": str(f)})

(OUT / "sheets.json").write_text(json.dumps(sheets, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(names)} bien the -> {len(sheets)} to")
for s in sheets:
    print(f"  {s['tag']}: {s['n']} o")
