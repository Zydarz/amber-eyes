#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 + tham chiếu — soi THẺ KẾT (shot cuối) của các tập đã xuất bản."""
import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

CASES = [
    ("tap03 VN", "03", ""), ("tap03 EN", "03", "en"), ("tap03 JA", "03", "ja"),
    ("tap02 VN", "02", ""), ("tap02 EN", "02", "en"), ("tap02 JA", "02", "ja"),
    ("tap01 VN", "01", ""), ("tap04 VN", "04", ""), ("tap04 JA", "04", "ja"),
    ("tap05 VN", "05", ""),
]

for label, ep, lang in CASES:
    os.environ["AE_EP"] = ep
    os.environ["AE_LANG"] = lang
    for m in [m for m in list(sys.modules) if m == "edition"]:
        del sys.modules[m]
    sys.path.insert(0, str(WORK))
    import edition as ED
    p = ED.w("shots.json")
    if not p.exists():
        print(f"[{label}] chua co {p.name}")
        continue
    sh = json.loads(p.read_text(encoding="utf-8"))
    last = sh["shots"][-1]
    print("=" * 76)
    print(f"[{label}]  shot cuối = {last['id']}  template={last.get('template')}  "
          f"bg={last.get('bg')}  {last['start']}->{last['end']}s")
    for seg in last.get("segments") or []:
        for el in seg.get("elems") or []:
            print(f"     {el[0]:6} | {el[1]}")
    print(f"     beat_text = {last.get('beat_text')}")
