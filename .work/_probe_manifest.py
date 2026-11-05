import json
for tag in ["JA","EN",""]:
    p = rf"D:/TEST/Gax/amber-eyes/.work/tts_manifest{('_'+tag) if tag else ''}_t02.json"
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        print(tag or "VI", "ERR", e); continue
    print("=== ", tag or "VI", type(d).__name__, len(d))
    if isinstance(d, dict):
        k = list(d)[:3]
        for kk in k:
            print("   ", kk, "->", str(d[kk])[:200])
    else:
        for it in d[:3]:
            print("   ", str(it)[:250])
