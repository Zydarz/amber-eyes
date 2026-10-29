import json
from pathlib import Path

W = Path(r"D:\TEST\Gax\Audi\.work")
sheet = json.load(open(W / "sfx_tap02.json", encoding="utf-8"))
script = json.load(open(W / "script_tap02.json", encoding="utf-8"))
sids = {s["id"] for e in script if e["kind"] == "LOI" for s in e["sentences"]}
eids = {e["id"] for e in script}

print("Music drops:", sheet.get("music_drop"))

missing_amb = []
for a in sheet.get("ambience", []):
    s, e = a[0], a[1]
    if s not in sids and s not in eids:
        missing_amb.append((s, a))
    if e not in sids and e not in eids:
        missing_amb.append((e, a))

print(f"Missing ambience endpoints: {len(missing_amb)}")
for m in missing_amb:
    print("  ", m)

missing_cues = []
for c in sheet.get("cues", []):
    anchor = c[0]
    if anchor not in sids and anchor not in eids:
        missing_cues.append((anchor, c))

print(f"Missing cues anchors: {len(missing_cues)}")
for m in missing_cues:
    print("  ", m)
