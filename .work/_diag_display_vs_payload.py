#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SO SANH THUC TE: timeline.display  vs  payload.display  (cai Higgs thuc su doc)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it["text"] for it in tl["items"]}

for tag, pf in [("PAYLOAD prod", "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json"),
                ("PAYLOAD r2", "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_r2_JA_t02.json"),
                ("MANIFEST prod", "kaggle_higgs/out_higgs_prod_JA_t02/out_higgs_prod_JA_t02/higgs_manifest.json")]:
    p = W / pf
    if not p.exists():
        print(f"{tag}: KHONG CO")
        continue
    d = json.loads(p.read_text(encoding="utf-8-sig"))
    items = d.get("items") if isinstance(d, dict) else d
    pm = {}
    for r in items:
        if isinstance(r, dict) and r.get("id"):
            pm.setdefault(r["id"], r)
    print("=" * 72)
    print(f"{tag}: {len(pm)} cau · co truong display = "
          f"{sum(1 for r in pm.values() if r.get('display'))}")
    cov = [i for i in sent if i in pm and pm[i].get("display")]
    diff = [i for i in cov if n(sent[i]) != n(pm[i]["display"])]
    print(f"  timeline.display vs payload.display: phu {len(cov)}/203 · KHAC {len(diff)}")
    for i in diff[:5]:
        print(f"    {i}\n      timeline: {sent[i][:92]}\n      payload : {pm[i]['display'][:92]}")
    # neu khong co truong display, so voi text_plain
    if not cov:
        cov2 = [i for i in sent if i in pm and pm[i].get("text_plain")]
        d2 = [i for i in cov2 if n(sent[i]) != n(pm[i]["text_plain"])]
        print(f"  timeline.display vs payload.text_plain: phu {len(cov2)}/203 · KHAC {len(d2)}")
        for i in d2[:5]:
            print(f"    {i}\n      timeline: {sent[i][:92]}\n      payload : {pm[i]['text_plain'][:92]}")

# bao nhieu cau doc len (spoken) khac phu de (display)?
p = W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json"
d = json.loads(p.read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in d["items"] if r.get("id")}
spoken = {}
for i, r in pm.items():
    spoken[i] = r.get("text_sent") or r.get("text") or ""
print("=" * 72)
print("=== DOC vs PHU DE (payload) ===")
big = []
for i in sent:
    if i not in spoken:
        continue
    a, b = n(spoken[i]), n(sent[i])
    if a != b:
        big.append((i, spoken[i], sent[i]))
print(f"  cau noi (Higgs) khac phu de (timeline): {len(big)} / {len(sent)}")
for i, sp, ds in big[:8]:
    print(f"    {i}")
    print(f"      NOI : {sp[:92]}")
    print(f"      DE  : {ds[:92]}")
