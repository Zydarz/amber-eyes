import json, sys
sys.stdout.reconfigure(encoding='utf-8')
prov = json.load(open("provenance.json", encoding="utf-8"))
for p in prov:
    f = p.get("file", "")
    if any(k in f for k in ["sigh", "breath", "crying", "sob"]):
        print(f, "-> track:", p.get("track_youtube"), "| mo_ta:", p.get("mo_ta"))
