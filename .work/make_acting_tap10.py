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

# Build acting structure
acting = {}
pause_after = {}

# All sentence ids in order
all_sents = []
for el in SCRIPT:
    if el["kind"] == "LOI":
        for s in el["sentences"]:
            all_sents.append((el, s))

total_sents = len(all_sents)
print(f"Tổng số câu thoại: {total_sents}")

for idx, (el, s) in enumerate(all_sents):
    sid = s["id"]
    act_str = str(el["act"])
    raw_role = el["role"]
    role = N_ELEMENT.get(el["id"], raw_role)
    
    # Determine emotion & speed
    default_emo, default_spd = ACT_MOOD.get((act_str, role), ("neutral", 0.0))
    base_delta = BASE_DELTA.get(role, -0.02)
    
    if sid in SPECIAL_EMOTIONS:
        emo, spd_tweak = SPECIAL_EMOTIONS[sid]
        final_speed = round(base_delta + spd_tweak, 3)
    else:
        emo = default_emo
        final_speed = round(base_delta + default_spd, 3)
        
    # Clamp speed in [-0.06, +0.02] per rule G4
    final_speed = max(-0.06, min(0.02, final_speed))
    
    acting[sid] = {
        "emotion": emo,
        "speed": final_speed,
        "pitch": 0, # Rule G5: ALWAYS 0
    }
    
    # Determine pause_after (Rule A13: ~50-65% of sentences, median >= 0.6s)
    # Check if this sentence is the last in the turn
    is_last_in_turn = (s == el["sentences"][-1])
    is_last_in_script = (idx == total_sents - 1)
    
    # Default pause logic:
    # 1. Last in turn -> 0.7 - 0.9s (role transition pause)
    # 2. Key dramatic sentence -> 0.6 - 0.9s
    # 3. Intermediate transition -> 0.4 - 0.5s
    # 4. Connected clause -> 0.3s
    if is_last_in_script:
        pause_after[sid] = 1.0
    elif is_last_in_turn:
        pause_after[sid] = 0.8
    else:
        # Inside turn: select ~50% of sentences to pause
        sent_num = int(sid.split("#")[1])
        total_in_el = len(el["sentences"])
        
        # Sentences at halfway marks or dramatic points
        if sent_num % 2 == 0:
            pause_after[sid] = 0.5
        elif sid in SPECIAL_EMOTIONS:
            pause_after[sid] = 0.6

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
