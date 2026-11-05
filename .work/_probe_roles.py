import json, sys
sys.stdout.reconfigure(encoding="utf-8")
def roles(tag):
    els = json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/script_tap02_{tag}.json", encoding="utf-8"))
    r = {}
    for e in els:
        if e.get("kind") == "LOI":
            r[e["id"]] = e["role"]
    return r
vn, en, ja, ko = roles("VN"), roles("EN"), roles("JA"), roles("KO")
print("VN vs EN:")
for k in sorted(set(vn) | set(en)):
    if vn.get(k) != en.get(k):
        print(f"   {k}: VN={vn.get(k)}  EN={en.get(k)}")
print("VN vs JA:")
for k in sorted(set(vn) | set(ja)):
    if vn.get(k) != ja.get(k):
        print(f"   {k}: VN={vn.get(k)}  JA={ja.get(k)}")
print("VN vs KO:")
for k in sorted(set(vn) | set(ko)):
    if vn.get(k) != ko.get(k):
        print(f"   {k}: VN={vn.get(k)}  KO={ko.get(k)}")
