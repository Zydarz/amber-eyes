#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phủ các câu chưa có job: câu thiếu nhập vào job của câu LIỀN TRƯỚC cùng hồi (ảnh giữ thêm một nhịp);
nếu là câu đầu hồi thì nhập vào job của câu liền sau. Chỉ thêm mã vào `sentences`, không đổi prompt/name.
Dùng: py -3 .work/fill_bg_gaps.py XX [--write]"""
import sys, json, shutil, importlib.util
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).parent
spec = importlib.util.spec_from_file_location("q", W / "qc_bg_mapping.py"); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
n = int(sys.argv[1]); p = W / f"bg_jobs_tap{n:02d}.json"; jobs = json.load(open(p, encoding="utf-8"))
seq = [(e["act"], s["id"]) for e in q.pk.parse_file(q.script_file(n)) for s in (e.get("sentences") or [])]
owner = {}
for i, x in enumerate(jobs):
    for c in x["sentences"].split(","):
        if c: owner.setdefault(c, i)
add = {}
for k, (a, c) in enumerate(seq):
    if c in owner: continue
    j = None
    for b in range(k - 1, -1, -1):
        if seq[b][0] != a: break
        if seq[b][1] in owner: j = owner[seq[b][1]]; break
    if j is None:
        for b in range(k + 1, len(seq)):
            if seq[b][0] != a: break
            if seq[b][1] in owner: j = owner[seq[b][1]]; break
    if j is None: print("không tìm được job cho", c); continue
    owner[c] = j; add.setdefault(j, []).append(c)
order = {c: i for i, (a, c) in enumerate(seq)}
for j, cs in add.items():
    allc = [c for c in jobs[j]["sentences"].split(",") if c] + cs
    jobs[j]["sentences"] = ",".join(sorted(allc, key=lambda c: order[c]))
print(f"Tập {n}: nhập {sum(len(v) for v in add.values())} câu vào {len(add)} job")
if "--write" in sys.argv:
    bk = W / "_cu" / "bg_jobs_remap_20261124"; bk.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, bk / f"bg_jobs_tap{n:02d}_before_fill.json")
    with open(p, "w", encoding="utf-8", newline="") as f: json.dump(jobs, f, ensure_ascii=False, indent=2); f.write("\n")
    print("đã ghi")
