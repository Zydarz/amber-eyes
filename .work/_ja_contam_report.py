#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phân rã nhiễm ngôn ngữ theo loại + danh sách mục cần dịch lại (theo cache).

    py -3 .work/_ja_contam_report.py
"""
import collections
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from _ja_cn_map import CN2JP  # noqa: E402

SKIP = {k for k, v in CN2JP.items() if k == v}
CN = {k for k, v in CN2JP.items() if k != v and k not in SKIP}
RXH = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
RXJ = re.compile(r"(?<!<)_(?=[A-Za-z])")
VND = set("àáảãạăâđêôơưÀÁẢÃẠĂÂĐÊÔƠƯ")

cn_c = collections.Counter()
ko_c = collections.Counter()
jk_c = collections.Counter()
vn_c = collections.Counter()
per_ep = collections.defaultdict(list)

for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    d = json.loads(cp.read_text(encoding="utf-8"))
    for k, v in d.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        ja = v.get("ja", "") or ""
        if not ja:
            continue
        why = []
        cn = sorted({x for x in ja if x in CN})
        if cn:
            why.append("CN")
            cn_c["".join(cn)] += 1
        ko = sorted(set(RXH.findall(ja)))
        if ko:
            why.append("KO")
            ko_c["".join(ko)] += 1
        if RXJ.search(ja):
            why.append("JUNK")
            jk_c[ep] += 1
        vn = sorted({x for x in ja if x in VND})
        if vn:
            why.append("VN")
            vn_c["".join(vn)] += 1
        if why:
            per_ep[ep].append((k, why, ja))

print("=== CN-only ===")
for k, n in cn_c.most_common(50):
    print(f"  {k:<14} x{n}")
print("\n=== HANGUL ===")
for k, n in ko_c.most_common(30):
    print(f"  {k:<24} x{n}")
print("\n=== JUNK (gach duong) ===", dict(jk_c))
print("\n=== VN diacritics ===")
for k, n in vn_c.most_common(30):
    print(f"  {k:<16} x{n}")

print("\n=== SO MUC THEO TAP ===")
tot = 0
for ep in sorted(per_ep):
    lst = per_ep[ep]
    tot += len(lst)
    ids = ",".join(k for k, _w, _j in lst)
    print(f"Tap{ep}: {len(lst)}  [{ids}]")
print(f"TONG {tot} muc")
