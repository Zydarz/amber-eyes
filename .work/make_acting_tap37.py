#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap37.json — Acting and pauses for Episode 37 (Harold Shipman).
Follows rules G1-G8, G10, A13, and qc_pause_gate standards.
"""
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap37.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
N_ELEMENT = {"1.05": "N1", "3.03": "N2"}

# Base speed deltas per character
BASE_DELTA = {"H": -0.02, "D": -0.02, "C": -0.02, "N1": -0.02, "N2": -0.02}

# Default emotion per act and role
ACT_MOOD = {
    ("1", "H"): ("neutral", 0.0),
    ("1", "D"): ("neutral", 0.0),
    ("1", "N1"): ("sad", -0.02),
    ("1", "C"): ("neutral", 0.0),
    ("2", "H"): ("neutral", 0.0),
    ("2", "D"): ("neutral", 0.0),
    ("2", "C"): ("neutral", 0.0),
    ("3", "H"): ("neutral", 0.0),
    ("3", "D"): ("neutral", 0.0),
    ("3", "N2"): ("fearful", -0.02),
    ("3", "C"): ("neutral", 0.0),
    ("4", "H"): ("neutral", 0.0),
    ("4", "D"): ("neutral", 0.0),
    ("4", "C"): ("neutral", 0.0),
    ("5", "H"): ("neutral", 0.0),
    ("5", "D"): ("neutral", 0.0),
    ("5", "C"): ("neutral", 0.0),
}

# Special sentence emotions and speed tweaks
SPECIAL_EMOTIONS = {
    "1.02#7": ("fearful", -0.02),
    "1.05#1": ("fearful", -0.02),
    "1.05#6": ("fearful", -0.02),
    "1.05#11": ("fearful", -0.02),
    "2.02#6": ("sad", -0.02),
    "2.02#9": ("sad", -0.03),
    "2.04#7": ("fearful", -0.02),
    "2.04#10": ("fearful", -0.03),
    "3.03#1": ("fearful", -0.02),
    "3.03#4": ("fearful", -0.03),
    "3.03#11": ("fearful", -0.03),
    "4.02#3": ("sad", -0.02),
    "4.04#6": ("fearful", -0.02),
    "5.04#4": ("fearful", -0.02),
}

def pause_for(script, el_idx, s_idx, total_s, role, text):
    if s_idx == total_s - 1:
        if el_idx + 1 < len(script):
            next_el = script[el_idx + 1]
            if next_el.get("kind") in ("BGM", "SFX"):
                return 1.0
            if next_el.get("role") != role:
                return 0.85
        return 0.8
    else:
        if text.endswith("?") or text.endswith(":"):
            return 0.7
        if len(text.split()) > 25:
            return 0.65
        return 0.6

def main():
    acting = {}
    pause_after = {}

    for el_idx, el in enumerate(SCRIPT):
        if el.get("kind") != "LOI":
            continue
        role = el["role"]
        el_id = el["id"]
        act_num = el_id.split(".")[0]

        if el_id in N_ELEMENT:
            role = N_ELEMENT[el_id]

        sents = el.get("sentences", [])
        for s_idx, s in enumerate(sents):
            s_id = s["id"]
            text = s["text"]

            default_emo, default_spd = ACT_MOOD.get((act_num, role), ("neutral", 0.0))
            emo, spd_offset = SPECIAL_EMOTIONS.get(s_id, (default_emo, default_spd))

            base_delta = BASE_DELTA.get(role, -0.02)
            final_spd_delta = round(base_delta + spd_offset, 3)

            acting[s_id] = {
                "role": role,
                "emotion": emo,
                "speed_delta": final_spd_delta,
                "text": text,
            }
            pause_after[s_id] = pause_for(SCRIPT, el_idx, s_idx, len(sents), role, text)

    out_file = WORK / "acting_tap37.json"
    data = {
        "acting": acting,
        "pause_after": pause_after,
        "total_sentences": len(acting),
    }
    out_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {out_file} with {len(acting)} sentences.")

if __name__ == "__main__":
    main()
