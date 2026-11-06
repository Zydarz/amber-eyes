import json
from pathlib import Path

WORK = Path("D:/TEST/Gax/amber-eyes/.work")
new = json.loads((WORK / "shots_t03.json").read_text(encoding="utf-8"))
old = json.loads((WORK / "_cu/t03_20261106_shots_t03.json.bak").read_text(encoding="utf-8"))

for tag, d in (("MOI", new), ("CU", old)):
    shots = d["shots"]
    durs = [(round(s["end"] - s["start"], 2), s["id"]) for s in shots]
    print(f"[{tag}] total={d['total']} shots={len(shots)}")
    print(f"   dai nhat 5 : {sorted(durs, reverse=True)[:5]}")
    print(f"   ngan nhat 5: {sorted(durs)[:5]}")
    over = [x for x in durs if x[0] > 15]
    under = [x for x in durs if x[0] < 3]
    print(f"   >15s: {len(over)} {over}")
    print(f"   <3s : {len(under)} {under}")
    # chuoi nen lap lien
    seq = [s["bg"] for s in shots]
    run, best, cur = 1, 1, 1
    for i in range(1, len(seq)):
        run = run + 1 if seq[i] == seq[i - 1] else 1
        best = max(best, run)
    print(f"   chuoi nen lap toi da: {best}")
    print()

# so sanh theo id
o = {s["id"]: s for s in old["shots"]}
n = {s["id"]: s for s in new["shots"]}
print("ID giong nhau:", set(o) == set(n))
diff = [(k, round(o[k]["start"], 2), round(n[k]["start"], 2)) for k in o if k in n and abs(o[k]["start"] - n[k]["start"]) > 0.01]
print(f"shot doi moc thoi gian: {len(diff)}")
for x in diff[:8]:
    print("   ", x)
print()
print("--- cac shot > 15s (moi) ---")
for s in new["shots"]:
    dd = s["end"] - s["start"]
    if dd > 15 or dd < 3:
        print(f"  {s['id']:>6s} {dd:7.2f}s  tmpl={s['template']} bg={s['bg']} "
              f"sent={len(s['sentences'])} hold={s['hold']} inherit={s.get('inherit','')}")
