#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap07 — probe: parse 3 scripts, count elements/sentences, compare with timeline/table."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

KB = {
    "vi": "01_KICH_BAN/Tap07/kichban_tap07_23102026.md",
    "en": "01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md",
    "ja": "01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md",
}
for lang, rel in KB.items():
    p = ROOT / rel
    if not p.exists():
        print(f"[{lang}] MISSING {rel}")
        continue
    els = parse_file(str(p))
    loi = [e for e in els if e.get("kind") != "BGM" and e.get("kind") != "SFX"
           and e.get("kind") != "NGHI"]
    n_sent = sum(len(e.get("sentences", [])) for e in loi)
    kinds = {}
    for e in els:
        kinds[e.get("kind")] = kinds.get(e.get("kind"), 0) + 1
    print(f"[{lang}] {rel}")
    print(f"     file mtime={p.stat().st_mtime:.0f}  elements={len(els)}  loi={len(loi)}  sentences={n_sent}")
    print(f"     kinds={kinds}")
    ids = [e["id"] for e in loi]
    print(f"     element ids: {ids[0]} .. {ids[-1]}  ({len(ids)})")

print()
print("=== .work json state ===")
for f in ["script_tap07.json", "script_tap07_EN.json", "script_tap07_JA.json",
          "acting_tap07.json", "acting_tap07_EN.json", "acting_tap07_JA.json",
          "timeline_s_t07.json", "timeline_s_EN_t07.json", "timeline_s_JA_t07.json",
          "shots_t07.json", "shots_EN_t07.json", "shots_JA_t07.json",
          "_t07/_t07_table.json"]:
    p = W / f
    if not p.exists():
        print(f"  {f:34} MISSING")
        continue
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  {f:34} BAD JSON {e}")
        continue
    if isinstance(d, dict):
        if "items" in d:
            n = len(d["items"])
        elif "shots" in d:
            n = len(d["shots"])
        elif "rows" in d:
            n = len(d["rows"])
        else:
            n = "?"
        print(f"  {f:34} OK n={n} total={d.get('total')} keys={list(d.keys())[:5]}")
    else:
        print(f"  {f:34} list len={len(d)}")
