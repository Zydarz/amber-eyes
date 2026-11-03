#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In bang doi chieu CU | MOI theo tung element (de xac minh bang do id)."""
import json
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"

old_s = json.loads(subprocess.run(["git", "show", "HEAD:.work/script_tap07.json"],
                                  cwd=ROOT, capture_output=True, text=True,
                                  encoding="utf-8").stdout)
new_s = json.loads((W / "script_tap07.json").read_text(encoding="utf-8-sig"))


def by_el(script):
    d = {}
    for it in script:
        if it.get("kind") not in ("LOI", "NGHI"):
            continue
        d.setdefault(it["id"], []).extend(
            (s["id"], s["text"].replace("“", '"').replace("”", '"'))
            for s in it.get("sentences", []))
    return d


o, n = by_el(old_s), by_el(new_s)
for el in sorted(set(o) | set(n)):
    ol, nl = o.get(el, []), n.get(el, [])
    if len(ol) == len(nl) and [x[1] for x in ol] == [x[1] for x in nl]:
        continue                      # giong het -> bo qua
    print("=" * 100)
    print(f"ELEMENT {el}   CU={len(ol)}  MOI={len(nl)}")
    print("=" * 100)
    for i in range(max(len(ol), len(nl))):
        oc = f"{ol[i][0]:>9} | {ol[i][1][:110]}" if i < len(ol) else " " * 9 + " |" + " " * 110
        nc = f"{nl[i][0]:>9} | {nl[i][1][:110]}" if i < len(nl) else " " * 9 + " |" + " " * 110
        print(f"  CU  {oc}")
        print(f"  MOI {nc}")
        print()
