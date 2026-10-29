import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(r"D:\TEST\Gax\Audi\.work")
sh = json.loads((W / "shots_EN_t02.json").read_text(encoding="utf-8"))
tl = json.loads((W / "timeline_s_EN_t02.json").read_text(encoding="utf-8"))
SENT = {i["id"]: i for i in tl["items"]}


def ctx_of(shot):
    parts = []
    for s in shot["sentences"]:
        it = SENT.get(s)
        if it:
            parts.append(it.get("display", ""))
    return " ".join(parts)


for sid in ("5-15", "5-16", "5-17", "5-18", "2-11"):
    s = next(x for x in sh["shots"] if x["id"] == sid)
    c = ctx_of(s)
    nums = sorted(set(re.findall(r"\d+", c)))
    print(f"--- {sid}  sá»‘ trong cÃ¢u: {nums}")
    print("    ctx:", c[:220])
    print("    on-screen:", " ".join(t for _k, t in s["on_screen"])[:220])

