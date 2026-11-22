# -*- coding: utf-8 -*-
"""Do vung chu + contact sheet cho 23 nen doc 9:16 Tap 04 (assets/bg/tk04_*.png).

Do 3 chi so moi anh (giong bo tk01/tk02/tk03 da xuat ban):
  1. mean/max vung hook (y 270-730, x 120-780)  - chu hook lon nhat
  2. mean/max vung sub  (y 996-1254, x 120-780) - chu phu de
  3. vet ngang: dong nao co >70% pixel trong x 120-780 vuot nguong sang 120
Nguong: hook mean <= 58 · sub mean <= 72 · vet ngang = 0 dong.
"""
import glob
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HOOK = (270, 730)
SUB = (996, 1254)
X0, X1 = 120, 780
THRESH = 120
PCT = 0.70
ROOT = r"D:/TEST/Gax/amber-eyes"
MONT = os.path.join(ROOT, ".work/_tk04_montage.png")


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
        run = best = 0
        for f in frac:
            if f > PCT:
                run += 1
                best = max(best, run)
            else:
                run = 0
        total += best
    return total


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "assets/bg/tk04_*.png")))
    print("so anh nen:", len(files))
    print("%-30s %9s %8s %8s %8s %9s %6s" %
          ("file", "hook_mean", "hook_max", "sub_mean", "sub_max", "size", "ngang"))
    hm = hx = sm = sx = 0.0
    bad, fail = [], []
    thumbs = []
    for p in files:
        with Image.open(p) as im:
            size = im.size
            g = np.asarray(im.convert("L"), dtype=np.float32)
            rgb = im.convert("RGB")
        b = bands(g)
        st = streaks(g)
        hm += b["hook"][0]; hx = max(hx, b["hook"][1])
        sm += b["sub"][0]; sx = max(sx, b["sub"][1])
        if st:
            bad.append((os.path.basename(p), st))
        if b["hook"][0] > 58 or b["sub"][0] > 72:
            fail.append((os.path.basename(p), round(b["hook"][0], 1), round(b["sub"][0], 1)))
        thumbs.append((os.path.basename(p), rgb))
        print("%-30s %9.1f %8.1f %8.1f %8.1f %9s %6d"
              % (os.path.basename(p), b["hook"][0], b["hook"][1], b["sub"][0], b["sub"][1],
                 "%dx%d" % size, st))
    n = max(1, len(files))
    print()
    print("TRUNG BINH hook mean %.1f · hook max %.1f · sub mean %.1f · sub max %.1f"
          % (hm / n, hx, sm / n, sx))
    print("anh co vet ngang: %d" % len(bad), bad if bad else "")
    print("anh vuot nguong vung chu: %d" % len(fail), fail if fail else "")

    # contact sheet 9:16
    COLS = 8
    TW, TH = 216, 384
    PAD, LAB = 8, 18
    rows = (len(thumbs) + COLS - 1) // COLS
    W = COLS * (TW + PAD) + PAD
    H = rows * (TH + PAD + LAB) + PAD
    sheet = Image.new("RGB", (W, H), (14, 14, 16))
    d = ImageDraw.Draw(sheet)
    for i, (name, rgb) in enumerate(thumbs):
        r, c = divmod(i, COLS)
        x = PAD + c * (TW + PAD)
        y = PAD + r * (TH + PAD + LAB)
        sheet.paste(rgb.resize((TW, TH), Image.Resampling.LANCZOS), (x, y))
        d.text((x + 2, y + TH + 3), name[6:-4][:26], fill=(205, 205, 205))
    sheet.save(MONT, "PNG", optimize=True)
    print("\ncontact sheet: %s (%d anh, %dx%d, %.2f MB)"
          % (MONT, len(thumbs), W, H, os.path.getsize(MONT) / 1048576))


if __name__ == "__main__":
    main()
