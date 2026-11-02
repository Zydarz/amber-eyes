#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra shot 2-23: so '2' tren hinh co trong cau noi moi (dinh dang kanji nhat) khong?"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
txt = json.loads((W / "shots_text_tap02_JA.json").read_text(encoding="utf-8-sig"))

for sid in ["2-23", "1-23", "1-27", "5-03", "2-14", "4-30", "5-11", "5-09"]:
    s = next((x for x in shots if x["id"] == sid), None)
    if not s:
        continue
    print(f"== {sid} · T{s['template']}")
    print(f"   CHU  : {txt.get(sid, [''])[0]}")
    for i in s["sentences"]:
        print(f"   {i}: {pm.get(i, {}).get('display', '<KHONG CO>')[:180]}")
    print()
