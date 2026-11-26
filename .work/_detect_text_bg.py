#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detector CHỮ trong ảnh nền bằng OpenCV (morphological gradient + connected components).

H26: khung hình KHÔNG CÓ CHỮ. Detector này chỉ là bộ lọc ưu tiên để soi mắt — không thay thế soi mắt.
Cách: nhị phân gradient -> connected components -> gom cụm theo khoảng cách -> chấm điểm cụm.
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
W = 1200


def score_text_regions(path):
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    h, w = img.shape
    scale = W / w
    small = cv2.resize(img, (W, int(h * scale)), interpolation=cv2.INTER_AREA)

    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    _, bw = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    bw = cv2.dilate(bw, np.ones((3, 3), np.uint8), iterations=1)

    n, lab, stats, cent = cv2.connectedComponentsWithStats(bw, 8)
    comps = []
    for i in range(1, n):
        x, y, cw, ch, area = stats[i]
        if not (6 <= ch <= 55 and 2 <= cw <= 90 and area >= 12):
            continue
        ar = cw / ch
        if not (0.12 <= ar <= 2.2):
            continue
        if cw * ch / area > 6.0:      # quá đặc -> không phải chữ
            continue
        comps.append((x, y, cw, ch))

    if not comps:
        return 0, []
    mask = np.zeros(bw.shape, np.uint8)
    for x, y, cw, ch in comps:
        mask[y:y + ch, x:x + cw] = 255
    mask = cv2.dilate(mask, np.ones((25, 25), np.uint8), iterations=1)
    n2, lab2, stats2, _ = cv2.connectedComponentsWithStats(mask, 8)
    clusters = []
    for i in range(1, n2):
        x, y, cw, ch, area = stats2[i]
        if area < 900:                # cụm nhỏ = chi tiết đồ vật
            continue
        sub = mask[y:y + ch, x:x + cw] > 0
        cnt = int(sub.sum() / 25)     # xấp xỉ số phần tử nguồn trong cụm
        clusters.append((cnt, (x, y, cw, ch)))
    clusters.sort(reverse=True)
    return len(clusters), clusters[:3]


def main():
    ep = sys.argv[1] if len(sys.argv) > 1 else "36"
    files = sorted(BG.glob(f"t{ep}_*.png"))
    res = []
    for f in files:
        n, top = score_text_regions(f)
        res.append((n, f.stem, top))
    res.sort(reverse=True, key=lambda r: r[0])
    print(f"{'cum':>4}  {'ten':<52} top")
    for n, name, top in res:
        if n:
            b = top[0][1]
            print(f"{n:>4}  {name:<52} x={b[0]} y={b[1]} w={b[2]} h={b[3]}")
    print(f"\nTong: {len(files)} anh · co cum >=1: {sum(1 for r in res if r[0])} · >=3 cum: {sum(1 for r in res if r[0] >= 3)}")
    (ROOT / ".work" / f"_text_detect_t{ep}.json").write_text(
        json.dumps([{"n": n, "name": name} for n, name, _ in res], ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
