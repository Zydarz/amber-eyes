import json, sys
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(r"D:/TEST/Gax/amber-eyes/.work/shots_text_tap02_EN.json", encoding="utf-8"))
for k in ("3-19","3-20","3-21","4-17","4-18","4-19"):
    if k in d: print(k, "->", json.dumps(d[k], ensure_ascii=False))
print()
els = json.load(open(r"D:/TEST/Gax/amber-eyes/.work/script_tap02_EN.json", encoding="utf-8"))
for e in els:
    if e.get("kind") != "LOI": continue
    for s in e["sentences"]:
        if s["id"] in ("3.08#10","3.08#11","4.10#6","4.10#5"):
            print(s["id"], ":", s["text"])
