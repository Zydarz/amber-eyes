#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đồng bộ prompt trong .work/bg_jobs_tap03_extra.json với bản đã sinh thật trong bg_jobs_tap03.json."""
import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
EXTRA = ROOT / ".work" / "bg_jobs_tap03_extra.json"
MAIN = ROOT / ".work" / "bg_jobs_tap03.json"

extra = json.loads(EXTRA.read_text(encoding="utf-8"))
main = {j["name"]: j for j in json.loads(MAIN.read_text(encoding="utf-8"))}

for job in extra:
    n = job["name"]
    if n in main and main[n]["prompt"].strip() != job["prompt"].strip():
        print(f"{n}: doi prompt sang ban da sinh that trong bg_jobs_tap03.json")
        job["prompt"] = main[n]["prompt"]
EXTRA.write_text(json.dumps(extra, ensure_ascii=False, indent=1), encoding="utf-8")
print("Da ghi", EXTRA)
