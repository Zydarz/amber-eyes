import json
from pathlib import Path
from collections import Counter
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
sh = json.loads((W/"shots_t03.json").read_text(encoding="utf-8-sig"))
S = sh["shots"]
print("camera:", Counter(s["camera"] for s in S))
print("template:", Counter(s["template"] for s in S))
print("transition:", Counter(s["transition"] for s in S))
durs = [(s["id"], round(s["end"]-s["start"],1), s["camera"]) for s in S]
print("\nSHOT > 20s:")
for i,(sid,d,c) in enumerate(durs):
    if d > 20: print(f"  {sid:6s} {d:5.1f}s  cam={c}")
print(f"\n>15s: {sum(1 for _,d,_ in durs if d>15)}   <3s: {sum(1 for _,d,_ in durs if d<3)}   trung binh {sum(d for _,d,_ in durs)/len(durs):.1f}s")
print("\nSHOT < 3s:")
for sid,d,c in durs:
    if d < 3: print(f"  {sid:6s} {d:5.1f}s cam={c}")
