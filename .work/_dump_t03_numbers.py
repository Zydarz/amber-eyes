#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — in câu đọc của các shot có số trên hình (để soi quy tắc số viết bằng chữ)."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANG = sys.argv[1] if len(sys.argv) > 1 else "ja"
TL = {"vi": "timeline_s_t03.json", "en": "timeline_s_EN_t03.json",
      "ja": "timeline_s_JA_t03.json"}[LANG]
SH = {"vi": "shots_t03.json", "en": "shots_EN_t03.json",
      "ja": "shots_JA_t03.json"}[LANG]

tl = json.loads((WORK / TL).read_text(encoding="utf-8"))
sh = json.loads((WORK / SH).read_text(encoding="utf-8"))
sent = {it["id"]: (it.get("text") or "") for it in tl["items"]}

TARGET = ["1-03", "1-22", "2-05", "2-06", "2-17", "3-03", "3-06", "3-12",
          "4-11", "5-04", "5-07", "5-09"]

for s in sh["shots"]:
    if s["id"] not in TARGET:
        continue
    ids = s.get("sentences") or []
    print(f"--- {s['id']}  [{s.get('template','')}]  bg={s.get('bg')}")
    print(f"    HÌNH : {(s.get('text') or '')[:170]}")
    for i in ids:
        print(f"    CÂU  : {i} -> {sent.get(i,'')[:170]}")
    print()
