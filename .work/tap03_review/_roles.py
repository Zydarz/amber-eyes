import json
from collections import Counter
els = json.load(open(r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json", encoding="utf-8"))
loi = [e for e in els if e["kind"] == "LOI"]
print("LOI turns:", len(loi), Counter(e["role"] for e in loi))
print("words:", sum(s["words"] for e in loi for s in e["sentences"]))
print("sentences:", sum(len(e["sentences"]) for e in loi))
