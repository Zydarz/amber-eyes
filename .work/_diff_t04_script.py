#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — phân tích chi tiết kịch bản MỚI so với bản CŨ (theo element).

In ra: mỗi element — số câu cũ / mới, câu nào giữ nguyên chữ, câu nào viết lại,
vai (role), loại element. Dùng để lập lại bảng shot.

Dùng:  py -3 .work/_diff_t04_script.py
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

OLD = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026_ban_goc.md"
NEW = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026.md"


def norm(s):
    return " ".join(s.replace("“", '"').replace("”", '"')
                    .replace("‘", "'").replace("’", "'").split())


def index(els):
    d = {}
    for el in els:
        if el["kind"] != "LOI":
            continue
        d[el["id"]] = {
            "role": el["role"],
            "dir": el.get("direction", ""),
            "sents": [(s["id"], s["text"]) for s in el.get("sentences", [])],
        }
    return d


old, new = index(parse_file(str(OLD))), index(parse_file(str(NEW)))
print(f"element LOI: cũ {len(old)} · mới {len(new)}")

tot_old = tot_new = 0
same = rewrite = 0
rows = []
for eid in sorted(new, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]))):
    n = new[eid]
    o = old.get(eid)
    tot_new += len(n["sents"])
    tot_old += len(o["sents"]) if o else 0
    if not o:
        rows.append((eid, "MỚI HOÀN TOÀN", 0, len(n["sents"]), n["role"], ""))
        continue
    os_ = [t for _, t in o["sents"]]
    ns_ = [t for _, t in n["sents"]]
    # so vị trí
    keep_idx, dif_idx = [], []
    for i, t in enumerate(ns_):
        if i < len(os_) and norm(os_[i]) == norm(t):
            keep_idx.append(i)
        else:
            dif_idx.append(i)
    same += len(keep_idx)
    rewrite += len(dif_idx)
    tag = "giữ" if not dif_idx and len(os_) == len(ns_) else ("VIẾT LẠI" if dif_idx else "THÊM")
    rows.append((eid, tag, len(os_), len(ns_), n["role"],
                 f"giữ#{[i + 1 for i in keep_idx]} viết#{[i + 1 for i in dif_idx]}"))

print(f"câu: cũ {tot_old} · mới {tot_new}")
print(f"câu giữ nguyên chữ (theo vị trí): {same} · câu viết lại/thêm: {rewrite}")
print()
for r in rows:
    print(f"  {r[0]:6s} {r[1]:14s} {r[2]:2d}->{r[3]:2d}  vai={r[4]}  {r[5]}")

# vai + hướng dẫn có đổi không
print("\n--- vai / hướng dẫn thay đổi ---")
for eid in sorted(new, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]))):
    if eid in old:
        if old[eid]["role"] != new[eid]["role"]:
            print(f"  ⚠ {eid}: vai {old[eid]['role']} -> {new[eid]['role']}")
        if old[eid]["dir"] != new[eid]["dir"]:
            print(f"  · {eid}: hướng dẫn đổi\n      cũ : {old[eid]['dir'][:100]}\n      mới: {new[eid]['dir'][:100]}")

# element không phải LOI (SFX/BGM/NGHI) — so trước sau
print("\n--- element phi-LOI ---")
for label, path in (("cũ", OLD), ("mới", NEW)):
    els = parse_file(str(path))
    kinds = {}
    for e in els:
        if e["kind"] != "LOI":
            kinds.setdefault(e["kind"], []).append((e["id"], e.get("sec", ""), (e.get("desc") or "")[:60]))
    print(f"  [{label}] " + " | ".join(f"{k}:{len(v)}" for k, v in kinds.items()))
    for k, v in kinds.items():
        print(f"      {k}: {v}")
