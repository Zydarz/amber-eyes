#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử phiên âm Latin -> Katakana trên các tên địa danh thật."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ja_kana import to_katakana  # noqa: E402

for n in ["New Jersey", "Missouri", "California", "Milwaukee", "Berlin", "Tokyo",
          "Schichtingen", "Texas", "Florida", "Dee Dee Blanchard", "Hong Kong",
          "San Francisco", "Virginia", "Ohio", "Seattle"]:
    print(f"  {n:20s} -> {to_katakana(n)}")
