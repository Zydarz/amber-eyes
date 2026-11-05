#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draft shots table for Tap 04 JA from KeHoach_Video_Tap04_EN.md + script_tap04_JA.json."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

# 1. Read EN shots table
en_plan = (ROOT / "02_SAN_XUAT/Tap04_EN/KeHoach_Video_Tap04_EN.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(en_plan) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(en_plan) if i > i0 and l.startswith("**Tổng:"))

rows = []
for l in en_plan[i0:i1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    rows.append({
        "id": m.group(1), "cau": c[1], "vai": c[2], "mau": c[3],
        "nen": c[4], "chu_en": c[5], "beat_en": c[6], "nv": c[7], "tr": c[8] if len(c) > 8 else ""
    })

# 2. Read JA script
ja_script = json.loads((W / "script_tap04_JA.json").read_text(encoding="utf-8"))
S = {}
ROLE = {}
for e in ja_script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]
            ROLE[s["id"]] = e.get("role", "")

def sent_range(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

# Fix 4 shots to cover the 5 expanded JA sentences
for r in rows:
    if r["id"] == "2-19":
        r["cau"] = "`2.11#9`–`#11`"
    elif r["id"] == "3-02":
        r["cau"] = "`3.02#4`–`#7`"
    elif r["id"] == "4-14":
        r["cau"] = "`4.12#8`–`#12`"
    elif r["id"] == "5-03":
        r["cau"] = "`5.02#5`–`#7`"

draft = {}
missing = []
for r in rows:
    ids = sent_range(r["cau"])
    txt = [S.get(i, "<<THIEU>>") for i in ids]
    if any(t == "<<THIEU>>" for t in txt):
        missing.append((r["id"], ids))
    draft[r["id"]] = {
        "cau": r["cau"], "ids": ids, "vai": r["vai"], "mau": r["mau"], "nen": r["nen"],
        "nv": r["nv"], "tr": r["tr"],
        "chu_en": r["chu_en"], "beat_en": r["beat_en"],
        "ja_sentences": txt,
        "role_in_script": [ROLE.get(i, "?") for i in ids],
    }

(W / "_draft_shots_tap04_JA.json").write_text(
    json.dumps(draft, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"Total shots: {len(draft)} · missing JA sentences: {len(missing)}")
for sid, ids in missing:
    print("  MISSING:", sid, ids)

# Check total covered sentences
all_covered = [sid for r in draft.values() for sid in r["ids"]]
tl_ja = json.load(open(W / "timeline_s_JA_t04.json", encoding="utf-8"))["items"]
tl_ids = [it["id"] for it in tl_ja]
diff = set(tl_ids) - set(all_covered)
print(f"Timeline items: {len(tl_ids)} · Covered: {len(all_covered)} · Uncovered: {diff}")
