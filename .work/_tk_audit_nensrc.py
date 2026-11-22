# -*- coding: utf-8 -*-
"""Audit NEN_SRC sau khi doi ten nen Tap 03."""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
p = os.path.join(ROOT, ".work", "_build_tk_tap03.py")
s = io.open(p, encoding="utf-8").read()

i = s.index("NEN_SRC = {")
blk = s[i:i + 1800]
pairs = re.findall(r'"(tk03_[a-z0-9_]+)"\s*:\s*"([^"]*)"', blk)
tup = sorted(set(re.findall(r'"(tk03_[a-z0-9_]+)"\s*,\s*"(?:still|pan|push|pull)"', s)))
print("NEN_SRC entries:", len(pairs))
print("bg dung trong clip:", len(tup))
have = set(k for k, _ in pairs)
print("bg thieu trong NEN_SRC:", [t for t in tup if t not in have])
print("NEN_SRC thua:", [k for k, _ in pairs if k not in tup])
for k, v in pairs:
    if any(x in k for x in ("apartos", "galaxie", "small_bed")):
        print("   ", k, "->", v)
print('so cap ngoac kep "" trong file:', s.count('""'))
for m in re.finditer(r'.{30}""[^"]*.{10}', s):
    print("   ctx:", m.group(0).replace("\n", " "))
    break
