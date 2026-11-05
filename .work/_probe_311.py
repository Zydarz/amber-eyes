import json, sys
sys.stdout.reconfigure(encoding="utf-8")
def get(tag):
    els = json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/script_tap02_{tag}.json", encoding="utf-8"))
    d = {}
    for e in els:
        if e.get("kind") == "LOI":
            d[e["id"]] = [s["text"] for s in e["sentences"]]
    return d
vn, ja, ko, en = get("VN"), get("JA"), get("KO"), get("EN")
for el in ("3.11", "3.10", "3.12"):
    print(f"=== {el}")
    print("  VN:", " | ".join(vn.get(el, []))[:400])
    print("  JA:", " | ".join(ja.get(el, []))[:400])
    print("  EN:", " | ".join(en.get(el, []))[:400])
    print("  KO:", " | ".join(ko.get(el, []))[:400])
