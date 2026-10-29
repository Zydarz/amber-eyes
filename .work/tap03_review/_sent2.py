import json
p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
els = json.load(open(p, encoding="utf-8"))
byid = {e["id"]: e for e in els}
for i in ["2.06", "3.05"]:
    e = byid[i]
    print(f"--- {i} ---")
    for s in e["sentences"]:
        print(f"  {s['id']:<9} {s['text']}")
