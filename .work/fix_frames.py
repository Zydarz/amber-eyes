#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cat vien/frame them do model ve (khung trang hoac den deu), roi resize lai 2112x1188.

usage: py -3 .work/fix_frames.py t3_ravine [ten2 ...]
Anh goc duoc giu lai trong assets/bg/_raw/ voi hau to _framefix.
"""
import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
BG = ROOT / "assets" / "bg"
RAW = BG / "_raw"
SIZE = (2112, 1188)
STD_MAX, RUN_MAX, FLAT_MAX, JUMP = 6.0, 12, 2.0, 25.0
PAD = 3            # cat them 3 px cho an toan


def band(a, axis, reverse=False):
    prof = a.std(axis=axis)
    seq = prof[::-1] if reverse else prof
    n = 0
    for v in seq:
        if v < STD_MAX:
            n += 1
        else:
            break
    if n == 0:
        return 0, 0.0, 0.0, 0.0
    means = a.mean(axis=1) if axis == 1 else a.mean(axis=0)
    mseq = means[::-1] if reverse else means
    inside = float(mseq[:n].mean())
    # mau "noi dung" phai lay o xa bien vi: hang/cot ngay canh vien bi blend -> nhay bi ha
    win = mseq[n:n + 40]
    outside = float(win.mean()) if len(win) else inside
    return n, inside, outside, float(mseq[:n].std())


def fix(name):
    p = BG / f"{name}.png"
    im = Image.open(p).convert("RGB")
    a = np.asarray(im.convert("L"), np.float32)
    h, w = a.shape
    t, ti, to, tf = band(a, 1, False)
    b, bi, bo, bf = band(a, 1, True)
    l, li, lo, lf = band(a, 0, False)
    r, ri, ro, rf = band(a, 0, True)

    crop_t = crop_b = crop_l = crop_r = 0
    for tag, (n, inside, outside, flat) in (("top", (t, ti, to, tf)), ("bottom", (b, bi, bo, bf)),
                                             ("left", (l, li, lo, lf)), ("right", (r, ri, ro, rf))):
        jump = abs(inside - outside)
        print(f"   {tag:<7} n={n:<4} inside={inside:7.1f} outside={outside:7.1f} "
              f"jump={jump:7.1f} flat={flat:5.2f} "
              f"{'-> VIEN' if (n >= RUN_MAX and flat < FLAT_MAX and jump > JUMP) else ''}")
    if t >= RUN_MAX and tf < FLAT_MAX and abs(ti - to) > JUMP:
        crop_t = t + PAD
    if b >= RUN_MAX and bf < FLAT_MAX and abs(bi - bo) > JUMP:
        crop_b = b + PAD
    if l >= RUN_MAX and lf < FLAT_MAX and abs(li - lo) > JUMP:
        crop_l = l + PAD
    if r >= RUN_MAX and rf < FLAT_MAX and abs(ri - ro) > JUMP:
        crop_r = r + PAD

    if not (crop_t or crop_b or crop_l or crop_r):
        print(f"{name}: khong co vien can sua")
        return False

    RAW.mkdir(parents=True, exist_ok=True)
    bak = RAW / f"{name}.framefix.png"
    if not bak.exists():
        shutil.copy2(p, bak)

    box = (crop_l, crop_t, w - crop_r, h - crop_b)
    out = im.crop(box).resize(SIZE, Image.LANCZOS)
    out.save(p)
    print(f"{name}: cat top={crop_t} bottom={crop_b} left={crop_l} right={crop_r} "
          f"-> resize {SIZE} (goc: {bak.name})")
    return True


if __name__ == "__main__":
    for n in sys.argv[1:]:
        fix(n)
