#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audio co khop timeline (phu de + chu tren hinh) khong? So ca 203 cau.

Nguon that su: higgs_manifest.json trong thu muc output Kaggle (cai ma Higgs doc that).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it["text"] for it in tl["items"]}

# 1) manifest Higgs that su
cands = list(W.glob("kaggle_higgs/**/higgs_manifest.json"))
print("=== MANIFEST HIGGS TIM THUC ===")
man = None
for c in cands:
    if "JA_t02" in str(c):
        d = json.loads(c.read_text(encoding="utf-8-sig"))
        print(f"  {c.relative_to(ROOT)}")
        print(f"    kieu={type(d).__name__} len={len(d)}")
        if isinstance(d, list) and d:
            print(f"    mau: {json.dumps(d[0], ensure_ascii=False)[:260]}")
        man = (c, d)
        break

# 2) manifest TTS cuc bo
ttm = json.loads((W / "tts_manifest_JA_t02.json").read_text(encoding="utf-8-sig"))
ttm_map = {}
for row in (ttm if isinstance(ttm, list) else ttm.get("items", [])):
    if isinstance(row, dict) and "id" in row:
        ttm_map[row["id"]] = row.get("text")

# 3) so sanh
print("\n=== SO SANH 203 CAU ===")
d_tl_ttm = [i for i in sent if i in ttm_map and sent[i] != ttm_map[i]]
print(f"  timeline vs tts_manifest_JA_t02: KHAC {len(d_tl_ttm)} / {len(sent)}")
for i in d_tl_ttm[:5]:
    print(f"    {i}\n      tl : {sent[i][:95]}\n      ttm: {ttm_map[i][:95]}")

if man:
    c, d = man
    hm = {}
    if isinstance(d, list):
        for row in d:
            if isinstance(row, dict):
                key = row.get("id") or row.get("key") or row.get("sentence_id")
                if key:
                    hm[key] = row.get("text") or row.get("sentence") or ""
    elif isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, str):
                hm[k] = v
    print(f"\n  higgs_manifest: {len(hm)} muc khoa")
    common = [i for i in sent if i in hm]
    diff = [i for i in common if sent[i] != hm[i]]
    print(f"  timeline vs higgs_manifest: giong {len(common)-len(diff)} · KHAC {len(diff)} / {len(sent)}")
    for i in diff[:6]:
        print(f"    {i}\n      tl  : {sent[i][:95]}\n      hig : {hm[i][:95]}")
    if not common:
        print("  (khong khop khoa id — in mau khoa)")
        print("  mau khoa:", list(hm)[:8])
