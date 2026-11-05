import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
for lang in ("VN","EN","JA","KO"):
    els = json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/script_tap02_{lang}.json", encoding="utf-8"))
    cnt = {}
    for e in els:
        if e.get("kind") != "LOI": continue
        for s in e["sentences"]:
            t = s["text"]
            for m in re.finditer(r"[A-Za-zÀ-ỹ぀-ヿ一-鿿가-힯][“”‘’][A-Za-zÀ-ỹ぀-ヿ一-鿿가-힯]", t):
                cnt.setdefault(m.group(0), []).append(s["id"])
            # nhay cong lap ngay sau dau cham
            for m in re.finditer(r"[:：]\s*”", t):
                cnt.setdefault(": ”", []).append(s["id"])
    print(f"=== {lang}: {sum(len(v) for v in cnt.values())} loi")
    for k, v in cnt.items():
        print("   ", repr(k), len(v), v[:6])
