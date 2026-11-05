import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
for tag, vd in (("EN","video3_EN_t02"),("JA","video3_JA_t02"),("KO","video3_KO_t02")):
    d = os.path.join(r"D:/TEST/Gax/amber-eyes/.work", vd, "stills")
    if not os.path.isdir(d): print(tag, "chua render"); continue
    ids = {f"shot_{s['id']}.png" for s in json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/shots_{tag}_t02.json", encoding="utf-8"))["shots"]}
    files = set(os.listdir(d))
    stale = sorted(files - ids)
    print(f"{tag}: {len(files)} file · thuoc bang shot moi: {len(files & ids)} · thua {len(stale)}: {stale[:10]}")
