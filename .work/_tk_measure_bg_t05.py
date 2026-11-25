# -*- coding: utf-8 -*-
"""Do vung chu + montage cho 32 nen doc 9:16 Tap 05 (assets/bg/tk05_*.png).

Do 3 chi so moi anh (giong bo tk01/tk02/tk03/tk04 da xuat ban):
  1. mean/max vung hook (y 270-730, x 120-780)  - chu hook lon nhat
  2. mean/max vung sub  (y 996-1254, x 120-780) - chu phu de
  3. vet ngang: dong nao co >70% pixel trong x 120-780 vuot nguong sang 120
Nguong: hook mean <= 58 · sub mean <= 72 · vet ngang = 0 dong.

Montage: 4 cột x 4 hàng / tờ, o 384 px (>=384 sau khi resize, canh dai <= ~1568)
=> soi mat 100% nen moi (H2/H19).
"""
import glob
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HOOK = (270, 730)
SUB = (996, 1254)
X0, X1 = 120, 780
THRESH = 120
PCT = 0.70
ROOT = r"D:/TEST/Gax/amber-eyes"
MONT_DIR = os.path.join(ROOT, ".work/qc_montage")


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
    files = sorted(glob.glob(os.path.join(ROOT, "assets/bg/tk05_*.png")))
    print("so anh nen:", len(files))
    print("%-38s %9s %8s %8s %8s %9s %6s" %
          ("file", "hook_mean", "hook_max", "sub_mean", "sub_max", "size", "ngang"))
    hm = hx = sm = sx = 0.0
    bad, fail, wrongsize = [], [], []
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
        if size != (1080, 1920):
            wrongsize.append((os.path.basename(p), size))
        thumbs.append((os.path.basename(p), rgb))
        print("%-38s %9.1f %8.1f %8.1f %8.1f %9s %6d" %
              (os.path.basename(p), b["hook"][0], b["hook"][1], b["sub"][0], b["sub"][1],
               "%dx%d" % size, st))
    n = max(1, len(files))
    print()
    print("TRUNG BINH hook mean %.1f · hook max %.1f · sub mean %.1f · sub max %.1f"
          % (hm / n, hx, sm / n, sx))
    print("anh co vet ngang: %d %s" % (len(bad), bad if bad else ""))
    print("anh vuot nguong vung chu: %d %s" % (len(fail), fail if fail else ""))
    print("anh sai kich thuoc: %d %s" % (len(wrongsize), wrongsize if wrongsize else ""))

    os.makedirs(MONT_DIR, exist_ok=True)
    try:
        font = ImageFont.truetype("arial.ttf", max(14, 384 // 14))
    except Exception:  # noqa: BLE001
        font = ImageFont.load_default()
    COLS, ROWS = 4, 4
    CW = 384
    CH = int(CW * 9 / 16)
    PAD, LAB = 4, 26
    per = COLS * ROWS
    for si in range(0, len(thumbs), per):
        chunk = thumbs[si:si + per]
        rows = (len(chunk) + COLS - 1) // COLS
        W = COLS * (CW + PAD)
        H = rows * (CH + LAB + PAD)
        sheet = Image.new("RGB", (W, H), (8, 8, 10))
        d = ImageDraw.Draw(sheet)
        for i, (name, rgb) in enumerate(chunk):
            c, r = i % COLS, i // COLS
            x, y = c * (CW + PAD), r * (CH + LAB + PAD)
            sheet.paste(rgb.resize((CW, CH), Image.Resampling.LANCZOS), (x, y))
            d.text((x + 3, y + CH + 4), name[5:-4][:30], font=font, fill=(232, 232, 238))
        out = os.path.join(MONT_DIR, "tk05_bg_sheet%d.jpg" % (si // per + 1))
        sheet.save(out, quality=90)
        print("  %s  %dx%d  %d anh" % (os.path.relpath(out, ROOT), W, H, len(chunk)))


if __name__ == "__main__":
    main()
