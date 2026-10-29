#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""t3_gavel — bien the lan 3: bo hanh tu phap ly ("judge", "gavel", "courtroom"),
chi giu hinh dang bang go: cay roi go nho + doi thu cham doi."""
import json
from pathlib import Path

p = Path(r"D:\TEST\Gax\Audi\.work\bg_jobs_tap03.json")
jobs = json.loads(p.read_text(encoding="utf-8"))

NEW = ("A small smooth wooden mallet with a round handle lying on a dark polished wooden surface "
       "beside a heavy round wooden disk, cold directional light raking from one side, deep "
       "shadow, shallow depth of field, still life, nobody present, no text, no writing.")

for j in jobs:
    if j["name"] == "t3_gavel":
        print("CU :", j["prompt"][:110])
        j["prompt"] = NEW
        print("MOI:", NEW[:110])
        break
else:
    raise SystemExit("khong tim thay t3_gavel")

p.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
print("da cap nhat")
