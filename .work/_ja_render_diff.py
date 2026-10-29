#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng lại file JA từ cache và so với file đang có trên đĩa."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

ep = sys.argv[1] if len(sys.argv) > 1 else "01"
cache = json.loads((M.WORK / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
in_turn = {u["id"] for t in M.group_turns(units) for u in t["units"]}

for u in units:
    if u["kind"] == "RAW":
        continue
    if u["kind"] in ("TEXT", "BULLET") and u["id"] in in_turn:
        parts = M.splittable(u)
        if parts:
            got = [cache.get(f"{u['id']}#{k}", {}).get("ja", "") for k in range(len(parts))]
            u["ja"] = "".join(got) if all(got) else ""
        else:
            u["ja"] = cache.get(f"{u['id']}#L", {}).get("ja", "")
    else:
        u["ja"] = cache.get(u["id"], {}).get("ja", "")

new = M.render(units)
p = M.KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
old = p.read_text(encoding="utf-8")
head = old.split("\n")[0]
new_full = head + "\n" + old.split("\n")[1] + "\n" + new

old_lines = old.splitlines()
new_lines = new_full.splitlines()
print(f"Tap{ep}: file {len(old_lines)} dòng · dựng lại {len(new_lines)} dòng")
import difflib
diff = list(difflib.unified_diff(old_lines, new_lines, "trên đĩa", "dựng lại", lineterm="", n=1))
if not diff:
    print("GIỐNG HỆT")
else:
    print(f"KHÁC Ở {len(diff)} dòng:")
    for d in diff[:60]:
        print("   ", d[:200])
