#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sửa 2 lỗi cuối:
  Tap16/u0060#0 - 'Áo' là 'Áo(Âustria)' bị bỏ sót + sai số (VN: 9 ly -> JA 22口径).
                    Đối chiếu bản EN: 'a twenty-two caliber target revolver and an
                    Austrian-made nine-millimeter semi-automatic pistol'.
  Tap28/u0146#0 - cụm tiếng Việt 'Hội chứng Chuột cùng đường' còn sót trong ngoặc
                    kép Nhật -> dùng đúng thuật ngữ của tập.

    py -3 .work/_ja_fix_last2.py --do
"""
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
APPLY = "--do" in sys.argv

FIX = {
    ("16", "u0060#0"):
        "犯人は、22口径のスポーツ用銃と、オーストリア製の9口径半自動銃という2種類の異なる銃を使用していました。",
    ("28", "u0146#0"):
        "ところが、店主が突然目を覚まし、侵入者を見つけた瞬間、極めて危険な心理反応、すなわち「追い詰められたネズミ症候群」が起動した。",
}

for (ep, key), new in FIX.items():
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    d = json.loads(cp.read_text(encoding="utf-8"))
    print(f"Tap{ep} {key}\n  OLD: {d[key]['ja']}\n  NEW: {new}")
    d[key]["ja"] = new
    if APPLY:
        shutil.copy2(cp, cp.with_suffix(".json.bak_last"))
        cp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  -> da ghi tap{ep}.json")
print("OK" if APPLY else "DRY-RUN")
