#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê mọi chữ Trung-only còn trong CACHE (nguồn sự thật) kèm ngữ cảnh.

    py -3 .work/_ja_cn_dump.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from _ja_scan_cn_only import CN2JP  # noqa: E402

# loại các ký tự mà dạng giản thạch TRÙNG shinjitai Nhật -> không sửa
SKIP = {k for k, v in CN2JP.items() if k == v}
CHAR = {k: v for k, v in CN2JP.items() if k != v and k not in SKIP}
print("Bo qua (gia tri == khoa):", "".join(sorted(SKIP)))
print()

seen = {}
for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    cache = json.loads(cp.read_text(encoding="utf-8"))
    for k, v in cache.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        ja = v.get("ja", "") or ""
        if not ja:
            continue
        for m in re.finditer("[" + "".join(CHAR) + "]", ja):
            c = m.group(0)
            s = max(0, m.start() - 14)
            e = min(len(ja), m.start() + 14)
            seen.setdefault(c, []).append((ep, k, ja[s:e]))

for c in sorted(seen):
    lst = seen[c]
    print(f"\n=== '{c}' (U+{ord(c):04X}) -> '{CHAR[c]}' : {len(lst)} lan")
    for ep, k, ctx in lst[:4]:
        print(f"    Tap{ep} {k}: {ctx}")
