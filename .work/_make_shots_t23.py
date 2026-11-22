# Tao shots_{,EN_,JA_}t23.json tu bg_jobs_tap23.json (bang shot VN trong KeHoach da loi thoi: 224 dong/245 cau).
# Phan bo theo thu tu cau: job co dai cau lech thu tu / chong lan bi bo (bao cao 'unused'); job 'The ket' = doan sau loi cuoi.
import json, re
from pathlib import Path
W = Path(__file__).parent
jobs = json.load(open(W/"bg_jobs_tap23.json", encoding="utf-8"))
for lang, suf in (("VI", ""), ("EN", "_EN"), ("JA", "_JA")):
    TL = json.load(open(W/f"timeline_s{suf}_t23.json", encoding="utf-8"))
    ids = [i["id"] for i in TL["items"]]; st = {i["id"]: i for i in TL["items"]}; pos = {s: n for n, s in enumerate(ids)}
    shots = []; nxt = 0; skipped = []; endcard = None
    for j in jobs:
        f = re.findall(r"\d\.\d+#\d+", j["sentences"])
        if not f: endcard = j["name"]; continue
        b = pos[f[-1]]
        if b < nxt or pos[f[0]] > b: skipped.append(j["name"]); continue
        shots.append({"id": f"s{len(shots)+1:03d}", "sentences": ids[nxt:b+1], "bg": j["name"], "start": round(st[ids[nxt]]["start"] - (0.2 if nxt == 0 else 0), 3)}); nxt = b + 1
    assert nxt == len(ids), (lang, nxt, len(ids))
    if endcard:
        shots.append({"id": f"s{len(shots)+1:03d}", "sentences": [], "bg": endcard, "start": round(st[ids[-1]]["end"] + 0.0, 3)})
    for i, s in enumerate(shots): s["end"] = shots[i+1]["start"] if i+1 < len(shots) else TL["total"]
    json.dump({"total": TL["total"], "shots": shots}, open(W/f"shots{suf}_t23.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    d = [round(s["end"]-s["start"], 1) for s in shots]
    print(lang, len(shots), "shot · min", min(d), "max", max(d), ">15s", sum(x > 15 for x in d), ">30s", sum(x > 30 for x in d), "· job bỏ", len(skipped), skipped)
