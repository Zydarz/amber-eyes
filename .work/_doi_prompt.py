#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Doi cau prompt cua 3 anh bi connector 500 lien tuc (gavel / trophy_box / red_flags).
Y nghia hinh anh giu nguyen, chi viet lai cach dien de tranh duong loi noi bo cua dich vu."""
import json
from pathlib import Path

sys_path = Path(r"D:\TEST\Gax\Audi\.work\bg_jobs_tap03.json")
jobs = json.loads(sys_path.read_text(encoding="utf-8"))

NEW = {
    "t3_gavel":
        "A dark polished wooden judge's bench in an empty courtroom, a wooden gavel resting on a "
        "round sounding block on the bench surface, cold directional light raking from one side, "
        "deep shadow, shallow depth of field, nobody present, no text, no emblem, no insignia.",
    "t3_trophy_box":
        "A plain closed wooden crate with a hinged lid sitting on a bare metal shelf in a dim "
        "storeroom, one cold shaft of light falling across the lid, deep shadow, still life, "
        "nobody present, no text, no markings, no labels.",
    "t3_red_flags":
        "Four plain objects spaced evenly in a row on a dark table under a single spotlight: a small "
        "empty wire cage, a burnt wooden matchstick, a folded grey wool blanket, and a stopped "
        "wristwatch with a blank face, deep shadow all around, nobody present, no text, no numbers.",
}

changed = []
for j in jobs:
    if j["name"] in NEW:
        old = j["prompt"]
        j["prompt"] = NEW[j["name"]]
        changed.append(j["name"])
        print(f"--- {j['name']} ---")
        print(f"  CU : {old[:100]}...")
        print(f"  MOI: {NEW[j['name']][:100]}...")

assert len(changed) == 3, changed
sys_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\nda cap nhat {len(changed)} prompt trong {sys_path.name}")
