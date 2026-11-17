# -*- coding: utf-8 -*-
"""Tập 12 — xuất danh sách nhóm nền (KEEP/NEW) kèm nội dung câu để viết prompt."""
import collections
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = json.loads(Path(".work/_t12_chunks.json").read_text(encoding="utf-8"))
ch = d["chunks"]
seen = collections.Counter()
lines = []
for i, c in enumerate(ch):
    seen[c["parent"]] += 1
    tag = "KEEP" if seen[c["parent"]] == 1 else "NEW"
    txt = " ~ ".join(x.strip("*")[:130] for x in c["chus"])
    caus = "|".join(c["caus"])
    lines.append(f'{tag} #{i:3d} {c["parent"]:42s} n={c["n"]} {c["sec"]:5.1f}s {caus:26s} {txt}')
Path(".work/_t12_chunk_list.txt").write_text("\n".join(lines), encoding="utf-8")
new = [l for l in lines if l.startswith("NEW")]
print(f"total {len(lines)} | NEW {len(new)}")
if "--new" in sys.argv:
    print("\n".join(new))
