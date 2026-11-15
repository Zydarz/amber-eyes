#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap20_JA.json — Acting and pauses for Episode 20 Japanese Edition."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap20_JA.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
VN_ACTING = json.loads((WORK / "acting_tap20.json").read_text(encoding="utf-8"))

output_data = {
    "_meta": {
        "episode": "20_JA",
        "description": "Acting & Pause parameters for Tap 20 JA (241 sentences)",
        "total_sentences": 241,
        "pause_count": len(VN_ACTING.get("_pause_after", {})),
    },
    "_pause_after": VN_ACTING.get("_pause_after", {}),
}

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

out_file = WORK / "acting_tap20_JA.json"
out_file.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {out_file.name}: {len(output_data) - 2} sentences")
