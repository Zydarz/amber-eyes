#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump RAW cache entries của các mục nhiễm (để lấy chuỗi chính xác, kể cả ô bảng).

    py -3 .work/_ja_dump_raw.py 06 15 28
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

RX_CJK = re.compile(r"[\u3400-\u9fff]+")
RX_HANGUL = re.compile(r"[\u3131-\u318e\uac00-\ud7a3]+")
RX_LATIN_JUNK = re.compile(r"[A-Za-z]{4,}")

TARGET = [a.zfill(2) for a in sys.argv[1:]] or [f"{i:02d}" for i in range(1, 30)]


def bad(ja):
    if any(c in M.CN_ONLY_CHARS for c in ja):
        return True
    if RX_HANGUL.search(ja):
        return True
    # rác: chữ Latin >=4 ký tự đứng lẻ giữa CJK (không phải tên riêng Latin)
    for m in RX_LATIN_JUNK.finditer(ja):
        w = m.group(0)
        before = ja[max(0, m.start() - 1):m.start()]
        after = ja[m.end():m.end() + 1]
        if before and (ord(before[-1]) > 0x2E80 or after and ord(after[0]) > 0x2E80):
            return True
    return False


for ep in TARGET:
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    d = json.loads(cp.read_text(encoding="utf-8"))
    for k, v in d.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        ja = v.get("ja", "")
        if not isinstance(ja, str) or not ja:
            continue
        if bad(ja):
            print(f"\n--- Tap{ep} {k}  ({v.get('kind','?')}) ---")
            print(ja)
