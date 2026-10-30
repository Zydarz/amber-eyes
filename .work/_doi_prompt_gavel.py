#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Viet lai prompt t3_gavel lan 2 (tranh khung 'sounding block on a polished bench')."""
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / ".work" / "bg_jobs_tap03.json"
jobs = json.loads(p.read_text(encoding="utf-8"))

NEW = ("A wooden judge's gavel lying on a dark wooden desk beside a closed leather law book, "
       "cold directional light raking across the desk surface, deep shadow, shallow depth of field, "
       "still life, nobody present, no text, no emblem, no writing, no page visible.")

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
