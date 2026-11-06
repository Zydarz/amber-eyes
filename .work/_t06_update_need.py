#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — cập nhật EPISODES['06']['need'] (các câu cần nguồn) theo kịch bản mới 212 câu."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

NEW = [
    # Hồi 1
    "1.02#1", "1.02#2", "1.02#4", "1.02#5", "1.02#6", "1.02#7", "1.02#8",
    "1.06#1", "1.06#2", "1.06#3", "1.06#4", "1.06#6", "1.06#7",
    "1.08#1", "1.08#3", "1.08#6",
    "1.09#1", "1.09#2",
    "1.11#2", "1.13#1", "1.14#2", "1.16#1",
    # Hồi 2
    "2.03#1", "2.03#2", "2.03#3", "2.03#4",
    "2.04#1", "2.04#2", "2.04#3", "2.04#4", "2.04#5", "2.04#6", "2.04#7",
    "2.05#2",
    "2.07#3", "2.07#4", "2.07#5", "2.07#6",
    "2.08#1", "2.08#2", "2.08#3",
    "2.09#3", "2.09#4", "2.09#7",
    "2.10#3", "2.10#4", "2.10#7", "2.10#8",
    "2.11#1", "2.11#2",
    "2.12#1", "2.12#2",
    # Hồi 3
    "3.02#1", "3.02#2",
    "3.03#1", "3.03#2", "3.03#3",
    "3.06#1", "3.06#2",
    "3.08#1", "3.08#2", "3.08#3",
    "3.10#1", "3.10#2", "3.10#4", "3.10#6", "3.10#7",
    "3.11#3", "3.11#4", "3.11#9", "3.11#12", "3.11#13",
    "3.12#1",
    # Hồi 4
    "4.03#2", "4.03#3",
    "4.05#1", "4.05#2", "4.05#3", "4.05#4",
    "4.06#1",
    "4.07#1", "4.07#2", "4.07#3", "4.07#4",
    "4.08#1",
    "4.09#2", "4.09#4",
    "4.10#1", "4.10#2",
    "4.11#1", "4.11#3", "4.11#4",
    # Hồi 5
    "5.02#1", "5.02#3", "5.02#4",
    "5.04#1", "5.04#2",
    "5.06#4", "5.06#5", "5.06#6", "5.06#8",
]

els = parse_file(str(ROOT / "01_KICH_BAN/Tap06/kichban_tap06_23102026.md"))
have = {}
for e in els:
    if e.get("kind") == "LOI":
        for s in e.get("sentences", []):
            have[s["id"]] = s["text"]

bad = [k for k in NEW if k not in have]
if bad:
    print("✗ không tồn tại trong kịch bản:", bad)
    sys.exit(1)
print(f"✓ {len(NEW)} mục hợp lệ")
print("```python")
print('        "need": [')
line = "                "
for i, k in enumerate(NEW):
    piece = f'"{k}"' + ("," if i < len(NEW) - 1 else "],")
    if len(line) + len(piece) > 92:
        print(line)
        line = "                "
    line += piece + " "
print(line)
print("```")
