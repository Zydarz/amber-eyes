# -*- coding: utf-8 -*-
"""Đo mốc chương (act start) thật cho Tập 17 mọi ngôn ngữ — logic y hệt package.act_start_times."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent


def mmss(t):
    t = int(t + 0.5)
    return f"{t // 60:02d}:{t % 60:02d}"


for tag, fn in [("VI", "timeline_s_t17.json"), ("EN", "timeline_s_EN_t17.json"),
                ("JA", "timeline_s_JA_t17.json"), ("KO", "timeline_s_KO_t17.json")]:
    p = W / fn
    if not p.exists():
        print(f"[{tag}] THIEU {fn}")
        continue
    tl = json.loads(p.read_text(encoding="utf-8"))
    starts = {}
    for it in tl.get("items", []):
        a = it.get("act")
        if a and a not in starts:
            starts[a] = it["start"]
    if not starts:
        for m in tl.get("markers", []):
            if m.get("type") == "ACT":
                starts[m["act"]] = m["start"]
    print(f"[{tag}] total={tl.get('total')} items={len(tl.get('items', []))} intro={tl.get('intro')}")
    for a in sorted(starts):
        print(f"    act{a}: {starts[a]:8.2f}s -> {mmss(starts[a])}")
