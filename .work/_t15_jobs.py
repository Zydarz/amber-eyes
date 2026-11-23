# -*- coding: utf-8 -*-
import json
import pathlib

p = pathlib.Path(r"D:/TEST/Gax/amber-eyes/.work/bg_jobs_tap15.json")
if not p.exists():
    print("khong co bg_jobs_tap15.json")
else:
    jobs = json.loads(p.read_text(encoding="utf-8"))
    print("so job tap15:", len(jobs))
    print("ten:", [j["name"] for j in jobs][:6], "...")
