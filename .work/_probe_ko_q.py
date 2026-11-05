import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
els = json.load(open(r"D:/TEST/Gax/amber-eyes/.work/script_tap02_KO.json", encoding="utf-8"))
ids = {"1.05#3","1.08#4","3.08#7","3.08#8","3.08#9","3.11#6"}
for e in els:
    if e.get("kind") != "LOI": continue
    for s in e["sentences"]:
        if s["id"] in ids:
            print(f"{s['id']}: {s['text']}")
