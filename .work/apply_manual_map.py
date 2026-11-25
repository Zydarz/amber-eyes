#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Áp bảng xếp tay {hồi: {số thứ tự job trong hồi: [câu đầu, câu cuối]}} (số thứ tự câu 1-based
trong hồi) vào bg_jobs_tapXX.json. Kiểm: mỗi câu của hồi đã xếp phải có ≥1 job.
Dùng: py -3 .work/apply_manual_map.py XX [--write]"""
import sys, json, shutil
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
import importlib.util
W = Path(__file__).parent
spec = importlib.util.spec_from_file_location("q", W / "qc_bg_mapping.py"); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
n = int(sys.argv[1]); m = json.load(open(W / f"manual_map_tap{n:02d}.json", encoding="utf-8"))
acts = {}
for e in q.pk.parse_file(q.script_file(n)):
    for s in e.get("sentences") or []: acts.setdefault(e["act"], []).append(s["id"])
p = W / f"bg_jobs_tap{n:02d}.json"; jobs = json.load(open(p, encoding="utf-8"))
byact = {}
for j in jobs: byact.setdefault(j["act"], []).append(j)
for a, mp in m.items():
    a = int(a); ss = acts[a]; js = byact[a]; cov = set()
    assert len(mp) == len(js), f"hồi {a}: {len(mp)} khoá ≠ {len(js)} job"
    for k, (x, y) in mp.items():
        js[int(k) - 1]["sentences"] = ",".join(ss[x - 1:y]); cov |= set(range(x, y + 1))
    miss = sorted(set(range(1, len(ss) + 1)) - cov)
    print(f"Tập {n} hồi {a}: {len(js)} job · {len(ss)} câu · câu chưa phủ: {miss or 'không'}")
if "--write" in sys.argv:
    with open(p, "w", encoding="utf-8", newline="") as f: json.dump(jobs, f, ensure_ascii=False, indent=2); f.write("\n")
    print("đã ghi")
