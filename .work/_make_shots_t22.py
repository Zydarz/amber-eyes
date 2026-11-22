# Tao shots_{,EN_,JA_}t22.json tu bg_jobs_tap22.json (moi anh = 1 shot, dai cau 'a–b') + timeline do tu SRT. Nen dung chung 3 ngon ngu.
import json, re
from pathlib import Path
W = Path(__file__).parent
jobs = json.load(open(W/"bg_jobs_tap22.json", encoding="utf-8"))
for lang, suf in (("VI", ""), ("EN", "_EN"), ("JA", "_JA")):
    TL = json.load(open(W/f"timeline_s{suf}_t22.json", encoding="utf-8"))
    ids = [i["id"] for i in TL["items"]]; st = {i["id"]: i for i in TL["items"]}; pos = {s: n for n, s in enumerate(ids)}
    shots = []; nxt = 0
    for j in jobs:
        f = re.findall(r"\d\.\d+#\d+", j["sentences"]); a, b = pos[f[0]], pos[f[-1]]
        assert a == nxt and b >= a, (lang, j["name"], j["sentences"], nxt)
        shots.append({"id": f"s{len(shots)+1:03d}", "sentences": ids[a:b+1], "bg": j["name"], "start": round(st[ids[a]]["start"] - (0.2 if a == 0 else 0), 3)}); nxt = b + 1
    assert nxt == len(ids), (lang, nxt, len(ids))
    for i, s in enumerate(shots): s["end"] = shots[i+1]["start"] if i+1 < len(shots) else TL["total"]
    json.dump({"total": TL["total"], "shots": shots}, open(W/f"shots{suf}_t22.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    d = [round(s["end"]-s["start"], 1) for s in shots]
    print(lang, len(shots), "shot · min", min(d), "max", max(d), "· tổng nền", len({s['bg'] for s in shots}))
