#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra manifest Higgs THAT SU (prod + r2) co doc dung text cua timeline khong."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it["text"] for it in tl["items"]}

for c in sorted(W.glob("kaggle_higgs/**/higgs_manifest.json")):
    d = json.loads(c.read_text(encoding="utf-8-sig"))
    if not isinstance(d, list) or not d:
        continue
    print("=" * 72)
    print(f"{c.relative_to(ROOT)}  ({len(d)} dong)")
    rows = []
    for r in d:
        if not isinstance(r, dict):
            continue
        sid = r.get("id")
        txt = r.get("text_sent") or r.get("text_plain") or r.get("text") or ""
        if sid:
            rows.append((sid, txt))
    ids = {r[0] for r in rows}
    print(f"  cau duy nhat: {len(ids)} / 203")
    same = [i for i, t in rows if i in sent and norm_eq(t, sent[i])] if False else None

    def n(t):
        import re
        return re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t)

    diff = [(i, t) for i, t in rows if i in sent and n(t) != n(sent[i])]
    cover = [i for i in sent if i in ids]
    print(f"  phu timeline: {len(cover)}/203 · KHAC text: {len(diff)}")
    for i, t in diff[:4]:
        print(f"    {i}\n      tl : {sent[i][:90]}\n      man: {t[:90]}")
    # cau trong manifest nhung timeline khong co
    extra = ids - set(sent)
    if extra:
        print(f"  cau trong manifest khong co trong timeline: {len(extra)} {sorted(extra)[:6]}")
