#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra + (tuỳ chọn) chuẩn hoá _sig của các file cache."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

CACHE = Path(__file__).parent / "ja_cache"
cur = M.cache_signature()
fix = "--fix" in sys.argv
n_ok = n_fix = 0
for p in sorted(CACHE.glob("tap*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    s = d.get("_sig")
    if s == cur:
        n_ok += 1
        continue
    n_fix += 1
    print(f"  {p.name}: _sig={s} -> {cur}  ({len([k for k in d if k.startswith('u')])} muc)")
    if fix:
        d["_sig"] = cur
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\n{n_ok} khop | {n_fix} can chuan hoa{'' if fix else ' (them --fix de ghi)'}")
