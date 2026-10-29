#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xoá cache của các unit loại ACT (tiêu đề hồi) — để dịch lại sau khi đổi cách
tách ngoặc cuối (mốc thời gian vs thuật ngữ).

    py -3 .work/_ja_purge_act.py          # xem trước
    py -3 .work\_ja_purge_act.py --do
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

CACHE = HERE / "ja_cache"
do = "--do" in sys.argv
n_files = n_keys = 0
for i in range(1, 30):
    ep = f"{i:02d}"
    cp = CACHE / f"tap{ep}.json"
    if not cp.exists():
        continue
    units = M.assign_turn_counts(M.parse_units(M.canonical_vn(ep)))
    acts = [u["id"] for u in units if u["kind"] == "ACT"]
    if not acts:
        continue
    d = json.loads(cp.read_text(encoding="utf-8"))
    hit = [a for a in acts if a in d]
    if not hit:
        continue
    n_files += 1
    n_keys += len(hit)
    print(f"  tap{ep}.json: {len(hit)} mục ACT -> {hit}")
    if do:
        for a in hit:
            d.pop(a, None)
        cp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\n{n_files} file, {n_keys} mục ACT" + (" -- ĐÃ XOÁ" if do else " (thêm --do để xoá)"))
