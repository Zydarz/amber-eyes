#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng skeleton: mỗi shot mới -> {vn, beat, nph, phrases_vn, old_ja}."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(__file__).resolve().parent
ROOT = W.parent

ref = (W / "_ovl_ref_JA.md").read_text(encoding="utf-8").splitlines()
vnlines = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vnlines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vnlines) if i > i0 and l.startswith("**Tổng:"))

old = json.loads((W / "_cu/shots_text_tap02_JA_pre_20261105.json").read_text(encoding="utf-8"))

VN = {}
for l in vnlines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    c = l.strip().strip("|").split("|")
    VN[m.group(1)] = {"cell": c[1].strip(), "chu": c[5].strip(), "beat": c[6].strip(),
                      "phrases_vn": re.findall(r'ở "([^"]+)"', c[6])}

# ---- ref: old_ja theo shot id moi
skel = {}
cur = None
for l in ref:
    m = re.match(r"^## ([1-5]-\d+)\s", l)
    if m:
        cur = m.group(1)
        skel[cur] = {"old_ja": None, "old_id": None}
        continue
    if cur is None:
        continue
    m = re.match(r"^- CHỮ JA CŨ \[([^\]]+)\]:\s*(.*)$", l)
    if m and skel[cur]["old_ja"] is None:
        oid = m.group(1)
        txt = m.group(2).strip()
        if oid == "None":
            skel[cur]["old_id"] = None
            skel[cur]["old_ja"] = ""
        else:
            skel[cur]["old_id"] = oid
            skel[cur]["old_ja"] = old.get(oid, [txt])[0] if oid in old else txt

out = {}
for sid, v in VN.items():
    s = skel.get(sid, {})
    out[sid] = {"cell": v["cell"], "vn": v["chu"], "beat": v["beat"],
                "nph": len(v["phrases_vn"]), "phrases_vn": v["phrases_vn"],
                "old_id": s.get("old_id"), "old_ja": s.get("old_ja")}

(W / "_ovl_skeleton.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("shots:", len(out))
mismatch = [s for s in out if out[s]["old_ja"] is None]
print("thieu old_ja:", len(mismatch), mismatch[:10])
