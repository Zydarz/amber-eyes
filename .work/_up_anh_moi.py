#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat bg_jobs_tap03.json sau khi review anh voi kich ban da sua:
  - t3_small_bed: bo song chắn (doc nhu phong giam, khong phai tang ham Montana 1950)
  - t3_trunk     : MOI - "coc xe" (2.07#6, #8) - anh cu khong phai coc
  - t3_trapdoor  : MOI - "cua bay duoi ban an" (3.05#7) - chua co anh
"""
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / ".work" / "bg_jobs_tap03.json"
jobs = json.loads(p.read_text(encoding="utf-8"))
names = {j["name"] for j in jobs}

NEW_SMALL_BED = (
    "A narrow child's bed with a thin blanket in a damp bare 1950s American cellar, bare "
    "concrete block and earthen walls, a small plain basement window with a single sheet of "
    "glass and no bars, a cold shaft of grey daylight from a stairwell above, dust and damp "
    "patches, nobody present, no text."
)

NEW = [
    {
        "name": "t3_trunk",
        "prompt": (
            "The open trunk of a 1969 pale yellow American full-size sedan parked on a wet road "
            "at night, the trunk lid raised, the empty dark trunk lining visible inside, a cold "
            "streetlight above, damp asphalt, deep shadow, nobody present, no text, no logos, "
            "no lettering, no license plate characters."
        ),
    },
    {
        "name": "t3_trapdoor",
        "prompt": (
            "The dining area of a 1950s American house at night, a plain wooden table on a worn "
            "linoleum floor, a square wooden trapdoor set into the floorboards beside the table "
            "standing slightly ajar with a dark opening below, a single bare bulb overhead, worn "
            "wallpaper, deep shadow, nobody present, no text, no lettering."
        ),
    },
]

for j in jobs:
    if j["name"] == "t3_small_bed":
        print("t3_small_bed: doi prompt (bo song chắn)")
        j["prompt"] = NEW_SMALL_BED

for n in NEW:
    if n["name"] in names:
        print(f"{n['name']}: da co, bo qua")
        continue
    jobs.append(n)
    print(f"{n['name']}: them vao")

p.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\ntong {len(jobs)} muc trong {p.name}")
