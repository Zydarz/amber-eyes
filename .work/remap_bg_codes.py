#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gán lại `sentences` của bg_jobs theo kịch bản hiện tại (giữ nguyên prompt/desc/name).
Mỗi hồi: job giữ thứ tự, chia các câu của hồi thành k cụm liền mạch theo TRỌNG SỐ SỐ TỪ
(mỗi shot ~ thời lượng đều nhau). Sao lưu bản gốc vào .work/_cu/bg_jobs_remap_20261124/.
Dùng: py -3 .work/remap_bg_codes.py XX [XX ...]   (--dry để chỉ in)"""
import sys, json, shutil, importlib.util, glob, re
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).parent; R = W.parent
spec = importlib.util.spec_from_file_location("q", W / "qc_bg_mapping.py"); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
dry = "--dry" in sys.argv
for n in [int(a) for a in sys.argv[1:] if a.isdigit()]:
    sf = q.script_file(n); els = q.pk.parse_file(sf)
    acts = {}
    for e in els:
        for s in e.get("sentences") or []:
            acts.setdefault(e["act"], []).append((s["id"], max(len(s["text"].split()), 1)))
    p = W / f"bg_jobs_tap{n:02d}.json"; jobs = json.load(open(p, encoding="utf-8"))
    byact = {}
    for x in jobs: byact.setdefault(x["act"], []).append(x)
    for a, js in byact.items():
        ss = acts.get(a, [])
        if not ss: print(f"Tập {n} hồi {a}: kịch bản không có câu!"); continue
        tot = sum(w for _, w in ss); k = len(js); cum = 0; bucket = [[] for _ in range(k)]
        for sid, w in ss:
            mid = (cum + w / 2) / tot; cum += w
            bucket[min(int(mid * k), k - 1)].append(sid)
        last = ss[0][0]
        for x, b in zip(js, bucket):
            if not b: b = [last]          # job nhiều hơn câu: dùng lại câu liền trước
            last = b[-1]; x["sentences"] = ",".join(b)
    if not dry:
        bk = W / "_cu" / "bg_jobs_remap_20261124"; bk.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, bk / p.name)
        with open(p, "w", encoding="utf-8", newline="") as f:
            json.dump(jobs, f, ensure_ascii=False, indent=2); f.write("\n")
    print(f"Tập {n}: {len(jobs)} job, {sum(len(v) for v in acts.values())} câu → {'(dry) ' if dry else ''}đã gán lại")
