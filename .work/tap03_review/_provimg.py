import json
p = r"D:\TEST\Gax\Audi\provenance.json"
d = json.load(open(p, encoding="utf-8"))
n = 0
for e in d:
    if e.get("file","").startswith("assets/bg/t3_"):
        print(json.dumps(e, ensure_ascii=False, indent=1))
        n += 1
        if n >= 2: break
print("--- so entry nen t3:", sum(1 for e in d if e.get("file","").startswith("assets/bg/t3_")))
