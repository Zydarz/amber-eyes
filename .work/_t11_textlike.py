#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo 'text-like' trên 136 nền Tập 11 — bổ sung cho soi mắt (H20).

Cách đo: edge map -> connected components lọc kích thước ký tự -> gom các
thành phần có cùng dải y (overlap > 50%) thành HÀNG -> hàng có >= 3 thành phần
và tổng bề rộng >= 6% ảnh được coi là dấu hiệu chữ. Điểm = chuẩn hoá.

Không khẳng định vi phạm — chỉ là bảng xếp hạng để đối chiếu với mắt.
"""
import json
import pathlib
import sys

import cv2
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
OUT = ROOT / ".work" / "_t11" / "textlike.json"


def text_score(bgr):
    h, w = bgr.shape[:2]
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 60, 180)
    # nối ký tự thành blob mảnh
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 2))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, k, iterations=1)
    n, lab, stats, cent = cv2.connectedComponentsWithStats(closed, 8)
    comps = []
    for i in range(1, n):
        x, y, cw, ch, area = stats[i]
        if 5 <= ch <= 70 and 1 <= cw <= 260 and area >= 8:
            comps.append((x, y, cw, ch))
    if not comps:
        return 0.0, 0
    # gom thành hàng theo dải y
    comps.sort(key=lambda c: c[1])
    rows = []
    for c in comps:
        placed = False
        for r in rows:
            lo = min(v[1] for v in r)
            hi = max(v[1] + v[3] for v in r)
            ov = min(hi, c[1] + c[3]) - max(lo, c[1])
            if ov > 0.5 * min(c[3], hi - lo):
                r.append(c)
                placed = True
                break
        if not placed:
            rows.append([c])
    score = 0.0
    hits = 0
    for r in rows:
        if len(r) < 3:
            continue
        x0 = min(v[0] for v in r)
        x1 = max(v[0] + v[2] for v in r)
        if (x1 - x0) < 0.06 * w:
            continue
        hits += 1
        score += len(r) * min(1.0, (x1 - x0) / w)
    return round(score / 12.0, 2), hits


def main():
    rows = []
    for p in sorted(BG.glob("t11_*.png")):
        img = cv2.imread(str(p), cv2.IMREAD_COLOR)
        s, hits = text_score(img)
        rows.append({"name": p.stem, "score": s, "rows": hits})
    rows.sort(key=lambda r: -r["score"])
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} nen · ghi {OUT.relative_to(ROOT)}")
    for r in rows[:40]:
        print(f"  {r['score']:6.2f}  rows={r['rows']:3d}  {r['name']}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
