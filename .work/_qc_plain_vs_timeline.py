#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""text_plain cua manifest Higgs JA Tap02 == timeline (phu de + chu tren hinh)?"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it["text"] for it in tl["items"]}
man_p = W / "kaggle_higgs/out_higgs_prod_JA_t02/out_higgs_prod_JA_t02/higgs_manifest.json"
man_r = W / "kaggle_higgs/out_higgs_r2_JA_t02/out_higgs_r2_JA_t02/higgs_manifest.json"

n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

for tag, f in [("PROD", man_p), ("R2", man_r)]:
    if not f.exists():
        print(f"{tag}: KHONG CO")
        continue
    rows = json.loads(f.read_text(encoding="utf-8-sig"))
    plain, sentv = {}, {}
    for r in rows:
        if not isinstance(r, dict):
            continue
        sid = r.get("id")
        if not sid:
            continue
        if r.get("text_plain"):
            plain.setdefault(sid, r["text_plain"])
        if r.get("text_sent"):
            sentv.setdefault(sid, r["text_sent"])
    cov = [i for i in sent if i in plain]
    diff = [(i, plain[i]) for i in cov if n(plain[i]) != n(sent[i])]
    print("=" * 72)
    print(f"{tag}: {f.relative_to(ROOT)}")
    print(f"  text_plain phu timeline: {len(cov)}/203 · KHAC: {len(diff)}")
    for i, p in diff[:6]:
        print(f"    {i}\n      tl    : {sent[i][:95]}\n      plain : {p[:95]}")
    # kiem tra 3.08#10
    for probe in ["3.08#10", "3.11#5", "4.06#4"]:
        if probe in plain:
            print(f"    [{probe}] plain = {plain[probe][:100]}")
            print(f"    [{probe}] sent  = {sentv.get(probe, '')[:100]}")

print("=" * 72)
print("=== KICH BAN MARKDOWN vs TIMELINE: bao nhieu cau lech? ===")
md = (ROOT / "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md").read_text(encoding="utf-8-sig")
sc = json.loads((W / "script_tap02_JA.json").read_text(encoding="utf-8-sig"))
smap = {}
for turn in sc:
    for s in turn.get("sentences", []):
        smap[s["id"]] = s["text"]
diff2 = [i for i in sent if i in smap and n(smap[i]) != n(sent[i])]
print(f"  script_tap02_JA.json vs timeline: KHAC {len(diff2)} / {len(sent)}")
for i in diff2[:6]:
    print(f"    {i}\n      script   : {smap[i][:95]}\n      timeline : {sent[i][:95]}")
