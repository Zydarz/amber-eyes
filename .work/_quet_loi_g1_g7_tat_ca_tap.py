# -*- coding: utf-8 -*-
"""H: Quet moi manifest (VN) xem loi G1 ('...') va G7 (chu thich trong ngoac) co lan sang tap khac khong."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(__file__).resolve().parents[1] / ".work"

files = {
    "Tập 01": "tts_manifest.json", "Tập 02": "tts_manifest_t02.json",
    "Tập 03": "tts_manifest_t03.json", "Tập 04": "tts_manifest_t04.json",
    "Tập 05": "tts_manifest_t05.json", "Tập 06": "tts_manifest_t06.json",
    "Tập 07": "tts_manifest_t07.json",
}
tot_d = tot_p = 0
print(f"{'Tap':8s} {'cau':>5s}  {'G1 \"...\"':>9s}  {'G7 (ngoac)':>11s}   chi tiet")
for ep, fn in files.items():
    p = WORK / fn
    if not p.exists():
        continue
    items = json.loads(p.read_text(encoding="utf-8"))
    dots = [x for x in items if "..." in x["text"]]
    par = [x for x in items if re.search(r"\([^)]*[A-Za-z][^)]*\)", x["text"])]
    tot_d += len(dots)
    tot_p += len(par)
    det = ", ".join(f"{x['id']}[{x['role']}]" for x in (dots + par))
    print(f"{ep:8s} {len(items):5d}  {len(dots):9d}  {len(par):11d}   {det}")
print(f"\nTONG: G1 = {tot_d} cau, G7 = {tot_p} cau")
print("\n--- G7 chi tiet (tat ca tap) ---")
for ep, fn in files.items():
    p = WORK / fn
    if not p.exists():
        continue
    items = json.loads(p.read_text(encoding="utf-8"))
    for x in items:
        if re.search(r"\([^)]*[A-Za-z][^)]*\)", x["text"]):
            print(f"  {ep} {x['id']:8s} [{x['role']}] {x['text'][:150]}")
