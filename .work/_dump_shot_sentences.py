#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shot -> sentence ids -> loi noi moi, cho cac shot can sua chu tren hinh."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]

IDS = ["1-24", "1-25", "1-28", "2-11", "3-02", "3-09", "3-13", "3-20", "3-25", "3-27",
       "3-28", "4-12", "4-13", "4-14", "4-15", "5-08", "5-10", "5-24", "2-17", "2-18",
       "3-21", "4-08"]
for sid in IDS:
    s = next((x for x in shots if x["id"] == sid), None)
    if not s:
        print(f"== {sid}: KHONG CO")
        continue
    print(f"== {sid} · vai {s['role']} · T{s['template']} · bg {s['bg']}")
    for i in s["sentences"]:
        t = pm.get(i, {}).get("display", "<KHONG CO TRONG PAYLOAD>")
        print(f"   {i}: {t}")
    print()
