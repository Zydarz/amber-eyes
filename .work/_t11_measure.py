#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo toàn bộ trạng thái bộ nền Tập 11 (16/11/2026) để viết báo cáo QC — số đo thật."""
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
WORK = ROOT / ".work"

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

files = sorted(BG.glob("t11_*.png"))
print(f"1) FILE NEN tren dia: {len(files)}")
sizes = Counter()
for p in files:
    from PIL import Image
    with Image.open(p) as im:
        sizes[im.size] += 1
print(f"   kich thuoc: {dict(sizes)}")

prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
tp = [r for r in prov if r.get("file", "").startswith("assets/bg/t11_")]
print(f"\n2) PROVENANCE (L7): {len(tp)} dong cho nen t11_")
print(f"   cong_cu: {dict(Counter(r.get('cong_cu', '?')[:60] for r in tp))}")
print(f"   ngay: {dict(Counter(r.get('ngay', '?') for r in tp))}")
esrgan = [r["file"] for r in tp if "Real-ESRGAN" in (r.get("cong_cu") or "").upper()
          and "KHONG" not in (r.get("cong_cu") or "").upper()
          and "NO " not in (r.get("cong_cu") or "").upper()]
print(f"   nen that su dung Real-ESRGAN: {len(esrgan)} {esrgan[:5]}")

for tag, f in [("VI", "shots_t11.json"), ("EN", "shots_EN_t11.json"), ("JA", "shots_JA_t11.json")]:
    sh = json.loads((WORK / f).read_text(encoding="utf-8"))["shots"]
    bgs = [s["bg"] for s in sh]
    dur = sum(s["end"] - s["start"] for s in sh)
    per = Counter(bgs)
    print(f"\n3) {tag}: {len(sh)} shot · {len(set(bgs))} nen · "
          f"{len(set(bgs)) - 1} nen t11_ · tong {dur:.1f} s · "
          f"trung binh {len(sh) / max(1, len(set(bgs)) - 1):.2f} shot/nen")
    print(f"   inherited={sum(1 for s in sh if s.get('bg_inherited'))} "
          f"hold={sum(1 for s in sh if s.get('hold'))} "
          f"max shot/1 nen={max(per.values())}")
    # phan bo shot/nen
    print(f"   phan bo shot/nen: {dict(sorted(Counter(per.values()).items()))}")

viol = json.loads((WORK / "_t11" / "violations_t11.json").read_text(encoding="utf-8"))
print(f"\n4) SOI MAT 100% nen: {len(viol)} nen co chu AI da phat hien "
      f"({len(viol) / len(files) * 100:.1f}%)")
print(f"   muc: {dict(Counter(v['level'] for v in viol))}")

for d in ["video3_t11", "video3_EN_t11", "video3_JA_t11"]:
    st = WORK / d / "stills"
    n = len(list(st.glob("shot_*.png"))) if st.is_dir() else 0
    print(f"5) STILL {d}: {n} anh")
