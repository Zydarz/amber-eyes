# -*- coding: utf-8 -*-
"""Đối chiếu 136 mã nền của Tập 11 với nội dung câu + mô tả/prompt để soi khớp H3."""
import json
import sys
from pathlib import Path

sys.path.insert(0, r"D:/TEST/Gax/amber-eyes/.work")
from _t11_chunk_plan import parse, MD  # noqa: E402

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
rows = parse(str(MD))
jobs = {j["name"]: j for j in json.loads((ROOT / ".work/bg_jobs_tap11_v3.json").read_text(encoding="utf-8"))}

# gom shot theo mã nền (kế hoạch đã ghi trong bảng)
from collections import OrderedDict
groups = OrderedDict()
cur = None
for r in rows:
    if r["bg"]:
        cur = r["bg"]
    if not cur:
        continue
    groups.setdefault(cur, []).append(r)

print(f"{len(groups)} mã nền · {len(jobs)} job\n")
for code, rs in groups.items():
    j = jobs.get(code)
    if not j:
        print(f"!!! THIẾU JOB: {code}")
        continue
    txt = " || ".join(x["chu"].replace("*", "") for x in rs)
    print(f"{code}")
    print(f"   desc : {j['desc'][:120]}")
    print(f"   noi dung: {txt[:150]}")
    print(f"   prompt: {j['prompt'][:110]}...")
