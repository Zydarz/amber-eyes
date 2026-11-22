# -*- coding: utf-8 -*-
"""Sua nen doc 9:16 cho 1 anh co vien san (parchment) trong anh nguon 16:9.

T4_somerset_courtroom.jpg con vien gia co mau kem o tren + duoi => vi pham
V7 (anh tran vien, khong vien/letterbox). Script nay cat vien kem ra tu anh goc,
roi lam lai chuoi crop 9:16 + nen toi vung chu.

usage: py -3 .work/_tk_fix_border_t04.py tk04_somerset_courtroom
"""
import os
import shutil
import sys
import time

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_fallback_crop_t04 import (  # noqa: E402
    best_window, content_box, safe_text_zone, darken_text_bands,
)
from _tk_src_t04 import PAIRS  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
RAW = os.path.join(ROOT, "assets/bg/_raw")
DST = os.path.join(ROOT, "assets/bg")
BAK = os.path.join(ROOT, ".work/_cu", "tk04_fixborder_%s" % time.strftime("%Y%m%d_%H%M"))
W, H = 1080, 1920


def trim_light_border(gray, thresh=150):
    """Cat cac hang sáng (vien kem) o tren + duoi, tra (top, bottom)."""
    h = gray.shape[0]
    top = 0
    while top < h - 50 and gray[top:min(top + 6, h)].mean() > thresh:
        top += 1
    bot = h
    while bot > top + 50 and gray[max(0, bot - 6):bot].mean() > thresh:
        bot -= 1
    # bo them hang den ngay sau vien (vien den) de khong keo theo
    while top < bot - 50 and gray[top].mean() < 60:
        top += 1
    while bot > top + 50 and gray[bot - 1].mean() < 60:
        bot -= 1
    return top, bot


def main():
    os.makedirs(BAK, exist_ok=True)
    ref_of = {n: r for n, r in PAIRS}
    for name in sys.argv[1:]:
        ref = ref_of.get(name)
        if not ref:
            print("KHONG biet nguon cho %s" % name)
            continue
        src = os.path.join(RAW, ref)
        dst = os.path.join(DST, name + ".png")
        if not os.path.exists(src):
            print("THIEU NGUON %s" % ref)
            continue
        shutil.copy2(dst, os.path.join(BAK, name + ".png"))

        with Image.open(src) as im:
            im = im.convert("RGB")
            gray = np.array(im.convert("L"))
            t0, b0 = trim_light_border(gray)
            print("%s <- %s : vien kem cat o hang %d..%d (anh goc %dx%d)"
                  % (name, ref, t0, b0, im.size[0], im.size[1]))
            im2 = im.crop((0, t0, im.size[0], b0))
            gray2 = np.array(im2.convert("L"))
            t, b, l, r = content_box(gray2)
            wl, wr = best_window(gray2, (t, b, l, r))
            ct, cb = max(0, t), min(gray2.shape[0], b)
            sub = im2.crop((wl, ct, wr, cb))
            sw, sh = sub.size
            if sw * 16 // 9 < sh:
                sh2 = sw * 16 // 9
                sub = sub.crop((0, (sh - sh2) // 2, sw, (sh - sh2) // 2 + sh2))
            else:
                sw2 = sh * 9 // 16
                sub = sub.crop(((sw - sw2) // 2, 0, (sw - sw2) // 2 + sw2, sh))
            out = sub.resize((W, H), Image.Resampling.LANCZOS)
            out = safe_text_zone(out)
            out, depth, hook, sub_m = darken_text_bands(out)
            out.save(dst, "PNG", optimize=True)
        print("   -> %s  depth=%.2f hook=%.1f sub=%.1f" % (dst, depth, hook, sub_m))
    print("backup: %s" % BAK)


if __name__ == "__main__":
    main()
