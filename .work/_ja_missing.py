#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem các mục dịch hỏng của một tập + thử dịch lại từng mục để xem lỗi."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
import ja_llm  # noqa: E402

ep = sys.argv[1] if len(sys.argv) > 1 else "01"
units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
cache = json.loads((M.CACHE_DIR / f"tap{ep}.json").read_text(encoding="utf-8"))
missing = [u for u in units if u["kind"] != "RAW" and u["id"] not in cache]
print(f"Tap{ep}: {len(missing)} mục thiếu")
for u in missing:
    print("=" * 70)
    print(u["id"], u["kind"], "n =", u.get("n"))
    print("VI:", u["vi"][:300])
    for kind in ("dialogue", "meta"):
        try:
            txt = ja_llm.call(M.build_prompt([u], kind), M.STYLE, model=M.MODEL,
                              max_tokens=4000, temperature=0.15, timeout=180)
            print(f"  -> {kind}: {txt[:600]}")
            try:
                rows = M.parse_json_array(txt)
                ja = rows[0]["ja"]
                ok, why = M.check_unit(u, ja, kind)
                print(f"     check: {'OK' if ok else 'FAIL - ' + why} | JA={ja[:200]}")
            except Exception as e:
                print("     parse lỗi:", e)
        except Exception as e:
            print(f"  -> {kind}: LỖI {e}")
