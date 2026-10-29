#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trích MỌI cụm nhiễm (cụm CJK chứa ký tự Trung-only, cụm Hangul) trong cache.

    py -3 .work/_ja_extract_runs.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

RX_CJK = re.compile(r"[\u3400-\u9fff]+")
RX_HANGUL = re.compile(r"[\u3131-\u318e\uac00-\ud7a3]+")

runs_cn = {}
runs_ko = {}
for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    d = json.loads(cp.read_text(encoding="utf-8"))
    for k, v in d.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        ja = v.get("ja", "") or ""
        if not ja:
            continue
        for m in RX_CJK.finditer(ja):
            r = m.group(0)
            if any(c in M.CN_ONLY_CHARS for c in r):
                runs_cn.setdefault(r, []).append((ep, k))
        for m in RX_HANGUL.finditer(ja):
            r = m.group(0)
            runs_ko.setdefault(r, []).append((ep, k))

print("=" * 70)
print("CUM CJK CO CHU TRUNG-ONLY  (theo do dai tang dan)")
print("=" * 70)
for r in sorted(runs_cn, key=lambda x: (-len(x), x)):
    where = ", ".join(f"Tap{e}/{k}" for e, k in runs_cn[r][:4])
    print(f"  {r:<16} x{len(runs_cn[r]):<3} {where}")

print()
print("=" * 70)
print("CUM HANGUL")
print("=" * 70)
for r in sorted(runs_ko, key=lambda x: (-len(x), x)):
    where = ", ".join(f"Tap{e}/{k}" for e, k in runs_ko[r][:4])
    print(f"  {r:<16} x{len(runs_ko[r]):<3} {where}")
