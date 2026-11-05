import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(r"D:/TEST/Gax/amber-eyes/.work/shots_EN_t02.json", encoding="utf-8"))
tl = json.load(open(r"D:/TEST/Gax/amber-eyes/.work/timeline_s_EN_t02.json", encoding="utf-8"))
S = {i["id"]: i for i in tl["items"]}
print("--- shot co thoi luong am ---")
for s in d["shots"]:
    dur = s["end"] - s["start"]
    if dur <= 0:
        print(f"  {s['id']}: {dur:.1f}s  sent={s['sentences']} tmpl={s['template']} hold={s.get('hold')} inherit={s.get('inherit')}")
        for sid in s["sentences"]:
            print(f"      {sid}: {S[sid]['start']} -> {S[sid]['end']}")
print("--- shot > 40s ---")
for s in d["shots"]:
    dur = s["end"] - s["start"]
    if dur > 40:
        print(f"  {s['id']}: {dur:.1f}s  sent={s['sentences']}")
print("--- ACT markers ---")
for m in tl["markers"]:
    if m["type"] == "ACT":
        print("   ", json.dumps(m, ensure_ascii=False))
print("--- acts ---", tl.get("acts"))
