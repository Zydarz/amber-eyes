# Tao shots_{,EN_,JA_}t21.json (dang don gian nhu T20) tu bang shot VI 'KeHoach_Video_Tap21.md' + timeline_s*_t21.json (do tu SRT).
# Nen dung CHUNG 3 ngon ngu; 1 shot = cac cau cua dong bang; moc lay tu timeline cua tung ngon ngu.
import json, re, sys
from pathlib import Path
W = Path(__file__).parent; R = W.parent
plan = (R/"02_SAN_XUAT/Ho_So_Toi_Pham/Tap21/KeHoach_Video_Tap21.md").read_text(encoding="utf-8")
sec = plan[re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M).end():]
rows = []
for l in sec.splitlines():
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|\s*(.*?)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*`([a-z0-9_]+)`", l)
    if m: rows.append((m[1], re.findall(r"\d\.\d+#\d+", m[2]), m[5]))
print("rows", len(rows), "no-sentence rows:", [r[0] for r in rows if not r[1]])
allsent = [s for r in rows for s in r[1]]
for lang, suf in (("VI", ""), ("EN", "_EN"), ("JA", "_JA")):
    TL = json.load(open(W/f"timeline_s{suf}_t21.json", encoding="utf-8"))
    st = {i["id"]: i for i in TL["items"]}
    ids = [i["id"] for i in TL["items"]]
    assert allsent == ids, (lang, len(allsent), len(ids), [ (a,b) for a,b in zip(allsent, ids) if a!=b][:3])
    shots = []
    for n, (sid, sents, bg) in enumerate(rows, 1):
        a = st[sents[0]]["start"] - (0.2 if n == 1 else 0.0)
        shots.append({"id": f"s{n:03d}", "plan_id": sid, "sentences": sents, "bg": bg, "start": round(a, 3)})
    for i, s in enumerate(shots):
        s["end"] = shots[i+1]["start"] if i+1 < len(shots) else TL["total"]
    json.dump({"total": TL["total"], "shots": shots}, open(W/f"shots{suf}_t21.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    d = [round(s["end"]-s["start"], 1) for s in shots]
    print(lang, len(shots), "shot · min", min(d), "max", max(d), "· nền riêng", len({s['bg'] for s in shots}))
