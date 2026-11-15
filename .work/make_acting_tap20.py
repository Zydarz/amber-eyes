#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap20.json — Acting and pauses for Episode 20 (Stephen McDaniel).
Follows rules G1-G8, G10, A13, and qc_pause_gate standards.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap20.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.09": "N2"}

# Base speed deltas per character
BASE_DELTA = {"H": -0.02, "D": -0.02, "C": -0.02, "N1": -0.02, "N2": -0.02}

# Default emotion per act and role
ACT_MOOD = {
    ("1", "H"): ("neutral", 0.0),
    ("1", "N1"): ("sad", -0.02),
    ("1", "D"): ("neutral", 0.0),
    ("2", "H"): ("neutral", 0.0),
    ("2", "D"): ("neutral", 0.0),
    ("3", "H"): ("neutral", 0.0),
    ("3", "C"): ("neutral", 0.0),
    ("4", "H"): ("neutral", 0.0),
    ("4", "D"): ("neutral", 0.0),
    ("4", "N2"): ("sad", -0.03),
    ("4", "C"): ("neutral", 0.0),
    ("5", "H"): ("neutral", 0.0),
    ("5", "D"): ("neutral", 0.0),
    ("5", "C"): ("neutral", 0.0),
}

# Special sentence emotions and speed tweaks
SPECIAL_EMOTIONS = {
    # Act 1
    "1.02#5": ("sad", -0.02),
    "1.02#8": ("fearful", -0.02),
    "1.06#4": ("fearful", -0.02),
    "1.06#5": ("fearful", -0.03),
    "1.07#1": ("sad", -0.02),
    "1.07#6": ("fearful", -0.03),
    "1.07#7": ("fearful", -0.03),
    "1.07#8": ("sad", -0.03),
    "1.09#2": ("fearful", -0.02),
    "1.09#3": ("fearful", -0.03),
    # Act 2
    "2.02#1": ("neutral", 0.0),
    "2.02#4": ("fearful", -0.02),
    "2.04#6": ("fearful", -0.02),
    "2.04#7": ("neutral", 0.0),
    "2.08#6": ("fearful", -0.02),
    # Act 3
    "3.02#1": ("neutral", 0.0),
    "3.03#3": ("fearful", -0.02),
    "3.05#4": ("fearful", -0.02),
    "3.07#4": ("fearful", -0.02),
    # Act 4
    "4.02#7": ("fearful", -0.02),
    "4.04#4": ("fearful", -0.02),
    "4.08#3": ("sad", -0.02),
    "4.09#1": ("sad", -0.02),
    "4.09#4": ("sad", -0.03),
    "4.09#5": ("sad", -0.03),
    "4.09#8": ("sad", -0.02),
    "4.11#3": ("sad", -0.02),
    # Act 5
    "5.02#1": ("neutral", 0.0),
    "5.04#2": ("neutral", 0.0),
}

PAUSES = {}

def build_pauses():
    all_sents = []
    for el in SCRIPT:
        if el["kind"] == "LOI":
            for s in el["sentences"]:
                all_sents.append(s["id"])
    
    # Target 55-65% sentences with pause
    # Values 0.4s to 0.9s (median >= 0.6s, <0.4s <= 25%)
    for i, sid in enumerate(all_sents):
        curr_el = sid.split("#")[0]
        next_sid = all_sents[i + 1] if i + 1 < len(all_sents) else None
        next_el = next_sid.split("#")[0] if next_sid else None
        
        is_turn_end = (curr_el != next_el)
        s_num = int(sid.split("#")[1])
        
        if is_turn_end:
            PAUSES[sid] = 0.8
        elif s_num % 2 == 0:
            PAUSES[sid] = 0.6
        elif sid in SPECIAL_EMOTIONS:
            PAUSES[sid] = 0.7

build_pauses()

output_data = {
    "_meta": {
        "episode": "20",
        "description": "Acting & Pause parameters for Tap 20 (241 sentences)",
        "total_sentences": 241,
        "pause_count": len(PAUSES),
    },
    "_pause_after": PAUSES,
}

for el in SCRIPT:
    if el["kind"] != "LOI":
        continue
    act = el["id"].split(".")[0]
    raw_role = el["role"]
    role = N_ELEMENT.get(el["id"], raw_role)
    
    mood_default, speed_default = ACT_MOOD.get((act, role), ("neutral", 0.0))
    
    for s in el["sentences"]:
        sid = s["id"]
        text = s["text"]
        
        mood, speed_tweak = SPECIAL_EMOTIONS.get(sid, (mood_default, speed_default))
        final_speed = BASE_DELTA.get(role, -0.02) + speed_tweak
        final_speed = round(max(-0.06, min(0.02, final_speed)), 3)
        
        entry = {
            "emotion": mood,
            "speed": final_speed,
            "pitch": 0,
            "text": text,
        }
        output_data[sid] = entry

out_file = WORK / "acting_tap20.json"
out_file.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {out_file.name}: {len(output_data) - 2} sentences ({len(PAUSES)} pauses, {round(len(PAUSES)/(len(output_data)-2)*100, 1)}%)")
