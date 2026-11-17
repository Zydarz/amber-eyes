# -*- coding: utf-8 -*-
"""Gỡ bản ghi provenance của 2 ảnh thừa đã xoá (H22 ①: 0 ảnh sinh mà không dùng)."""
import json
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PROV = ROOT / "provenance.json"
DROP = {"assets/bg/t11_battered_woman_syndrome_file.png",
        "assets/bg/t11_toxic_devotion_cruelty.png"}

prov = json.loads(PROV.read_text(encoding="utf-8"))
before = len(prov)
prov = [r for r in prov if r.get("file") not in DROP]
PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"provenance: {before} -> {len(prov)} (gỡ {before - len(prov)})")
for r in prov:
    if "t11_" in (r.get("file") or "") and "Real-ESRGAN" in (r.get("cong_cu") or ""):
        print("  còn bản ghi Real-ESRGAN:", r["file"])
