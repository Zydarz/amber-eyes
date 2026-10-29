import json, sys
sys.stdout.reconfigure(encoding='utf-8')
prov = json.load(open("provenance.json", encoding="utf-8"))
for p in prov:
    if "t05" in p.get("file", ""):
        print(json.dumps(p, ensure_ascii=False, indent=2))
        break
