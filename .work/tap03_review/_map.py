import json
from collections import Counter

p = r"D:\TEST\Gax\Audi\.work\script_tap03.json"
els = json.load(open(p, encoding="utf-8"))
print("total elements:", len(els))
print("kinds:", Counter(e["kind"] for e in els))
words = 0
for e in els:
    if e["kind"] == "LOI":
        words += sum(s["words"] for s in e["sentences"])
        first = e["text"][:50].replace("\n", " ")
        print(f'{e["id"]:>6} {e["role"]:<3} {len(e["sentences"]):>2}s  {first}')
print("total words (LOI):", words)
