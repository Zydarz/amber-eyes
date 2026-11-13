#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap10_JA.json — Acting and pauses for Episode 10 Japanese Edition."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap10_JA.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.05": "N2"}

# Load base pauses and emotions from VN edition
VN_ACTING = json.loads((WORK / "acting_tap10.json").read_text(encoding="utf-8"))

output_data = {
    "_meta": {
        "episode": "10_JA",
        "description": "Acting & Pause parameters for Tap 10 JA (240 sentences)",
        "total_sentences": 240,
        "pause_count": len(VN_ACTING.get("_pause_after", {})),
    },
    "_pause_after": VN_ACTING.get("_pause_after", {}),
}

for k, v in VN_ACTING.items():
    if k.startswith("_"):
        continue
    output_data[k] = v

out_file = WORK / "acting_tap10_JA.json"
out_file.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Đã xuất file diễn xuất JA: {out_file}")
