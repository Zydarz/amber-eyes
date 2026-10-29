import json

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
els = json.load(open(p, encoding="utf-8"))
for e in els:
    if e.get("id") in ("1.05", "1.07", "4.05", "5.02"):
        print("=" * 18, e["id"], "=" * 18)
        for s in e["sentences"]:
            print(f'  {s["id"]:<10} {s["text"][:120]}')
