import json
import re

script = json.loads(open(".work/script_tap04.json", encoding="utf-8").read())

sents_dict = {}
for e in script:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents_dict[s["id"]] = s["text"]

print(f"Total script sentences: {len(sents_dict)}")
