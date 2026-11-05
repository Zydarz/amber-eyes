#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
d = Path("D:/TEST/Gax/amber-eyes/.work/_en_repr.txt").read_text(encoding="utf-8")
print(sorted(set(re.findall(r"\\u[0-9a-f]{4}", d))))
print("---- lines with smart quotes ----")
for line in d.splitlines():
    if "\\u201" in line:
        print(line)
