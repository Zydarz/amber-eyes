import json
s = json.load(open(".work/_cu/shots_EN_t02_20261031_233834.json", encoding="utf-8"))
for sh in s["shots"][:12]:
    print(f"{sh['id']:5s} | {sh['role']} | {sh['template']} | {sh['bg']:20s} | {sh['sentences']} | {sh['segments']}")
