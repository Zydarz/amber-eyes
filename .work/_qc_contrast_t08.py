#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC độ tương phản chữ trên ảnh tĩnh Tập 08 (H9).

Cách đo: với mỗi ảnh, tìm nét chữ (pixel gần màu vai của shot) trong dải chữ,
lấy trung vị nền quanh đó (loại bỏ nét chữ) rồi tính tỉ lệ tương phản WCAG.
Ngưỡng: ratio < 1.6 hoặc |Δlum| < 45  => chữ "chìm" trên nền sáng => cần text_scrim.
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")

ROLE_COLOR = {"H": (226, 180, 103), "D": (134, 169, 204), "C": (169, 155, 214),
              "N1": (217, 185, 155), "N2": (110, 140, 160)}
PALETTE = [(226, 180, 103), (242, 239, 233), (156, 152, 143), (134, 169, 204),
           (169, 155, 214), (217, 185, 155), (110, 140, 160), (232, 160, 191)]


def lum(c):
    def f(v):
        v = v / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(x) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def scan(folder, shots_file):
    SH = json.loads(Path(shots_file).read_text(encoding="utf-8"))["shots"]
    role_of = {s["id"]: (s.get("role") or "H") for s in SH}
    bad, notes = [], []
    for f in sorted(Path(folder).glob("shot_*.png")):
        sid = f.stem.replace("shot_", "")
        im = np.asarray(Image.open(f).convert("RGB"), dtype=np.float32)
        band = im[700:1010, :, :]                       # dai chu T1
        tc = np.array(ROLE_COLOR[role_of.get(sid, "H")], dtype=np.float32)
        d = np.sqrt(((band - tc) ** 2).sum(axis=2))
        mask = d < 60
        if mask.sum() < 60:                            # it chu -> dung mau chung
            m2 = np.zeros(band.shape[:2], bool)
            for p in PALETTE:
                d2 = np.sqrt(((band - np.array(p, dtype=np.float32)) ** 2).sum(axis=2))
                m2 |= d2 < 45
            mask = m2
        if mask.sum() < 60:
            continue
        bg = band[~mask]
        if bg.size == 0:
            continue
        med = np.median(bg.reshape(-1, 3), axis=0)
        bgc = tuple(int(x) for x in med)
        tc2 = tuple(int(x) for x in tc)
        r = ratio(tc2, bgc)
        dl = abs(lum(tc2) - lum(bgc))
        if r < 1.6 or dl < 0.045:
            bad.append(f"{sid}: ratio {r:.2f} · Δlum {dl*1000:.0f} · chữ {tc2} · nền {bgc}")
        elif r < 3.0:
            notes.append(f"{sid}: ratio {r:.2f} (chữ nhạt)")
    return bad, notes


if __name__ == "__main__":
    for lang, suf in (("vi", "_t08"), ("en", "_EN_t08"), ("ja", "_JA_t08")):
        folder = ROOT / f".work/video3{suf}/stills"
        shots = ROOT / f".work/shots{suf}.json"
        bad, notes = scan(folder, shots)
        print(f"== {lang}: {len(bad)} anh co chu chim · {len(notes)} anh chu nhat")
        for b in bad:
            print("   [LOI]", b)
        for n in notes[:6]:
            print("   [GHI ]", n)
