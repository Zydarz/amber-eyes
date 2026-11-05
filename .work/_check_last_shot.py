import json

s = json.load(open(".work/shots_EN_t02.json", encoding="utf-8"))
last_shot = s["shots"][-1]
print(json.dumps(last_shot, indent=2))
