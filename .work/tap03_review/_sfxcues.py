import json, re, collections
p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
d = json.load(open(p, encoding="utf-8"))
els = d["elements"] if isinstance(d, dict) and "elements" in d else d
sfx = [e for e in els if str(e.get("type","")).upper() in ("SFX","AMBIENCE","AMBI","BGM")]
print("Tong so phan tu khuong nhac:", len(sfx))
for e in sfx:
    print(e.get("id"), "|", e.get("type"), "|", e.get("text","")[:140].replace("\n"," "))
