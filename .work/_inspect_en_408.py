import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
s = json.load(open(".work/script_tap02_EN.json", encoding="utf-8"))
for e in s:
    if e.get("id") == "4.08":
        for x in e["sentences"]:
            print(f"{x['id']}: {x['text']}")
