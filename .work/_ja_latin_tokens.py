#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trích TẤT CẢ token Latin trong 29 file JA, đếm số lần, để soi phần rác.

    py -3 .work/_ja_latin_tokens.py
"""
import collections
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
KB = ROOT / "01_KICH_BAN"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cnt = collections.Counter()
where = collections.defaultdict(list)
rx = re.compile(r"[A-Za-z][A-Za-z_']*")

for i in range(1, 30):
    ep = "%02d" % i
    f = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not f.exists():
        continue
    for ln_no, ln in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        for m in rx.finditer(ln):
            w = m.group(0)
            cnt[w] += 1
            if len(where[w]) < 3:
                s = max(0, m.start() - 22)
                where[w].append(f"Tap{ep} d{ln_no}: ...{ln[s:m.start()+30]}...")

print(f"{'token':<24}{'so':>5}  vi du")
for w, n in cnt.most_common():
    print(f"{w:<24}{n:>5}  {where[w][0][:120]}")
print(f"\nTONG {len(cnt)} token khac nhau")
