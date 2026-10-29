#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem chính xác ký tự lạ trong bản dịch JA (repr + codepoint)."""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M

ep = sys.argv[1] if len(sys.argv) > 1 else "02"
ids = sys.argv[2:] or ["u0018", "u0029", "u0035"]

units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
cache = json.loads((M.CACHE_DIR / f"tap{ep}.json").read_text(encoding="utf-8"))
for uid in ids:
    ja = cache.get(uid, {}).get("ja", "")
    print("=" * 70)
    print(uid, "len =", len(ja))
    for i, ch in enumerate(ja):
        o = ord(ch)
        if o > 127 and not (0x3000 <= o <= 0x30FF) and not (0x4E00 <= o <= 0x9FFF) \
           and not (0xFF00 <= o <= 0xFFEF):
            print(f"  [{i}] {ch!r} U+{o:04X}  ctx={ja[max(0,i-12):i+12]!r}")
    # ký tự fullwidth latin
    fw = [(i, ch) for i, ch in enumerate(ja) if 0xFF01 <= ord(ch) <= 0xFF5E]
    if fw:
        print("  fullwidth:", fw[:10])
