import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).resolve().parents[1] / ".work"

en_table = json.load(open(W / "shots_text_tap02_EN.json", encoding="utf-8"))
shots = json.load(open(W / "_shots_analysis.json", encoding="utf-8"))

quotes = []
numbers = []
for s in shots:
    sid = s["sid"]
    chu_en = s["chu_en"]
    q_matches = re.findall(r"“([^”]+)”", chu_en)
    if q_matches:
        quotes.append((sid, q_matches, s["ctx_ja"]))
    nums = re.findall(r"\d+", re.sub(r"→\s*`#\d+`:", " ", chu_en))
    if nums:
        numbers.append((sid, nums, chu_en, s["ctx_ja"]))

print(f"Shots with quotes: {len(quotes)}")
for sid, q, ctx in quotes:
    print(f"{sid}: quotes={q}")
    print(f"  ctx_ja={ctx}")

print(f"\nTotal shots with numbers: {len(numbers)}")
