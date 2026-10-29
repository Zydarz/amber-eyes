#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Truy vết unit theo số dòng của file VN + trạng thái cache cho tap.

    py -3 .work/_ja_unit_trace.py 01 96 99
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402
from ja_split import split_dialogue_sentences, parts_balanced  # noqa: E402

ep = sys.argv[1]
src = M.canonical_vn(ep)
units = M.assign_turn_counts(M.parse_units(src))
cache = {}
cp = HERE / "ja_cache" / f"tap{ep}.json"
if cp.exists():
    cache = json.loads(cp.read_text(encoding="utf-8"))

print(f"tap{ep}: {len(units)} unit · cache {len(cache)} mục")
for u in units:
    if u["kind"] in ("TEXT", "BULLET"):
        parts = split_dialogue_sentences(u["vi"])
        bal = parts_balanced(parts) if parts else False
        spl = M.splittable(u)
        if u.get("n", 0) >= 3 or (parts and not bal):
            print(f"\n{u['id']} kind={u['kind']} n={u.get('n')} "
                  f"parts={len(parts) if parts else 0} balanced={bal} splittable={bool(spl)}")
            print(f"   VI: {u['vi'][:200]}")
            if parts:
                for k, p in enumerate(parts):
                    ck = f"{u['id']}#{k}"
                    has = cache.get(ck, {}).get("ja", "")
                    print(f"   part{k} [{ck}] cache={'YES' if has else 'NO '} "
                          f"len={len(has)} :: {p[:90]}")
            lk = f"{u['id']}#L"
            print(f"   LINE [{lk}] cache={'YES' if lk in cache else 'NO'}")
