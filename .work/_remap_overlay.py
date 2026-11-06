#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đổi lại khoá của lớp phủ chữ khi skeleton đánh số lại ID shot.

Cặp theo (element, câu đầu, câu cuối) — dùng khi đánh số lại ID.
Dùng:  py -3 .work/_remap_overlay.py <skeleton_cu> <skeleton_moi> <overlay> [<overlay> ...]
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent

old_p, new_p = W / sys.argv[1], W / sys.argv[2]
old = json.loads(old_p.read_text(encoding="utf-8"))
new = json.loads(new_p.read_text(encoding="utf-8"))


def sig(r):
    if r["kind"] != "shot":
        return ("meta", r["cells"][1], r["cells"][3], r["cells"][4])
    eid, a, b = r["spans"][0]
    return ("shot", eid, a, b, r["cells"][3], r["cells"][4])


new_by_sig = {}
for r in new["rows"]:
    new_by_sig.setdefault(sig(r), []).append(r["sid"])

remap, used = {}, {}
for r in old["rows"]:
    s = sig(r)
    lst = new_by_sig.get(s, [])
    if not lst:
        print("  !! không khớp:", r["sid"], s)
        continue
    i = used.get(s, 0)
    if i < len(lst):
        remap[r["sid"]] = lst[i]
        used[s] = i + 1

for ov_name in sys.argv[3:]:
    p = W / ov_name
    ov = json.loads(p.read_text(encoding="utf-8"))
    out, changed = {}, 0
    for k, v in ov.items():
        if k.startswith("_"):
            out[k] = v
            continue
        nk = remap.get(k)
        if nk is None:
            print(f"  !! {p.name}: không map được {k}")
            continue
        out[nk] = v
        if nk != k:
            changed += 1
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  {p.name}: đổi {changed}/{len(ov) - 1} khoá")
