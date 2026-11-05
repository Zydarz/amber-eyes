import json
for tag in ["", "_EN", "_JA"]:
    p = rf"D:/TEST/Gax/amber-eyes/.work/timeline_s{tag}_t02.json"
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        print(tag or "VI", "ERR", e); continue
    print("===", tag or "VI", list(d.keys()))
    print("   items:", len(d["items"]), "markers:", len(d.get("markers", [])))
    print("   item0:", json.dumps(d["items"][0], ensure_ascii=False))
    print("   itemN:", json.dumps(d["items"][-1], ensure_ascii=False))
    ms = [m for m in d.get("markers", [])][:4]
    for m in ms: print("   marker:", json.dumps(m, ensure_ascii=False))
    for k in d:
        if k not in ("items","markers"): print("   other:", k, str(d[k])[:200])
