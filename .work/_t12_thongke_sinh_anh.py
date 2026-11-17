# -*- coding: utf-8 -*-
"""Tổng hợp số lượt sinh ảnh Tập 12 để rút kinh nghiệm."""
import glob
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]

total = 0
print("=== FILE JOBS ===")
for f in sorted(glob.glob(str(ROOT / ".work/bg_jobs_tap12*.json"))):
    try:
        j = json.loads(Path(f).read_text(encoding="utf-8"))
    except Exception as e:
        print(Path(f).name, "ERR", e)
        continue
    if not isinstance(j, list):
        continue
    bases = sorted({x["name"].rsplit("_", 1)[0] for x in j})
    seeds = [x.get("seed") for x in j if x.get("seed")]
    print(f"{Path(f).name:42} {len(j):>4} anh | {len(bases):>3} nen | seed {min(seeds) if seeds else '-'}..{max(seeds) if seeds else '-'}")
    total += len(j)

print(f"\nTONG so anh da sinh (theo file jobs): {total}")

print("\n=== ANH STAGING TREN DIA ===")
for d in ["old29", "old29v5", "old29v6", "detext3", "detext4"]:
    p = ROOT / ".work/_t12" / d
    if p.is_dir():
        print(f"  {d:10} {len(list(p.glob('*.png'))):>3} png")

print("\n=== KERNEL DA PUSH (ten co trong .work/kaggle_flux) ===")
for m in sorted(glob.glob(str(ROOT / ".work/kaggle_flux/*/kernel-metadata.json"))):
    md = json.loads(Path(m).read_text(encoding="utf-8"))
    print(f"  {md.get('id','?'):55} {Path(m).parent.name}")
