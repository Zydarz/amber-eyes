import json, sys
sys.stdout.reconfigure(encoding="utf-8")
for tag in ("", "_EN"):
    d = json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/timeline_s{tag}_t02.json", encoding="utf-8"))
    print("===", tag or "VI", "total", d["total"], "acts", d.get("acts"))
    for m in d["markers"]:
        if m["type"] in ("ACT", "NGHI"):
            print("   ", json.dumps(m, ensure_ascii=False))
    print("   first item:", json.dumps(d["items"][0], ensure_ascii=False))
