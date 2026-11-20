#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap38.json — Acting and pauses for Episode 38 (Natascha Kampusch).
Follows rules G1-G8, G10, A13, and qc_pause_gate standards.
Target: 240 sentences, median pause >= 0.6s, <= 25% under 0.4s.
"""
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap38.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.05": "N2"}

# Base speed deltas per character
BASE_DELTA = {"H": -0.02, "D": -0.02, "C": -0.02, "N1": -0.02, "N2": -0.02}

# Default emotion per act and role
ACT_MOOD = {
    ("1", "H"): ("neutral", 0.0),
    ("1", "D"): ("neutral", 0.0),
    ("1", "N1"): ("fearful", -0.02),
    ("1", "C"): ("neutral", 0.0),
    ("2", "H"): ("neutral", 0.0),
    ("2", "D"): ("neutral", 0.0),
    ("2", "C"): ("neutral", 0.0),
    ("3", "H"): ("neutral", 0.0),
    ("3", "D"): ("neutral", 0.0),
    ("3", "C"): ("neutral", 0.0),
    ("4", "H"): ("neutral", 0.0),
    ("4", "D"): ("neutral", 0.0),
    ("4", "N2"): ("fearful", -0.02),
    ("4", "C"): ("neutral", 0.0),
    ("5", "H"): ("neutral", 0.0),
    ("5", "D"): ("neutral", 0.0),
    ("5", "C"): ("neutral", 0.0),
}

# Special sentence emotions and speed tweaks
SPECIAL_EMOTIONS = {
    "1.04#6": ("fearful", -0.02),
    "1.06#1": ("fearful", -0.02),
    "1.06#6": ("sad", -0.02),
    "1.07#3": ("fearful", -0.04),
    "1.07#5": ("sad", -0.02),
    "2.04#3": ("fearful", -0.02),
    "2.06#1": ("neutral", 0.0),
    "3.06#1": ("surprised", -0.02),
    "3.07#6": ("surprised", -0.02),
    "3.10#2": ("surprised", -0.02),
    "4.04#2": ("surprised", -0.02),
    "4.05#3": ("fearful", -0.04),
    "4.07#2": ("sad", -0.02),
    "4.10#3": ("sad", -0.02),
    "5.03#6": ("neutral", 0.0),
}

# End of act / turn long pause markers
LONG_PAUSES = {
    "1.02#12": 0.9,
    "1.04#6": 0.8,
    "1.06#6": 0.9,
    "1.07#5": 0.9,
    "1.09#5": 0.8,
    "1.10#7": 0.85,
    "1.11#5": 1.1,
    "2.02#6": 0.85,
    "2.04#10": 0.9,
    "2.05#5": 0.85,
    "2.06#12": 0.9,
    "2.07#4": 0.8,
    "2.08#7": 0.9,
    "2.09#4": 0.85,
    "2.10#6": 0.9,
    "2.11#3": 1.1,
    "3.02#4": 0.8,
    "3.04#4": 0.85,
    "3.05#7": 0.9,
    "3.06#4": 0.85,
    "3.07#11": 0.95,
    "3.08#8": 0.9,
    "3.09#8": 0.9,
    "3.10#3": 1.1,
    "4.02#5": 0.85,
    "4.03#9": 0.9,
    "4.04#5": 0.85,
    "4.05#8": 0.95,
    "4.07#6": 0.9,
    "4.08#4": 0.85,
    "4.09#9": 0.95,
    "4.10#6": 1.1,
    "5.02#8": 0.85,
    "5.03#7": 0.9,
    "5.04#6": 0.9,
    "5.05#12": 0.95,
    "5.05#15": 1.2,
}

out = {}
pauses = []

for elem in SCRIPT:
    if elem.get("kind") != "LOI":
        continue
    el_id = elem["id"]
    act = str(elem["act"])
    raw_role = elem["role"]
    role = N_ELEMENT.get(el_id, raw_role)

    sents = elem.get("sentences", [])
    for idx, s in enumerate(sents):
        sid = s["id"]
        words = s["words"]

        # Base emotion & delta
        base_emo, delta_tweak = ACT_MOOD.get((act, role), ("neutral", 0.0))
        speed_delta = BASE_DELTA.get(role, -0.02) + delta_tweak

        # Check special emotions
        if sid in SPECIAL_EMOTIONS:
            base_emo, speed_delta = SPECIAL_EMOTIONS[sid]

        # Calculate pause after (Rule A13: median >= 0.6s, <= 25% under 0.4s)
        if sid in LONG_PAUSES:
            pause = LONG_PAUSES[sid]
        elif idx == len(sents) - 1:
            pause = 0.8
        else:
            if words < 15:
                pause = 0.55
            elif words < 25:
                pause = 0.65
            elif words < 35:
                pause = 0.70
            else:
                pause = 0.75

        pauses.append(pause)
        out[sid] = {
            "emotion": base_emo,
            "speed_delta": round(speed_delta, 3),
            "pitch_delta": 0,
            "_pause_after": round(pause, 2),
        }

OUT_PATH = WORK / "acting_tap38.json"
OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

med = statistics.median(pauses)
under_04 = sum(1 for p in pauses if p < 0.4) / len(pauses) * 100

print(f"Generated {len(out)} acting sentences for Episode 38.")
print(f"Median pause: {med:.2f}s (Standard >= 0.60s: {'PASS' if med >= 0.6 else 'FAIL'})")
print(f"Pauses < 0.4s: {under_04:.1f}% (Standard <= 25%: {'PASS' if under_04 <= 25 else 'FAIL'})")
