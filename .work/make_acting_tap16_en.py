#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap16_EN.json — Acting and pauses for Episode 16 English Edition."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap16_EN.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
VN_ACTING = json.loads((WORK / "acting_tap16.json").read_text(encoding="utf-8"))

output_data = {
    "_meta": {
        "episode": "16_EN",
        "description": "Acting & Pause parameters for Tap 16 EN (257 sentences)",
        "total_sentences": 257,
        "pause_count": len(VN_ACTING.get("_pause_after", {})),
    },
    "_pause_after": VN_ACTING.get("_pause_after", {}),
}

# Map English text into acting entries
vn_map = {k: v for k, v in VN_ACTING.items() if not k.startswith("_")}

for el in SCRIPT:
    if el["kind"] != "LOI":
        continue
    for s in el["sentences"]:
        sid = s["id"]
        text = s["text"]
        entry = dict(vn_map.get(sid, {"emotion": "neutral", "speed": -0.02, "pitch": 0}))
        entry["text"] = text
        output_data[sid] = entry

out_file = WORK / "acting_tap16_EN.json"
out_file.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {out_file.name}: {len(output_data) - 2} sentences")
