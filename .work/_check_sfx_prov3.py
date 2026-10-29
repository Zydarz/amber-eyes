import json, sys
sys.stdout.reconfigure(encoding='utf-8')
prov = json.load(open("provenance.json", encoding="utf-8"))
for p in prov:
    if "assets/sfx/t05" in p.get("file", ""):
        print(p.get("file"), "-> track:", p.get("track_youtube"), "| nguon:", p.get("nguon_goc"), "| cat:", p.get("cat_goc"))
