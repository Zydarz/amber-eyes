#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sánh cache trước/sau một bản vá."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).parent

old_p = Path(sys.argv[1])
new_p = Path(sys.argv[2])
b = json.loads(old_p.read_text(encoding="utf-8"))
n = json.loads(new_p.read_text(encoding="utf-8"))
for k in sorted(set(b) | set(n)):
    bv = b.get(k)
    nv = n.get(k)
    bj = bv.get("ja") if isinstance(bv, dict) else bv
    nj = nv.get("ja") if isinstance(nv, dict) else nv
    if bj != nj:
        print("KEY", k)
        print("  OLD:", bj)
        print("  NEW:", nj)
