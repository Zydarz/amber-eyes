#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê chi tiết các unit của 1 tập: id, kind, số câu VN, và từng câu JA trong cache.

    py -3 .work/_ja_dump_unit.py 03
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
from ja_split import split_dialogue_sentences  # noqa: E402

ep = sys.argv[1]
only = sys.argv[2] if len(sys.argv) > 2 else None

units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
byid = {u["id"]: u for u in units}
cache = json.loads((HERE / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))

for u in units:
    if u["kind"] not in ("TEXT", "BULLET"):
        continue
    parts = split_dialogue_sentences(u["vi"])
    if u.get("n", 0) < 2 and not only:
        continue
    if only and u["id"] != only:
        continue
    jid = f"{u['id']}#L"
    in_cache = jid in cache
    print(f"== {u['id']} kind={u['kind']} n={u.get('n')} "
          f"parts={len(parts)} cache#L={'CÓ' if in_cache else 'KHÔNG'}")
    if not in_cache:
        # thử dựng lại từ các câu #k
        ks = [k for k in cache if k.startswith(u["id"] + "#")]
        for k in sorted(ks):
            ja = cache[k].get("ja", "") if isinstance(cache[k], dict) else ""
            print(f"   {k}: {ja[:160]}")
        print()
        continue
    ja = cache[jid].get("ja", "")
    print(f"   JA dòng: {ja[:600]}")
    print(f"   câu JA  : {len(M.ja_sentences(ja))}")
    print(f"   VN parts: {parts[:8]}")
    print()
