#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump toàn bộ prompt t31/t32 ra file để soi tay."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
out = []
for ep in (31, 32):
    jobs = json.loads((ROOT / ".work" / f"bg_jobs_tap{ep}.json").read_text(encoding="utf-8"))
    out.append(f"##### TAP {ep} ({len(jobs)} job) #####")
    for j in jobs:
        out.append(f"{j['name']} :: {j['prompt']}")
(ROOT / ".work" / "_dump_prompts_t31_32.txt").write_text("\n".join(out), encoding="utf-8")
print("ok")
