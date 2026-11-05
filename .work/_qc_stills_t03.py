#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra bộ ảnh tĩnh Tập 03 sau khi render: đủ chưa, còn ảnh thừa không."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")
SHOTS = json.loads((ROOT / ".work" / "shots_t03.json").read_text(encoding="utf-8"))
SD = ROOT / ".work" / "video3_t03" / "stills"
CUT = datetime.datetime(2026, 11, 5, 14, 40)

ids = {f"shot_{s['id']}.png" for s in SHOTS["shots"]}
files = {p.name for p in SD.glob("*.png")}
new = [p for p in SD.glob("*.png")
       if datetime.datetime.fromtimestamp(p.stat().st_mtime) > CUT]
print(f"shot trong bang      : {len(ids)}")
print(f"file trong thu muc   : {len(files)}")
print(f"render moi (14:40+)  : {len(new)}")
print(f"THUA (file cu thua)  : {sorted(files - ids)}")
print(f"THIEU                : {sorted(ids - files)}")

bad = [p.name for p in SD.glob("*.png") if p.stat().st_size < 20000]
print(f"anh < 20KB (hong)    : {len(bad)} {bad[:8]}")

# so voi manifest cu
mans = sorted((ROOT / ".work" / "_cu").glob("stills_t03_manifest_*.json"))
if mans:
    man = json.loads(mans[-1].read_text(encoding="utf-8"))
    changed = [n for n, v in man.items()
               if (SD / n).exists()
               and hashlib.sha256((SD / n).read_bytes()).hexdigest()[:16] != v["sha256"]]
    print(f"da doi so voi ban 11/02: {len(changed)} / {len(man)}")
    print(f"   -> {sorted(changed)}")
