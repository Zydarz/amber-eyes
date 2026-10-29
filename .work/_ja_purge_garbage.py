#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BƯỚC A: tìm & xoá các mục cache bị model HỎNG (rác) để dịch lại.

Dấu hiệu hỏng:
  - gạch dưới đứng trước chữ cái (VD "_statistics", "_bounds", "_yaml")
  - từ tiếng Anh lạc vào giữa tiếng Nhật (VD "attentively", "resulte")
  - tên riêng sai chính tả (VD "Colomy" -> "Colony")

    py -3 .work/_ja_purge_garbage.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# rác: _ + chữ cái (loại trừ <br>)
RX_UNDERSCORE = re.compile(r"(?<!<)_(?=[A-Za-z])")
# các từ tiếng Anh bị lẫn vào giữa tiếng Nhật
RX_ENGLISH = re.compile(
    r"(?<![A-Za-z])(attentively|gradually|resulte|resulting|result|bounds|repository|"
    r"psychiatry|forensic|statistics|yaml|exist|HANDLE|rage)(?![A-Za-z])")
# tên riêng viết sai (không dùng \b vì CJK cũng là word-char trong Python)
# LƯU Ý: "Colomy" là tên đúng lấy từ bản VN (Bruce Colomy) => KHÔNG phải rác.
RX_TYPO = re.compile(r"(?<![A-Za-z])Columy(?![A-Za-z])")

purged = {}
for i in range(1, 30):
    ep = "%02d" % i
    cp = HERE / "ja_cache" / f"tap{ep}.json"
    if not cp.exists():
        continue
    cache = json.loads(cp.read_text(encoding="utf-8"))
    hit = []
    for k, v in cache.items():
        if not isinstance(k, str) or k.startswith("_") or not isinstance(v, dict):
            continue
        ja = v.get("ja", "") or ""
        if not ja:
            continue
        reasons = []
        if RX_UNDERSCORE.search(ja):
            reasons.append("gach-duong")
        m = RX_ENGLISH.search(ja)
        if m:
            reasons.append("tieng-anh:" + m.group(0))
        if RX_TYPO.search(ja):
            reasons.append("sai-chinh-ta:Colomy")
        if reasons:
            hit.append((k, reasons, ja))
    if hit:
        purged[ep] = hit
        for k, reasons, ja in hit:
            print(f"Tap{ep} {k}: {','.join(reasons)}")
            print(f"     {ja[:170]}")

if not purged:
    print("KHONG co muc rac nao")
else:
    print(f"\n=> {sum(len(v) for v in purged.values())} muc can xoa va dich lai")
    print("Tap bi anh huong:", " ".join(sorted(purged)))

if "--do" in sys.argv:
    for ep, hit in purged.items():
        cp = HERE / "ja_cache" / f"tap{ep}.json"
        cache = json.loads(cp.read_text(encoding="utf-8"))
        for k, _r, _ja in hit:
            cache.pop(k, None)
        cp.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  -> da xoa {len(hit)} muc trong tap{ep}.json")
    print("XOA XONG. Chay lai pipeline cho cac tap tren de dich lai.")
