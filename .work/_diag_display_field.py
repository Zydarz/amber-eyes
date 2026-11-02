#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tts_manifest_JA_t02.json: truong 'display' co bao gio khac 'text' khong? + so sanh VOI payload Higgs."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ttm = json.loads((W / "tts_manifest_JA_t02.json").read_text(encoding="utf-8-sig"))
rows = ttm if isinstance(ttm, list) else ttm.get("items", [])
print("tts_manifest_JA_t02.json:", len(rows), "dong · truong:", sorted(rows[0].keys()))
for r in rows:
    if r.get("id") == "3.08#10":
        print("\nROW 3.08#10:")
        for k, v in r.items():
            print(f"   {k:<12} = {str(v)[:160]}")

disp = {r["id"]: r.get("display") for r in rows if "id" in r}
txt = {r["id"]: r.get("text") for r in rows if "id" in r}
d_diff = [i for i in disp if disp.get(i) != txt.get(i)]
print(f"\n  display != text: {len(d_diff)} / {len(disp)}")
for i in d_diff[:6]:
    print(f"    {i}\n      text    : {str(txt.get(i))[:95]}\n      display : {str(disp.get(i))[:95]}")

# payload Higgs (dict 6 khoa)
p = W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json"
pd = json.loads(p.read_text(encoding="utf-8-sig"))
print("\npayload keys:", list(pd.keys()))
items = pd.get("items") or pd.get("rows") or pd.get("sentences") or []
print("payload items:", len(items) if hasattr(items, "__len__") else items)
if isinstance(items, list) and items:
    print("mau payload item keys:", sorted(items[0].keys()))
    pm = {}
    for r in items:
        if isinstance(r, dict) and r.get("id"):
            pm[r["id"]] = r.get("text_plain") or r.get("text") or ""
    cov = [i for i in disp if i in pm]
    import re
    n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")
    diff = [i for i in cov if n(disp[i]) != n(pm[i])]
    print(f"  display(timeline) vs payload: phu {len(cov)}/203 · KHAC {len(diff)}")
    for i in diff[:8]:
        print(f"    {i}\n      disp   : {disp[i][:95]}\n      payload : {pm[i][:95]}")
