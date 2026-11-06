#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — do tuong phan CHU/CHU tren nen, tinh ca chu bi 'chim'.

Tinh bang cach:
  - lay dung vi tri net chu (alpha == 255) cua tung element chu
  - mau chu = mau pixel that su
  - nen tai do = bg_frame + lop phu cua renderer (DARK70 / GRAD)
  - do |lum_chu - lum_nen| va tuong phan WCAG
Nguyen tac: tuong phan < 1.6 (WCAG) hoac |dLum| < 45 => chu bi 'chim' -> can text_scrim.
"""
import json
import os
import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ.setdefault("AE_EP", "06")
os.environ.setdefault("AE_LANG", "vi")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
import build_video3 as B  # noqa: E402


def lum(rgb):
    a = np.asarray(rgb, dtype=np.float32)
    return 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]


def apply_overlay(bg, shot, els):
    """bg_frame + MOI lop phu toan khung ma renderer ve TRUOC chu
    (GRAD / DARK70 / soft_scrim) — dung thu tu trong els."""
    for el in els:
        if not hasattr(el, "img") or el.img is None:
            continue
        if el.img.width < 1900 or el.img.height < 1000:
            continue                                   # khong phai lop phu toan khung
        bg = Image.alpha_composite(bg, el.img)
    return bg


from PIL import Image  # noqa: E402

shots = json.loads((W / "shots_t06.json").read_text(encoding="utf-8"))["shots"]
rows = []
for sh in shots:
    if sh.get("hold") or sh.get("template") in (None, "T10"):
        continue
    try:
        els = B.build_elements(sh)
    except Exception as e:                                   # noqa: BLE001
        print(f"  ! {sh['id']} build_elements lỗi: {e}")
        continue
    t = sh["start"] + 0.6
    bg = apply_overlay(B.bg_frame(sh, t, 0).convert("RGBA"), sh, els)
    bga = np.asarray(bg.convert("RGB")).astype(np.float32)
    bgl = lum(bga)
    tot = bad = 0
    worst = 99.0
    for el in els:
        if not hasattr(el, "img") or el.img is None:
            continue
        if el.img.width >= 1900 or el.img.height >= 1000:
            continue                                            # lop phu toan khung
        arr = np.asarray(el.img)
        m = arr[:, :, 3] == 255
        if not m.any():
            continue
        ys, xs = np.nonzero(m)
        fx = np.clip(el.x + xs, 0, 1919)
        fy = np.clip(el.y + ys, 0, 1079)
        cols = Counter(map(tuple, arr[:, :, :3][m].tolist()))
        txt_rgb = np.array(cols.most_common(1)[0][0], dtype=np.float32)
        tl = float(lum(txt_rgb))
        bl = bgl[fy, fx]
        d = np.abs(tl - bl)
        ratio = (np.maximum(tl, bl) + 0.05) / (np.minimum(tl, bl) + 0.05)
        n_bad = int(((ratio < 1.6) | (d < 45)).sum())
        tot += len(fx)
        bad += n_bad
        worst = min(worst, float(np.percentile(ratio, 10)))
    if tot:
        pct = 100.0 * bad / tot
        rows.append((pct, worst, sh["id"], sh.get("template"), tot, bad))

rows.sort(reverse=True)
print(f"\n{len(rows)} shot co chu · nguong: can text_scrim neu >8% net chu bi chim\n")
for pct, worst, sid, tpl, tot, bad in rows:
    flag = "  <-- CAN SCRIM" if pct > 8 else ""
    print(f"  {sid:>5}  {tpl:<4} net={tot:<7} chim {bad:<6} ({pct:5.1f}%)  p10 tuong phan={worst:.2f}{flag}")
print("\nID can text_scrim (>8%):")
print(repr([r[2] for r in rows if r[0] > 8]))
