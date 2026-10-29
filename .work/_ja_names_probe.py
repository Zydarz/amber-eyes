#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thu thập tên riêng bị gắn cờ 'mất tên' trên toàn bộ file JA đã có."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from _qc_ja import names_of  # noqa: E402

allnames = {}
for i in range(1, 30):
    ep = f"{i:02d}"
    p = M.KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not p.exists():
        continue
    ja = p.read_text(encoding="utf-8")
    vn = M.canonical_vn(ep).read_text(encoding="utf-8")
    for n in names_of(vn):
        if vn.count(n) >= 3 and n not in ja:
            allnames.setdefault(n, []).append(ep)

for n, eps in sorted(allnames.items()):
    print(f"  {n:36s} tap={','.join(eps)}")
print(f"\nTONG: {len(allnames)} ten bi gac co")
