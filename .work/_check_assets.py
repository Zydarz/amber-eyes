#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rà xem mã SFX nào trong bảng mục 4 chưa có file trong assets/sfx/."""
import io
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
TICK = chr(96)

out = {}
for line in io.open(DOC, encoding="utf-8").read().splitlines():
    p = [x.strip() for x in line.split("|")]
    if len(p) < 6 or not p[2].startswith(TICK):
        continue
    name = p[2].strip(TICK)
    dest = p[5].strip(TICK)
    if name.endswith(".wav") and dest.startswith("assets/sfx/"):
        out[name[:-4]] = dest

print("doc ma:", len(out))
missing = [m for m, d in out.items() if not (ROOT / d).exists()]
print("THIEU file:", len(missing))
for m in sorted(missing):
    print("  ", m, "->", out[m])
