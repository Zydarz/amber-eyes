#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap10.json — Acting and pauses for Episode 10 (Colleen Stan).
Follows rules G1-G8, G10, A13, and qc_pause_gate standards.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap10.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.05": "N2"}

# Base speed deltas per character
BASE_DELTA = {"H": -0.02, "D": -0.02, "C": -0.02, "N1": -0.02, "N2": -0.02}

# Default emotion per act and role
ACT_MOOD = {
    ("1", "H"): ("neutral", 0.0),
    ("1", "N1"): ("sad", -0.02),
    ("1", "D"): ("neutral", 0.0),
    ("2", "H"): ("neutral", 0.0),
    ("2", "D"): ("neutral", 0.0),
    ("2", "C"): ("neutral", 0.0),
    ("3", "H"): ("neutral", 0.0),
    ("3", "D"): ("neutral", 0.0),
    ("3", "C"): ("neutral", 0.0),
    ("4", "H"): ("neutral", 0.0),
    ("4", "D"): ("neutral", 0.0),
    ("4", "N2"): ("sad", -0.03),
    ("4", "C"): ("neutral", 0.0),
    ("5", "H"): ("neutral", 0.0),
    ("5", "C"): ("neutral", 0.0),
    ("5", "D"): ("neutral", 0.0),
}

# Special sentence emotions and speed tweaks
SPECIAL_EMOTIONS = {
    # Act 1
    "1.02#6": ("sad", -0.02),
    "1.02#12": ("fearful", -0.02),
    "1.04#6": ("neutral", 0.0),
    "1.06#5": ("fearful", -0.02),
    "1.06#6": ("fearful", -0.03),
    "1.07#1": ("sad", -0.02),
    "1.07#4": ("sad", -0.03),
    "1.07#5": ("sad", -0.03),
    "1.09#2": ("fearful", -0.02),
    "1.09#3": ("fearful", -0.03),
    "1.10#3": ("neutral", 0.0),
    "1.11#3": ("sad", -0.03),
    # Act 2
    "2.02#1": ("fearful", -0.02),
    "2.02#5": ("fearful", -0.03),
    "2.02#6": ("sad", -0.03),
    "2.04#7": ("sad", -0.02),
    "2.04#8": ("sad", -0.03),
    "2.06#6": ("sad", -0.02),
    "2.06#8": ("neutral", 0.0),
    "2.08#4": ("fearful", -0.02),
    "2.09#2": ("fearful", -0.02),
    "2.09#4": ("fearful", -0.03),
    "2.10#5": ("sad", -0.02),
    # Act 3
    "3.02#4": ("neutral", 0.0),
    "3.04#3": ("sad", -0.02),
    "3.05#4": ("fearful", -0.02),
    "3.06#1": ("neutral", -0.02),
    "3.06#3": ("fearful", -0.02),
    "3.07#8": ("sad", -0.02),
    "3.07#11": ("sad", -0.03),
    "3.08#5": ("sad", -0.02),
    "3.08#7": ("sad", -0.03),
    # Act 4
    "4.02#5": ("fearful", -0.02),
    "4.03#6": ("fearful", -0.02),
    "4.05#1": ("sad", -0.03),
    "4.05#4": ("fearful", -0.03),
    "4.05#5": ("sad", -0.03),
    "4.05#6": ("fearful", -0.03),
    "4.05#8": ("neutral", -0.02),
    "4.07#1": ("surprised", 0.0),
    "4.07#4": ("surprised", 0.0),
    "4.07#6": ("neutral", 0.0),
    "4.10#3": ("sad", -0.02),
    "4.10#5": ("neutral", -0.02),
    # Act 5
    "5.02#4": ("sad", -0.02),
    "5.02#6": ("neutral", 0.0),
    "5.03#4": ("neutral", 0.0),
    "5.03#7": ("neutral", 0.0),
    "5.05#12": ("neutral", 0.0),
}

def pause_for(elems, el_idx, s_idx, n_sent, role, text):
    is_last = (s_idx == n_sent - 1)
    if is_last:
        nxt = elems[el_idx + 1]["kind"] if el_idx + 1 < len(elems) else "END"
        if nxt in ("NGHI", "SFX", "END"):
            return 1.0
        if role in ("N1", "N2"):
            return 0.8
        return 0.6
    t_clean = text.rstrip("”\" ").strip()
    if t_clean.endswith("?"):
        return 0.5
    if len(text.split()) >= 25:
        return 0.4
    return 0.3

# Build acting structure
acting = {}
pause_after = {}

# All sentence ids in order
for el_idx, el in enumerate(SCRIPT):
    if el.get("kind") != "LOI":
        continue
    act_str = str(el["act"])
    raw_role = el["role"]
    role = N_ELEMENT.get(el["id"], raw_role)
    sents = el.get("sentences", [])
    n_sent = len(sents)

    default_emo, default_spd = ACT_MOOD.get((act_str, role), ("neutral", 0.0))
    base_delta = BASE_DELTA.get(role, -0.02)

    for s_idx, s in enumerate(sents):
        sid = s["id"]
        if sid in SPECIAL_EMOTIONS:
            emo, spd_tweak = SPECIAL_EMOTIONS[sid]
            final_speed = round(base_delta + spd_tweak, 3)
        else:
            emo = default_emo
            final_speed = round(base_delta + default_spd, 3)

        # Clamp speed in [-0.06, +0.02] per rule G4
        final_speed = max(-0.06, min(0.02, final_speed))

        acting[sid] = [emo, final_speed, 0, None]
        pause_after[sid] = pause_for(SCRIPT, el_idx, s_idx, n_sent, role, s["text"])

total_sents = len(acting)
print(f"Tổng số câu thoại: {total_sents}")

print(f"Số câu có nhịp nghỉ pause_after: {len(pause_after)} / {total_sents} ({len(pause_after)/total_sents:.1%})")

# Combine into output format
output_data = {
    "_meta": {
        "episode": "10",
        "description": "Acting & Pause parameters for Tap 10 (240 sentences)",
        "total_sentences": total_sents,
        "pause_count": len(pause_after),
    },
    "_pause_after": pause_after,
}
output_data.update(acting)

out_file = WORK / "acting_tap10.json"
out_file.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Đã xuất file diễn xuất: {out_file}")
