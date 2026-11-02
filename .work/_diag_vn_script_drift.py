#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VN script (audio that cu) vs JA payload (audio moi): cung mot ban dich?"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

vn = {}
sc = json.loads((W / "script_tap02.json").read_text(encoding="utf-8-sig"))
for turn in sc:
    for s in turn.get("sentences", []):
        vn[s["id"]] = s["text"]

pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}

PROBES = ["2.07#3", "3.11#5", "3.08#10", "4.08#6", "4.08#7", "4.08#8", "5.04#8",
          "1.17#1", "1.14#2", "1.10#2"]
for p in PROBES:
    print(f"== {p}")
    print(f"   VN : {vn.get(p, '<KHONG CO>')[:150]}")
    print(f"   JA : {pm.get(p, {}).get('display', '<KHONG CO>')[:150]}")
    print()

# so cau doc = timeline JA (25/10) vs payload JA (31/10)
tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it["text"] for it in tl["items"]}
same_vn = sum(1 for i in sent if i in vn and n(vn[i]) == n(sent[i]))
print(f"timeline JA (25/10) vs script VN: giong {same_vn}/{len(sent)}")
