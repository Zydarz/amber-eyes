import json, sys
sys.stdout.reconfigure(encoding='utf-8')
prov = json.load(open("provenance.json", encoding="utf-8"))
for p in prov:
    if "fx_sigh_emotional" in p.get("file", ""):
        print(p.get("file"), "-> track:", p.get("track_youtube"), "| mo_ta:", p.get("mo_ta"))
