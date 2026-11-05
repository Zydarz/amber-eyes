#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — in danh sách gọn 89 lớp phủ VN (để soi cấu trúc khi viết JA)."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent

sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
chu = json.loads((W / "_t04_chu_vn.json").read_text(encoding="utf-8"))
shots = [r for r in sk["rows"] if r["kind"] == "shot"]
for r in shots:
    parts = re.split(r"\s+→\s+", chu.get(r["sid"], ""))
    struct = " || ".join(p for p in parts)
    print(f"{r['sid']:6s} [{r['cells'][3]:10s}] {struct}")
