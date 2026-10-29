#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So từng lượt: parser chính (parse_kichban) vs cách gom của pipeline JA."""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

WORK = Path(__file__).parent
ep = sys.argv[1] if len(sys.argv) > 1 else "01"
src = M.canonical_vn(ep)
out = WORK / f"_ja_parse_{ep}.json"
subprocess.run([sys.executable, str(WORK / "parse_kichban.py"), str(src), str(out)], check=True,
               capture_output=True)
els = json.loads(out.read_text(encoding="utf-8"))
official = [e for e in els if e["kind"] == "LOI"]

units = M.assign_turn_counts(M.parse_units(src))
turns = M.group_turns(units)

lines = [f"=== Tap{ep}: parser {len(official)} lượt / JA {len(turns)} lượt ==="]
for i in range(max(len(official), len(turns))):
    o = official[i] if i < len(official) else None
    t = turns[i] if i < len(turns) else None
    oc = len(o["sentences"]) if o else 0
    jn = sum(u.get("n", 0) for u in t["units"]) if t else -1
    mark = " " if oc == jn else "X"
    ot = (o["text"][:70].replace("\n", " ") if o else "-")
    jt = (" | ".join(x["vi"][:34].replace("\n", " ") for x in t["units"])[:70] if t else "-")
    lines.append(f"{mark} [{i+1:02d}] parser role={o['role'] if o else '-':2} n={oc:3} | {ot}")
    lines.append(f"      JA  role={t['role'] if t else '-':2} n={jn:3} | {jt}")
txt = WORK / f"_ja_turns_{ep}.txt"
txt.write_text("\n".join(lines), encoding="utf-8")
print(f"written {txt} · lệch {sum(1 for l in lines if l.startswith('X'))} lượt")
