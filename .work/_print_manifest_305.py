import json
m = json.load(open(".work/tts_manifest_EN_t02.json", encoding="utf-8"))
for x in m:
    if x["id"].startswith("3.05") or x["id"].startswith("3.07") or x["id"].startswith("3.08"):
        print(f"{x['id']:8s} : {x['text']}")
