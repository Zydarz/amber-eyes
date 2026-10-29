import json, re, sys

# Load script
script = json.load(open(".work/script_tap05.json", encoding="utf-8"))
sent_dict = {}
for el in script:
    if el.get("kind") == "LOI":
        for s in el.get("sentences", []):
            sent_dict[s["id"]] = s["text"]

print(f"Total sentences: {len(sent_dict)}")
