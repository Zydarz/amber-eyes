import json
for f in ["shots_text_tap02_EN.json","shots_text_tap02_JA.json"]:
    d = json.load(open("D:/TEST/Gax/amber-eyes/.work/"+f, encoding="utf-8"))
    d = {k:v for k,v in d.items() if not k.startswith("_")}
    print("==",f,len(d),"last keys:",list(d)[-4:])
    for k in list(d)[-4:]:
        print("  ",k, json.dumps(d[k], ensure_ascii=False))
