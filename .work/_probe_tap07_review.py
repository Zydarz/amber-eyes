import json, sys
sys.stdout.reconfigure(encoding="utf-8")

with open(".work/script_tap07.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for el in data:
    if el.get("kind") == "LOI":
        for s in el.get("sentences", []):
            if ":" in s["text"]:
                print(f"[{s['id']}] {s['text']}")
