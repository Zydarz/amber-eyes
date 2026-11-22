# -*- coding: utf-8 -*-
"""Do vung chu cua 26 anh nen doc 9:16 Tap 02 (assets/bg/tk02_*.png).
Do 2 chi so:
  1. mean/max vung hook (y 270-730, x 120-780)  - chu hook lon nhat
  2. vet ngang: dong nao co >70% pixel trong x 120-780 vuot nguong sang
Ke tham chieu: bo tk01_xu ban (mean 41,6 - max 74,0) va bo tk02 truoc khi thay AI (mean 42,4 - max 56,9).
"""
import glob
import os

import numpy as np
from PIL import Image

HOOK = (270, 730)
SUB = (996, 1254)
X0, X1 = 120, 780
THRESH = 120          # nguong "sang" de lo vet ngang
PCT = 0.70            # 70% so pixel vuot nguong -> coi la vet ngang
ROOT = r"D:/TEST/Gax/amber-eyes"


def bands(gray):
    out = {}
    for name, (y0, y1) in (("hook", HOOK), ("sub", SUB)):
        reg = gray[y0:y1, X0:X1]
        out[name] = (float(reg.mean()), float(reg.max()))
    return out


def streaks(gray):
    total = 0
    for (y0, y1) in (HOOK, SUB):
        reg = gray[y0:y1, X0:X1]
        frac = (reg > THRESH).mean(axis=1)
        run, best = 0, 0
        for f in frac:
            if f > PCT:
                run += 1
                best = max(best, run)
            else:
                run = 0
        total += best
    return total


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "assets/bg/tk02_*.png")))
    print("so anh nen:", len(files))
    print("%-26s %9s %8s %8s %8s %9s %5s" % ("file", "hook_mean", "hook_max", "sub_mean", "sub_max", "size", "ngang"))
    hm = hx = sm = sx = 0.0
    bad = []
    for p in files:
        with Image.open(p) as im:
            size = im.size
            g = np.asarray(im.convert("L"), dtype=np.float32)
        b = bands(g)
        st = streaks(g)
        hm += b["hook"][0]; hx = max(hx, b["hook"][1])
        sm += b["sub"][0]; sx = max(sx, b["sub"][1])
        if st:
            bad.append((os.path.basename(p), st))
        print("%-26s %9.1f %8.1f %8.1f %8.1f %9s %5d"
              % (os.path.basename(p), b["hook"][0], b["hook"][1], b["sub"][0], b["sub"][1],
                 "%dx%d" % size, st))
    n = len(files)
    print()
    print("TRUNG BINH hook mean %.1f · hook max %.1f · sub mean %.1f · sub max %.1f"
          % (hm / n, hx, sm / n, sx))
    print("anh co vet ngang: %d" % len(bad), bad if bad else "")


if __name__ == "__main__":
    main()
