#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .work/acting_tap34.json — Acting and pauses for Episode 34 (Nguyen Duc Nghia).
Follows rules G1-G8, G10, A13, and qc_pause_gate standards.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
SCRIPT_PATH = WORK / "script_tap34.json"

if not SCRIPT_PATH.exists():
    raise FileNotFoundError(f"Missing {SCRIPT_PATH}")

SCRIPT = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
N_ELEMENT = {"1.04": "N1", "4.04": "N2", "5.04": "N1"}

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
    ("3", "C"): ("neutral", 0.0),
    ("4", "H"): ("neutral", 0.0),
    ("4", "D"): ("neutral", 0.0),
    ("4", "N2"): ("sad", -0.03),
    ("4", "C"): ("neutral", 0.0),
    ("5", "H"): ("neutral", 0.0),
    ("5", "D"): ("neutral", 0.0),
    ("5", "N1"): ("sad", -0.02),
    ("5", "C"): ("neutral", 0.0),
}

# Special sentence emotions and speed tweaks
SPECIAL_EMOTIONS = {
    # Act 1
    "1.02#5": ("fearful", -0.02),
    "1.02#10": ("fearful", -0.02),
    "1.03#4": ("fearful", -0.02),
    "1.04#1": ("fearful", -0.02),
    "1.04#4": ("fearful", -0.03),
    "1.04#5": ("fearful", -0.03),
    "1.05#4": ("neutral", 0.0),
    # Act 2
    "2.02#6": ("sad", -0.02),
    "2.02#9": ("fearful", -0.02),
    "2.03#5": ("fearful", -0.02),
    "2.04#5": ("fearful", -0.02),
    "2.04#6": ("neutral", 0.0),
    # Act 3
    "3.02#3": ("neutral", -0.02),
    "3.02#6": ("fearful", -0.02),
    "3.03#6": ("neutral", 0.0),
    "3.04#3": ("fearful", -0.02),
    "3.05#5": ("neutral", 0.0),
    # Act 4
    "4.02#5": ("sad", -0.02),
    "4.03#5": ("sad", -0.03),
    "4.03#6": ("sad", -0.03),
    "4.04#1": ("sad", -0.03),
    "4.04#4": ("fearful", -0.03),
    "4.04#5": ("sad", -0.03),
    "4.05#2": ("fearful", -0.02),
    "4.06#5": ("sad", -0.03),
    "4.07#5": ("sad", -0.02),
    # Act 5
    "5.02#5": ("neutral", 0.0),
    "5.03#4": ("neutral", 0.0),
    "5.04#2": ("sad", -0.02),
    "5.04#5": ("sad", -0.02),
    "5.05#4": ("neutral", 0.0),
    "5.06#3": ("neutral", 0.0),
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

def main():
    acting = {}
    pause_after = {}

    for el_idx, el in enumerate(SCRIPT):
        if not el.get("role"):
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

    out_file = WORK / "acting_tap34.json"
    data = {
        "acting": acting,
        "pause_after": pause_after,
        "total_sentences": len(acting),
    }
    out_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {out_file} with {len(acting)} sentences.")

if __name__ == "__main__":
    main()
