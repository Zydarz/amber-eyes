#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L — Liet ke ung vien giong NAM trong catalog 332 + kiem tra 2 giong legacy co song khong."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(__file__).resolve().parents[1] / ".work"
live = json.loads((WORK / "_voice_list_live_20261027.json").read_text(encoding="utf-8-sig"))
vs = live["available_voices"]


def is_male(vid, name):
    s = f"{vid} {name}".lower()
    # thu tu quan trong: "female" chua "male", "woman" chua "man"
    if any(k in s for k in ("female", "woman", "girl", "lady", "queen", "sir")):
        return False
    return any(k in s for k in (" man", "_man", "man_", "male", "boy", "gentleman", "guy"))


males = [(v["voice_id"], v["voice_name"]) for v in vs if is_male(v["voice_id"], v["voice_name"])]
print(f"Tong giong trong catalog: {len(vs)}   -> gioi tinh NAM (suy tu ten): {len(males)}")
print()
for vid, nm in males:
    print(f"   {vid:42s} | {nm}")
print()

DONE = {"Korean_ColdYoungMan", "English_Deep-VoicedGentleman", "English_expressive_narrator"}
cand = [m for m in males if m[0] not in DONE]
print(f"UNG VIEN CHUA DO (tru 3 giong da do): {len(cand)}")
print()
for vid, nm in cand:
    print(f"   {vid:42s} | {nm}")
