#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gộp 5 file _ovl_act*.json thành .work/shots_text_tap02_JA.json (thứ tự mã shot)."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).resolve().parent

merged = {}
for a in range(1, 6):
    p = W / f"_ovl_act{a}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    for k, v in d.items():
        if k in merged:
            print("TRUNG MA:", k)
        merged[k] = v

ROOT = W.parent
vn = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn) if i > i0 and l.startswith("**Tổng:"))
order = []
for l in vn[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if m:
        order.append(m.group(1))

missing = [k for k in order if k not in merged]
extra = [k for k in merged if k not in order]
if missing:
    print("THIEU:", missing)
if extra:
    print("THUA:", extra)
if missing or extra:
    sys.exit(1)

out = {"_note": "shot_id -> [chu_JA, [ja_beat_phrase_1, ...], beat_override|null]"}
for k in order:
    out[k] = merged[k]

dest = W / "shots_text_tap02_JA.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"Da ghi {dest} · {len(out) - 1} shot")
