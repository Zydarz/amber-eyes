#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xoá các mục cache '#L' (dòng nhiều câu) — dùng khi đổi cách kiểm tra.

    py -3 .work/_ja_purge_line.py          # xem trước
    py -3 .work/_ja_purge_line.py --do     # thực sự xoá
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CACHE = Path(__file__).parent / "ja_cache"
do = "--do" in sys.argv

n_files = n_keys = 0
for p in sorted(CACHE.glob("tap*.json")):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        continue
    bad = [k for k in d if isinstance(k, str) and k.endswith("#L")]
    if not bad:
        continue
    n_files += 1
    n_keys += len(bad)
    print(f"  {p.name}: {len(bad)} mục #L -> {bad[:6]}")
    if do:
        for k in bad:
            d.pop(k, None)
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"\n{n_files} file, {n_keys} mục #L" + (" -- ĐÃ XOÁ" if do else " (thêm --do để xoá)"))
