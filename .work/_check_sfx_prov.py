import json, sys
sys.stdout.reconfigure(encoding='utf-8')
prov = json.load(open("provenance.json", encoding="utf-8"))
t05_sfx = [p for p in prov if "t05" in p.get("file", "") or "floppy" in p.get("file", "") or "server_fan" in p.get("file", "")]
for p in t05_sfx:
    print(p.get("file"), "|", p.get("tool"), "|", p.get("license"), "|", p.get("commercial_ok"))
