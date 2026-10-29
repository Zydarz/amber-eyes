import json
p = r"D:\TEST\Gax\Audi\.work\sfx_tap02.json"
d = json.load(open(p, encoding="utf-8"))
print(type(d))
print(json.dumps(d, ensure_ascii=False, indent=1)[:2600])
