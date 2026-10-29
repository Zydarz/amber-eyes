#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đọc lại các dòng đã sửa tay / sửa bằng LLM để kiểm tra văn phong."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import make_ja_scripts as M  # noqa: E402

SHOW = [
    ("01", "u0009"), ("02", "u0195#1"), ("04", "u0092#0"), ("06", "u0007"),
    ("08", "u0152#0"), ("11", "u0099#4"), ("13", "u0058#5"), ("14", "u0062"),
    ("14", "u0086"), ("16", "u0010"), ("16", "u0060#0"), ("18", "u0273"),
    ("19", "u0269#0"), ("21", "u0122"), ("22", "u0122"), ("24", "u0122"),
    ("25", "u0240#0"), ("26", "u0256#0"), ("27", "u0136#0"), ("28", "u0047#0"),
    ("28", "u0146#0"), ("28", "u0252#0"), ("29", "u0063#0"),
]

import json
for ep, key in SHOW:
    d = json.loads((HERE / "ja_cache" / f"tap{ep}.json").read_text(encoding="utf-8"))
    ja = d.get(key, {}).get("ja", "")
    print(f"[Tap{ep} {key}]")
    print(f"  {ja}")
    print()
