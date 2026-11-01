#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do TUONG PHAN chu tren nen trong 83 anh tinh T04 (H9) — theo TUNG KHOI CHU.

Khong doan bang mat thuong:
  1. pixel chu = mau chinh xac C["text"]=(242,239,233) (Pillow ve sau nen,
     nen khong doi mau) -> chi lay mau nay, bo mau "muted" (trung nen).
  2. noi cac net thanh khoi chu (binary_closing) -> label -> tung khoi.
  3. nen quanh khoi = median lum cua pixel nen trong bbox + 12 px.
  4. tuong phan WCAG voi chu lon: (239.2+.05)/(median_nen+.05); can >= 3.0
  5. KET LUAN: khoi nao tuong phan < 3.0 => chu chim tren nen sang.
Xuat: .work/_cu/stills_check/contrast_t04.csv
"""
import csv
import pathlib
import sys

import numpy as np
from PIL import Image
from scipy.ndimage import binary_closing, binary_dilation, label

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
SD = ROOT / ".work" / "video3_t04" / "stills"
OUTD = ROOT / ".work" / "_cu" / "stills_check"
OUTD.mkdir(parents=True, exist_ok=True)
TEXT = np.array([242, 239, 233])
L_TEXT = 0.2126 * 242 + 0.7152 * 239 + 0.0722 * 233


def analyze(p):
    a = np.asarray(Image.open(p).convert("RGB")).astype(int)
    ui = np.abs(a - TEXT).max(axis=2) <= 2
    if ui.sum() < 120:
        return None
    L = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    closed = binary_closing(ui, structure=np.ones((13, 13), bool))
    lab, n = label(closed)
    ui_dil = binary_dilation(ui, structure=np.ones((3, 3), bool), iterations=6)
    blocks = []
    for i in range(1, n + 1):
        m = lab == i
        cnt = int((m & ui).sum())
        if cnt < 120:
            continue
        ys, xs = np.where(m)
        y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
        py0, py1 = max(0, y0 - 12), min(L.shape[0], y1 + 13)
        px0, px1 = max(0, x0 - 12), min(L.shape[1], x1 + 13)
        win = L[py0:py1, px0:px1]
        winbg = ~ui_dil[py0:py1, px0:px1]
        if winbg.sum() < 60:
            continue
        bg_med = float(np.median(win[winbg]))
        bg_p90 = float(np.percentile(win[winbg], 90))
        ratio_med = (L_TEXT + 0.05) / (bg_med + 0.05)
        ratio_p90 = (L_TEXT + 0.05) / (bg_p90 + 0.05)
        blocks.append(dict(x=int(x0), y=int(y0), w=int(x1 - x0), h=int(y1 - y0),
                           px=cnt, bg_med=round(bg_med, 1), bg_p90=round(bg_p90, 1),
                           r_med=round(ratio_med, 2), r_p90=round(ratio_p90, 2)))
    if not blocks:
        return None
    blocks.sort(key=lambda b: b["r_med"])
    worst = blocks[0]
    nbad = sum(1 for b in blocks if b["r_med"] < 3.0)
    return dict(shot=p.stem.replace("shot_", ""), n_blocks=len(blocks), n_bad=nbad,
                worst_r=worst["r_med"], worst_bg=worst["bg_med"],
                worst_x=worst["x"], worst_y=worst["y"], worst_w=worst["w"])


rows = []
for p in sorted(SD.glob("shot_*.png")):
    r = analyze(p)
    if r:
        rows.append(r)
rows.sort(key=lambda r: (r["n_bad"] > 0, r["worst_r"]))
with (OUTD / "contrast_t04.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

print("%-7s %7s %6s %8s %8s  %s" % ("shot", "blocks", "bad", "min_r", "bg_med", "vung_cham"))
for r in rows:
    if r["n_bad"]:
        print("%-7s %7d %6d %8.2f %8.1f  x=%d y=%d w=%d"
              % (r["shot"], r["n_blocks"], r["n_bad"], r["worst_r"], r["worst_bg"],
                 r["worst_x"], r["worst_y"], r["worst_w"]))
print("\nTong so shot co khoi 'chim':", sum(1 for r in rows if r["n_bad"]),
      "/", len(rows))
print("->", OUTD / "contrast_t04.csv")
