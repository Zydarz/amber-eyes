#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Khôi phục thuật ngữ glossary '覚醒の教訓' trong dòng bài kết Tap19
(bản dịch lại bằng LLM đã làm mất cụm này).

    py -3 .work/_ja_fix_term19.py --do
"""
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
APPLY = "--do" in sys.argv

NEW = ("本日は、「犯罪心理学事件簿」でAmber Eyesとともに時間を費やし、"
       "胸を痛める残酷な出来事と深い覚醒の教訓に満ちた回にお付き合いいただき、ありがとうございます。")

cp = HERE / "ja_cache" / "tap19.json"
d = json.loads(cp.read_text(encoding="utf-8"))
print("OLD:", d["u0274#0"]["ja"])
print("NEW:", NEW)
d["u0274#0"]["ja"] = NEW
if APPLY:
    shutil.copy2(cp, cp.with_suffix(".json.bak_term"))
    cp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print("da ghi tap19.json")
else:
    print("DRY-RUN")
