import json
s = json.load(open(".work/shots_EN_t02.json", encoding="utf-8"))
print(json.dumps(s["shots"][1], indent=2))
print(json.dumps(s["shots"][5], indent=2))
print(json.dumps(s["shots"][6], indent=2))
