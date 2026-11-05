import json
t = json.load(open(".work/temp_verify_en_t02.json", encoding="utf-8"))
for e in t[:5]:
    print(e.get("id"), e.get("kind"), [s.get("id") for s in e.get("sentences", [])])
