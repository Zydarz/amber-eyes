#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đếm các dòng kiểu '**nhãn:** nội dung' trong 29 kịch bản (dòng metadata, không phải thoại)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

RE_LABELED = re.compile(r"^\*\*[^*]{1,40}\*\*\s+\S")
tot = 0
for i in range(1, 30):
    ep = f"{i:02d}"
    src = M.canonical_vn(ep)
    hits = []
    for ln in src.read_text(encoding="utf-8").splitlines():
        s = ln.strip()
        if RE_LABELED.match(s):
            hits.append(s[:90])
    tot += len(hits)
    if hits:
        print(f"Tap{ep}: {len(hits)}")
        for h in hits[:4]:
            print("    ", h)
print("TỔNG:", tot)
