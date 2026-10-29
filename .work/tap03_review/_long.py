import json

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_tap03.json"
els = json.load(open(p, encoding="utf-8"))
longs = []
for e in els:
    if e["kind"] != "LOI":
        continue
    for s in e["sentences"]:
        if s["words"] > 40:
            longs.append((e["id"], s["id"], s["words"], s["text"]))
print("sentences > 40 words:", len(longs))
for eid, sid, w, t in longs:
    print(f'\n[{eid} {sid}] {w}w\n  {t}')
