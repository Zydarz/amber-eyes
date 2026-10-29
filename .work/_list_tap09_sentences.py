import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open(".work/script_tap09.json", encoding="utf-8") as f:
    d = json.load(f)

for t in d:
    if t.get("kind") == "LOI":
        act = t.get("act")
        role = t.get("role")
        for s in t.get("sentences", []):
            print(f"[{act}] {s['id']} ({role}): {s['text']}")
