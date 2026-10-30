import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
script = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8"))
tl = json.loads((ROOT / ".work" / "timeline_s_t04.json").read_text(encoding="utf-8"))

sents = {}
for e in script:
    if e["kind"] == "LOI":
        r = e["role"]
        if e["id"] == "1.07": r = "N1"
        elif e["id"] == "4.06": r = "N2"
        for s in e["sentences"]:
            sents[s["id"]] = {"role": r, "text": s["text"], "elem": e["id"]}

# In các câu của từng cụm để đối chiếu khi viết bảng shot
print("Loaded script sentences:", len(sents))
