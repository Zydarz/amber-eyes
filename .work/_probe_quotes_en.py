import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
els = json.load(open(r"D:/TEST/Gax/amber-eyes/.work/script_tap02_EN.json", encoding="utf-8"))
bad = 0
for e in els:
    if e.get("kind") != "LOI": continue
    for s in e["sentences"]:
        t = s["text"]
        # nhay cong lon '“' hoac '”' o giua tu (khong phai dau trich dan)
        for m in re.finditer(r"[A-Za-z][“”][A-Za-z]", t):
            print(f"{s['id']}: ...{t[max(0,m.start()-45):m.end()+45]}...")
            bad += 1
print("TONG loi:", bad)
