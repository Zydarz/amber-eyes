import json, sys
sys.stdout.reconfigure(encoding="utf-8")
for tag, f in (("EN","shots_EN_t02.json"),("JA","shots_JA_t02.json"),("KO","shots_KO_t02.json")):
    d = json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/{f}", encoding="utf-8"))
    sh = d["shots"]
    durs = [(s["id"], round(s["end"]-s["start"],1)) for s in sh]
    neg = [x for x in durs if x[1] <= 0]
    long = sorted([x for x in durs if x[1] > 15], key=lambda x:-x[1])
    print(f"{tag}: {len(sh)} shot · am={len(neg)} {neg[:4]} · >15s={len(long)} dai nhat {long[:4]}")
