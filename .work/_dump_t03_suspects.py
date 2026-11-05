#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — soi 4 shot nghi vấn (1-01, 5-02 ở VN/EN): chữ trên hình vs câu đọc."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

CASES = [
    ("vi", "timeline_s_t03.json", "shots_t03.json", ["1-01", "5-02"]),
    ("en", "timeline_s_EN_t03.json", "shots_EN_t03.json", ["1-01", "5-02"]),
    ("ja", "timeline_s_JA_t03.json", "shots_JA_t03.json", ["1-01", "5-02"]),
]

for lang, tl_name, sh_name, targets in CASES:
    tl = json.loads((WORK / tl_name).read_text(encoding="utf-8"))
    sh = json.loads((WORK / sh_name).read_text(encoding="utf-8"))
    sent = {it["id"]: (it.get("text") or "") for it in tl["items"]}
    print("=" * 80)
    print(f"[{lang}]")
    for s in sh["shots"]:
        if s["id"] not in targets:
            continue
        print(f"--- {s['id']}  template={s.get('template')}  bg={s.get('bg')}")
        for seg in s.get("segments") or []:
            at = seg.get("at_sentence")
            for el in seg.get("elems") or []:
                print(f"    [seg @{at}] {el[0]:6} | {el[1]}")
        print("    CÂU ĐỌC:")
        for i in s.get("sentences") or []:
            print(f"      {i}: {sent.get(i,'')}")
        print()
