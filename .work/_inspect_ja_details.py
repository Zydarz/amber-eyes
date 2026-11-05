import json
from pathlib import Path

W = Path(".work")

with open(W / "timeline_s_JA_t02.json", "r", encoding="utf-8") as f:
    tl = json.load(f)

print("Timeline keys:", list(tl.keys())[:10])
print("Timeline total:", tl.get("total"))
sents = tl.get("sentences", {})
print("Type of sentences:", type(sents), "len:", len(sents))
if isinstance(sents, dict):
    first_keys = list(sents.keys())[:5]
    print("First sentence keys:", first_keys)
    if first_keys:
        print("First sent:", sents[first_keys[0]])
    last_keys = list(sents.keys())[-5:]
    print("Last sentence keys:", last_keys)
    if last_keys:
        print("Last sent:", sents[last_keys[-1]])

with open(W / "shots_JA_t02.json", "r", encoding="utf-8") as f:
    shots = json.load(f)

print("Shots type:", type(shots))
if isinstance(shots, dict):
    print("Shots keys:", list(shots.keys())[:10])
    for k in list(shots.keys())[:3]:
        print(f"shots[{k}]:", type(shots[k]), len(shots[k]) if hasattr(shots[k], '__len__') else shots[k])
        if isinstance(shots[k], list) and shots[k]:
            print(f"  sample: {shots[k][0]}")
elif isinstance(shots, list):
    print("Shots len:", len(shots))
    print("First shot:", shots[0])
