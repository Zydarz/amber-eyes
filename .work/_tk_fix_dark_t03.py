# -*- coding: utf-8 -*-
"""Toi them vung chu cho 1 anh nen doc cu the (khi do luminance vua cham nguong).

usage: py -3 .work/_tk_fix_dark_t03.py tk03_mother_shadow [ten2 ...]
"""
import os
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_fallback_crop_t03 import _band_profile, HOOK_BAND, SUB_BAND, SX0, SX1  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
DST = os.path.join(ROOT, "assets/bg")


def measure(gray):
    hook = float(gray[HOOK_BAND[0]:HOOK_BAND[1], SX0:SX1].mean())
    sub = float(gray[SUB_BAND[0]:SUB_BAND[1], SX0:SX1].mean())
    return hook, sub


def main():
    for name in sys.argv[1:]:
        p = os.path.join(DST, name + ".png")
        im = Image.open(p).convert("RGB")
        arr = np.array(im, dtype=np.float32)
        h = arr.shape[0]
        for extra in (0.05, 0.10, 0.15, 0.20, 0.25):
            prof = _band_profile(h, extra)
            out = np.clip(arr * prof[:, None, None], 0, 255).astype(np.uint8)
            g = np.asarray(Image.fromarray(out).convert("L"), dtype=np.float32)
            hook, sub = measure(g)
            if hook <= 56.0 and sub <= 70.0:
                Image.fromarray(out).save(p, "PNG", optimize=True)
                print("%-26s depth=%.2f hook=%.1f sub=%.1f" % (name, extra, hook, sub))
                break
        else:
            print("%-26s KHONG dua duoc xuong nguong (hook=%.1f sub=%.1f)" % (name, hook, sub))


if __name__ == "__main__":
    main()
