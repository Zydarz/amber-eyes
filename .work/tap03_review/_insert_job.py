#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chèn job sinh ảnh còn thiếu của Tập 03 vào .work/bg_jobs_tap03.json (giữ thứ tự cảnh).
Không ghi đè job đã có. In ra phần đã thay đổi để kiểm chứng."""
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
MAIN = ROOT / ".work" / "bg_jobs_tap03.json"
EXTRA = ROOT / ".work" / "bg_jobs_tap03_extra.json"

main = json.loads(MAIN.read_text(encoding="utf-8"))
extra = json.loads(EXTRA.read_text(encoding="utf-8"))
names = {j["name"] for j in main}

# vị trí chèn: ngay sau job đứng trước trong truyện (dùng bảng ánh xạ B2)
AFTER = {
    "t3_backyard_garden": "t3_ravine",   # 2.06#2 — khu vườn sau nhà
    "t3_trapdoor":        "t3_small_bed", # 3.05#7 — cửa bẩy dưới bàn ăn
}

added = []
for job in extra:
    n = job["name"]
    if n in names:
        # job đã có: so prompt, nếu khác thì giữ bản đã có nhưng báo lại
        cur = next(j for j in main if j["name"] == n)
        same = cur["prompt"].strip() == job["prompt"].strip()
        print(f"  {n}: da co trong jobs — prompt {'GIONG' if same else 'KHAC'} voi ban extra")
        if not same:
            print(f"    jobs : {cur['prompt'][:150]}")
            print(f"    extra: {job['prompt'][:150]}")
        continue
    anchor = AFTER.get(n)
    if anchor and anchor in names:
        idx = [j["name"] for j in main].index(anchor) + 1
        main.insert(idx, job)
        added.append((n, idx, anchor))
    else:
        main.append(job)
        added.append((n, len(main), "cuoi file"))
    names.add(n)

MAIN.write_text(json.dumps(main, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\nTong so muc trong bg_jobs_tap03.json: {len(main)}")
for n, idx, a in added:
    print(f"  + {n} (vi tri {idx}, ngay sau {a})")
print(f"Da ghi: {MAIN}")
