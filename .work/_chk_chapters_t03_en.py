#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra khoi mo ta co moc CHAPTERS (package.py description_en() se SystemExit neu thieu)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
FENCE = chr(96) * 3
tpl = Path("D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap03_EN/CHU_CO_DINH_EN.md").read_text(encoding="utf-8")
blocks = re.findall(re.escape(FENCE) + r"(?:text)?\n(.*?)" + re.escape(FENCE), tpl, re.S)
best = None
for b in blocks:
    if "CHAPTERS" in b:
        best = b
print("so khoi ``` :", len(blocks), "| co khoi CHAPTERS:", best is not None)
if best:
    print("--- 700 ky tu dau ---")
    print(best[:700])
