# -*- coding: utf-8 -*-
"""Draft shot mapping and English text for Episode 06 EN from VN plan + EN script."""
import json
import re
from pathlib import Path

ROOT = Path(".")
plan_vn = (ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md").read_text(encoding="utf-8")
script_en = json.load(open(".work/script_tap06_EN.json", encoding="utf-8"))
tl_en = json.load(open(".work/timeline_s_EN_t06.json", encoding="utf-8"))

# Dictionary of sentences in EN script
S_EN = {}
ROLE_EN = {}
for e in script_en:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S_EN[s["id"]] = s["text"]
            ROLE_EN[s["id"]] = e.get("vai") or e.get("role")

# Extract all 73 shots from VN plan
lines = plan_vn.splitlines()
shots_vn = []
for l in lines:
    m = re.match(r"^\|\s*([1-5]-\d{2})\s*\|", l)
    if m:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        shots_vn.append({
            "id": m.group(1),
            "cau": c[1],
            "vai": c[2],
            "mau": c[3],
            "nen": c[4],
            "chu_vn": c[5],
            "beat_vn": c[6],
            "nv": c[7],
            "tr": c[8] if len(c) > 8 else ""
        })

print(f"Total VN shots: {len(shots_vn)}")

# Analyze sentence assignments
# We need to map 165 EN sentences into the 73 shots
# Let's inspect which shots need sentence range adjustments:
def parse_sents(cau_str):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cau_str):
        for k in range(int(a), int(b or a) + 1):
            out.append(f"{ma}#{k}")
    return out

# Check which sentences were in VN plan
all_vn_sents = []
for s in shots_vn:
    all_vn_sents.extend(parse_sents(s["cau"]))

print(f"Total sentences covered in VN plan: {len(all_vn_sents)}")
print(f"Total sentences in EN script: {len(S_EN)}")
