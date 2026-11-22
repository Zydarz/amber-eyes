# -*- coding: utf-8 -*-
"""Them mapping thieu cho NEN_SRC trong _build_tk_tap03.py.

Generator goc chi co 27/28 mapping (thieu t3_self_observation) => QC row 8
("Nguon 16:9 cua 28 nen co trong assets/bg/_raw/") se bao thieu raw.
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
p = os.path.join(ROOT, ".work", "_build_tk_tap03.py")

s = io.open(p, encoding="utf-8").read()
old = ' "tk03_life_sentence": "t3_life_sentence",\n}'
new = (' "tk03_life_sentence": "t3_life_sentence",\n'
       ' "tk03_self_observation": "t3_self_observation",\n}')
if old not in s:
    print("KHONG tim thay khoi can them")
    sys.exit(1)
s = s.replace(old, new, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("da them tk03_self_observation -> t3_self_observation")
