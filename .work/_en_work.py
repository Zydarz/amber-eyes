#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trích bảng shot VN + câu EN tương ứng ra file làm việc để dịch sang EN.

python .work/_en_work.py <act>     -> .work/_en_work_<act>.json
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

en = json.loads((W / "script_tap02_EN.json").read_text(encoding="utf-8"))
S = {}
for e in en:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

vn_plan = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_plan) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_plan) if i > i0 and l.startswith("**Tổng:"))


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


rows = []
act = None
for l in vn_plan[i0:i1]:
    m_act = re.match(r"### HỒI (\d)", l)
    if m_act:
        act = int(m_act.group(1))
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    sid = m.group(1)
    c = l.strip().strip("|").split("|")
    ids = sents(c[1])
    rows.append({
        "id": sid,
        "act": act,
        "sentences": ids,
        "vai": c[2].strip(),
        "mau": c[3].strip(),
        "nen": c[4].strip(),
        "chu_vn": c[5].strip(),
        "beat_vn": c[6].strip(),
        "nhan_vat": c[7].strip(),
        "chuyen": c[8].strip() if len(c) > 8 else "",
        "en_text": " ".join(S.get(x, "") for x in ids),
    })

out = W / f"_en_work_{sys.argv[1]}.json" if len(sys.argv) > 1 else W / "_en_work.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(rows)} shot -> {out.name}")
for a in (1, 2, 3, 4, 5):
    print(f"  hoi {a}: {sum(1 for r in rows if r['act'] == a)}")
