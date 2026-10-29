import json, re, sys
from pathlib import Path

# Load script
script = json.load(open(".work/script_tap05.json", encoding="utf-8"))
all_sents = []
for el in script:
    if el.get("kind") == "LOI":
        for s in el.get("sentences", []):
            all_sents.append(s["id"])

print(f"Total script sentences: {len(all_sents)}")
