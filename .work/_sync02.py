import json, re
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
for ep, tl_f in (("02","timeline_s_t02.json"), ("03","timeline_s_t03.json")):
    tl = json.loads((W/tl_f).read_text(encoding="utf-8-sig"))
    sh = json.loads((W/f"shots_t{ep}.json").read_text(encoding="utf-8-sig"))
    ids = {i["id"] for i in tl["items"]}
    used = [x for s in sh["shots"] for x in s["sentences"]]
    print(f"--- Tap{ep} ---")
    print(f"  timeline items={len(ids)}  shots={len(sh['shots'])}  used sents={len(used)}  unique={len(set(used))}")
    print(f"  used khong ton tai: {sorted(set(used)-ids)[:10]}")
    print(f"  thieu: {sorted(ids-set(used))[:10]}")
    print(f"  shots.total={sh.get('total')}  timeline.total={tl['total']}")
