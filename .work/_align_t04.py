#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — căn chỉnh câu cũ ↔ câu mới bằng Needleman-Wunsch (đơn điệu, mờ).

Bỏ bước "dựng bảng", chỉ xuất BẢN ĐỒ căn chỉnh + báo cáo độ phủ, để ta kiểm
tra trước khi sinh bảng shot mới.

Dùng:  py -3 .work/_align_t04.py
"""
import difflib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

OLD_KB = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026_ban_goc.md"
NEW_KB = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026.md"
W = ROOT / ".work"


def index(els):
    d = {}
    for el in els:
        if el["kind"] == "LOI":
            d[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]
    return d


old_idx = index(parse_file(str(OLD_KB)))
new_idx = index(parse_file(str(NEW_KB)))


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"')
    return " ".join(re.sub(r"[^\w\s]", " ", s).split())


def nw_align(old_s, new_s, gap=0.0, thresh=0.30):
    """Căn chỉnh đơn điệu tối ưu tổng similarity. Trả về list (oi, nj) và các câu mới không khớp."""
    n, m = len(old_s), len(new_s)
    on = [norm(t) for _, t in old_s]
    nn = [norm(t) for _, t in new_s]
    sm = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        sm[i][0] = i * gap
    for j in range(m + 1):
        sm[0][j] = j * gap
    ptr = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            r = difflib.SequenceMatcher(None, on[i - 1], nn[j - 1], autojunk=False).ratio()
            best = sm[i - 1][j - 1] + r
            k = "D"
            if sm[i - 1][j] + gap > best:
                best, k = sm[i - 1][j] + gap, "U"
            if sm[i][j - 1] + gap > best:
                best, k = sm[i][j - 1] + gap, "L"
            sm[i][j], ptr[i][j] = best, k
    pairs, i, j = [], n, m
    while i > 0 or j > 0:
        k = ptr[i][j]
        if k == "D":
            pairs.append((i - 1, j - 1))
            i, j = i - 1, j - 1
        elif k == "U":
            i -= 1
        else:
            j -= 1
    pairs.reverse()
    keep = [(i, j) for i, j in pairs
            if difflib.SequenceMatcher(None, on[i], nn[j], autojunk=False).ratio() >= thresh]
    used_new = {j for _, j in keep}
    orphan_new = [j for j in range(m) if j not in used_new]
    orphan_old = [i for i in range(n) if i not in {i for i, _ in keep}]
    return keep, orphan_new, orphan_old


align_map = {}
tot_old = tot_new = 0
aligned = 0
lines = []
for eid in sorted(old_idx, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]))):
    o, n = old_idx[eid], new_idx.get(eid, [])
    if not n:
        continue
    tot_old += len(o)
    tot_new += len(n)
    keep, onw, oow = nw_align(o, n)
    for oi, nj in keep:
        align_map[f"{eid}#{oi + 1}"] = f"{eid}#{nj + 1}"
    aligned += len(keep)
    lines.append(f"=== {eid}  cũ {len(o)} → mới {len(n)}  | khớp {len(keep)} | mới-mồ côi {onw} | cũ-mồ côi {oow}")
    for oi, nj in keep:
        r = difflib.SequenceMatcher(None, norm(o[oi][1]), norm(n[nj][1]), autojunk=False).ratio()
        lines.append(f"   {o[oi][0]} -> {n[nj][0]}  sim={r:.2f}")
        lines.append(f"      cũ : {o[oi][1][:150]}")
        lines.append(f"      mới: {n[nj][1][:150]}")
    for j in onw:
        lines.append(f"   [MỚI, chưa có dòng] {n[j][0]}: {n[j][1][:160]}")

print(f"câu cũ {tot_old} · câu mới {tot_new} · căn chỉnh được {aligned} "
      f"→ phủ {aligned}/{tot_new} câu mới")
all_new = [f"{eid}#{i + 1}" for eid, v in new_idx.items() for i in range(len(v))]
uncovered = [x for x in all_new if x not in set(align_map.values())]
print(f"câu mới chưa khớp câu cũ nào: {len(uncovered)}")
print("   " + ", ".join(uncovered))
json.dump(align_map, open(W / "_t04_align.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
open(W / "_t04_align_report.txt", "w", encoding="utf-8", newline="\n").write("\n".join(lines))
