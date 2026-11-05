import json, sys
sys.stdout.reconfigure(encoding="utf-8")
for tag in ("t02","EN_t02","JA_t02","KO_t02"):
    d = json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/shots_{tag}.json", encoding="utf-8"))
    ids = [s["id"] for s in d["shots"]]
    for tgt in ("3-20", "5-36", "1-01"):
        if tgt in ids:
            i = ids.index(tgt)
            print(f"{tag}: {tgt} -> sheet_{i//9+1:02d} (vi tri {i})")
