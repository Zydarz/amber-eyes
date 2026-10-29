#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử kind 'table' với LLM thật: 2 dòng bảng, kiểm tra số ô khớp."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

items = [
    {"id": "uT1", "vi": "**Tổng thời lượng dự kiến**\t25 – 27 phút (5 hồi nội dung + các khoảng lặng âm thanh kịch tính)",
     "cells": ["**Tổng thời lượng dự kiến**",
               "25 – 27 phút (5 hồi nội dung + các khoảng lặng âm thanh kịch tính)"]},
    {"id": "uT2", "vi": "**Nhạc nền (BGM) gợi ý**\tDark Ambient căng thẳng ngột ngạt, Tiếng cello u tối giằng xé, Tiếng đàn Dương cầm tối giản",
     "cells": ["**Nhạc nền (BGM) gợi ý**",
               "Dark Ambient căng thẳng ngột ngạt, Tiếng cello u tối giằng xé, Tiếng đàn Dương cầm tối giản"]},
]
out = M.call_batch(items, "table", tries=2, ep_tokens=set())
print("\nKẾT QUẢ:")
for it in items:
    ja = out.get(it["id"], "<THIẾU>")
    n = len(ja.split("\t"))
    print(f"  {it['id']}: ô JA={n} (cần {len(it['cells'])}) -> {ja[:160]!r}")
