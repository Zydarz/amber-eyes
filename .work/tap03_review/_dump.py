import json

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
els = json.load(open(p, encoding="utf-8"))
for e in els:
    if e["kind"] != "LOI":
        kind = e["kind"]
        extra = f' [{e.get("sec","")}s]' if kind == "NGHI" else ""
        print(f'{e["id"]:<7} {kind}{extra}')
        continue
    print(f'{e["id"]:<7} LOI {e["role"]}')
    for s in e["sentences"]:
        print(f'    {s["id"]:<10} {s["text"][:118]}')
