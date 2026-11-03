#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh bản nháp cho bảng shot JA Tập 03: mỗi shot kèm câu JA + chữ VN + beat VN.

Output: .work/_draft_shots_tap03_JA.json  (dùng để viết shots_text_tap03_JA.json)
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

# ---------- 1. đọc bảng shot VN ----------
plan = (ROOT / "02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(plan) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(plan) if i > i0 and l.startswith("**Tổng:"))
rows = []
for l in plan[i0:i1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    rows.append({"id": m.group(1), "cau": c[1], "vai": c[2], "mau": c[3],
                 "nen": c[4], "chu_vn": c[5], "beat_vn": c[6], "nv": c[7], "tr": c[8] if len(c) > 8 else ""})

# ---------- 2. đọc kịch bản JA ----------
script = json.loads((W / "script_tap03_JA.json").read_text(encoding="utf-8"))
S = {}
ROLE = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]
            ROLE[s["id"]] = e.get("role", "")

# ---------- 3. ghép ----------
def sent_range(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

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
        "chu_vn": r["chu_vn"], "beat_vn": r["beat_vn"],
        "ja_sentences": txt,
        "role_in_script": [ROLE.get(i, "?") for i in ids],
    }

(W / "_draft_shots_tap03_JA.json").write_text(
    json.dumps(draft, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"shot: {len(draft)} · thieu cau JA: {len(missing)}")
for sid, ids in missing[:20]:
    print("  THIEU", sid, ids)

# in ra de soi nhanh
print("\n=== SOI NHANH ===")
for sid in list(draft)[:6]:
    d = draft[sid]
    print(f"\n[{sid}] vai={d['vai']} mau={d['mau']} nen={d['nen']} nv={d['nv']}")
    print("  chu_vn :", d["chu_vn"][:150])
    print("  beat_vn:", d["beat_vn"][:90])
    for i, t in zip(d["ids"], d["ja_sentences"]):
        print(f"   {i}: {t[:110]}")
