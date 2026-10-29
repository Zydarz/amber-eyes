import json

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_tap03.json"
els = json.load(open(p, encoding="utf-8"))
for e in els:
    if e.get("id") in ("4.08", "5.08", "3.08"):
        print("=" * 20, e["id"], "=" * 20)
        for s in e["sentences"]:
            print(f'  [{s["words"]:>3}w] {s["text"][:160]}')
