#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So từng dòng thoại VN vs JA, in ra dòng nào lệch số câu."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from ja_split import ja_sentences  # noqa: E402

ep = sys.argv[1] if len(sys.argv) > 1 else "03"
units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}

cache = {}
import json
p = M.WORK / "ja_cache" / f"tap{ep}.json"
if p.exists():
    cache = json.loads(p.read_text(encoding="utf-8"))

print(f"===== Tap{ep}: so từng dòng =====")
for u in units:
    if u["kind"] not in ("TEXT", "BULLET") or u["id"] not in in_turn:
        continue
    parts = M.splittable(u)
    if parts:
        got = [cache.get(f"{u['id']}#{k}", {}).get("ja", "") for k in range(len(parts))]
        if all(got):
            ja = "".join(got)
        else:
            ja = ""
    else:
        ja = cache.get(f"{u['id']}#L", {}).get("ja", "")
    need = u.get("n", 0)
    got_n = ja_sentences(ja) if ja else -1
    if got_n != need:
        print(f"\n!!! {u['id']}  cần={need}  được={got_n}  loại={u['kind']} "
              f"tách={bool(parts)}")
        print(f"   VN : {u['vi'][:200]}")
        print(f"   JA : {ja[:200]}")
        print(f"   cache keys: {[k for k in cache if k.startswith(u['id'])]}")
