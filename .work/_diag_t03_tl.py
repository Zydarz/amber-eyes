import json
from pathlib import Path

tl = json.loads(Path(".work/timeline_s_t03.json").read_text(encoding="utf-8"))
items = tl["items"]
print("acts dict :", json.dumps(tl["acts"], ensure_ascii=False))
for a in range(1, 6):
    ai = [i for i in items if i["act"] == a]
    print("act %d: first %s start=%s | last %s end=%s | n=%d"
          % (a, ai[0]["id"], ai[0]["start"], ai[-1]["id"], ai[-1]["end"], len(ai)))
print()
print("ACT markers:", [(m["act"], m["start"], m["end"]) for m in tl["markers"] if m["type"] == "ACT"])
print()
# gap check: do items overlap / have holes?
prev = None
holes = 0
for i in items:
    if prev is not None and i["start"] - prev["end"] > 0.01:
        holes += 1
    prev = i
print("items monotonic:", all(items[i]["start"] <= items[i + 1]["start"] for i in range(len(items) - 1)))
print("gaps > 10ms between consecutive items:", holes)
print("last item end:", items[-1]["end"], " total:", tl["total"], " tail =", round(tl["total"] - items[-1]["end"], 3))
