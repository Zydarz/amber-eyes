#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét NHIỄM NGÔN NGỮ trong cache JA: Hàn Quốc, Trung giản thạch, rác Latin,
tiếng Việt sót.

    py -3 .work/_ja_scan_contamination.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from _ja_scan_cn_only import CN2JP  # noqa: E402

SKIP = {k for k, v in CN2JP.items() if k == v}
CN_ONLY = {k for k, v in CN2JP.items() if k != v and k not in SKIP}

RX_HANGUL = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
RX_JUNK = re.compile(r"(?<!<)_(?=[A-Za-z])")
# tiếng Việt sót: chữ có dấu nối trong từ (trừ tên riêng đã biết)
VN_DIAC = re.compile(r"[àáảãạăâđêôơưÀÁẢÃẠĂÂĐÊÔƠƯ]")

rows = []
for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    cache = json.loads(cp.read_text(encoding="utf-8"))
    for k, v in cache.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        ja = v.get("ja", "") or ""
        if not ja:
            continue
        why = []
        if RX_HANGUL.search(ja):
            why.append("HANGUL")
        cn = sorted({c for c in ja if c in CN_ONLY})
        if cn:
            why.append("CN:" + "".join(cn))
        if RX_JUNK.search(ja):
            why.append("JUNK_")
        vn = sorted({c for c in ja if c in "àáảãạăâđêôơư"})
        if vn:
            why.append("VN:" + "".join(vn))
        if why:
            rows.append((ep, k, ",".join(why), ja))

by_ep = {}
for ep, k, why, ja in rows:
    by_ep.setdefault(ep, []).append((k, why, ja))

tot = 0
for ep in sorted(by_ep):
    lst = by_ep[ep]
    tot += len(lst)
    print(f"\n===== Tap{ep}: {len(lst)} muc nhiem")
    for k, why, ja in lst:
        print(f"  {k:<12} [{why}]")
        print(f"      {ja[:150]}")
print(f"\nTONG {tot} muc nhiem / {len(by_ep)} tap")
print("Tap:", " ".join(sorted(by_ep)))
