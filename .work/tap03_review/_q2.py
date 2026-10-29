import json
p = r"D:\TEST\Gax\Audi\.work\script_tap02.json"
els = json.load(open(p, encoding="utf-8"))
n = 0
for e in els:
    if e["kind"] != "LOI":
        continue
    for s in e["sentences"]:
        if "\u201c" in s["text"] or "\u201d" in s["text"]:
            print(f'{s["id"]:<10} | {s["text"][:150]}')
            n += 1
    if n > 14:
        break
