#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Viết lại 5 dòng cue BGM bị model viết nửa Trung nửa Anh, và sửa detector
để dấu câu Nhật (。、「」…) không bị tính là "dính CJK"."""

import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

APPLY = "--do" in sys.argv

FULL = {
    ("18", "u0273"): "*温かく荘厳な多半奏のBGM。5秒までに完全にフェードアウト。*",
    ("20", "u0277"): "*温かく荘厳な多半奏のBGMが流れ、5秒目で完全にフェードアウトする。*",
    ("21", "u0122"): "*ミニマル・ピアノ（Minimalist Piano）と重低音のドローン音が重なり、専門深い学術・臨床分析の雰囲気が支配する。*",
    ("22", "u0122"): "*ミニマルピアノが重厚でくぐもったドローン音と重なり、学術的・臨床分析的な雰囲気が漂う。*",
    ("24", "u0122"): "*ミニマルなピアノの音が、深く沈んだドローン音と重なり、学術的で綿密な臨床分析の雰囲気が満ちる。*",
}


def main():
    miss = []
    files = {}
    for (ep, key), new in FULL.items():
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        if ep not in files:
            files[ep] = (cp, json.loads(cp.read_text(encoding="utf-8")))
        d = files[ep][1]
        v = d.get(key)
        if not isinstance(v, dict):
            miss.append((ep, key))
            continue
        print(f"  Tap{ep} {key}\n     OLD: {v.get('ja')}\n     NEW: {new}")
        v["ja"] = new
    if miss:
        print("KHONG TIM THAY:", miss)
    if not APPLY:
        print("\nDRY-RUN. Them --do de ghi.")
        return
    for ep, (cp, d) in files.items():
        shutil.copy2(cp, cp.with_suffix(".json.bak_bgm"))
        cp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"   da ghi tap{ep}.json")


if __name__ == "__main__":
    main()
