#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem các mục dịch hỏng trong cache + nguyên văn VN của chúng."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

WORK = Path(__file__).parent
ep = sys.argv[1] if len(sys.argv) > 1 else "01"
cache = json.loads((WORK / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}

missing = []
for u in units:
    if u["kind"] == "RAW":
        continue
    if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
        parts = M.splittable(u)
        if parts:
            for k, p in enumerate(parts):
                jid = f"{u['id']}#{k}"
                if not cache.get(jid, {}).get("ja"):
                    missing.append((jid, u, p))
        else:
            jid = f"{u['id']}#L"
            if not cache.get(jid, {}).get("ja"):
                missing.append((jid, u, u["vi"]))
    else:
        if not cache.get(u["id"], {}).get("ja"):
            missing.append((u["id"], u, u["vi"]))

print(f"Tap{ep}: {len(missing)} mục thiếu\n")
for jid, u, part in missing:
    print(f"--- {jid}  kind={u['kind']} n={u.get('n')}")
    print(f"    VN đơn vị : {u['vi'][:220]}")
    print(f"    VN phần   : {part[:220]}")
    print(f"    marker    : **={part.count('**')} *={part.count('*')}")
    print()
