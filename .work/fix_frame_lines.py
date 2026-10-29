#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cat vien/khung do model ve (duong net mong hoac mat trang quanh anh).

Khong phai moi "diem cuc bo toi" o canh deu la khung ve — canh trong nhien
(may, duong chan troi, bo toi) cung tao cuc bo toi. Khuong cach phan biet:
KHUNG VE co duong net song song o >= 2 canh voi KHOANG CACH CUNG NHAU.
Day la dieu kien bat buoc (1 cong nguoi ve khung -> ca 4 canh cung lech).

usage: py -3 .work/fix_frame_lines.py t3_apartos_house t3_textbooks ...
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
WIN = 40
MIN_DROP = 12          # duong net phai toi hon hang xung quan it nhat day
AGREE = 7              # cac canh phai lech nhau <= 7 px de coi la cung 1 khung
PAD = 2


def candidates(prof, content_ref):
    out = []
    for i in range(WIN):
        v = prof[i]
        lo, hi = max(0, i - 3), min(len(prof), i + 4)
        neigh = np.concatenate([prof[lo:i], prof[i + 1:hi]])
        if len(neigh) == 0:
            continue
        drop = float(neigh.mean()) - float(v)
        if drop >= MIN_DROP and abs(v - content_ref) > MIN_DROP:
            out.append((i, drop, float(v)))
    return out


def find_frame(a):
    h, w = a.shape
    rows, cols = a.mean(axis=1), a.mean(axis=0)
    cands = {
        "top": candidates(rows, float(rows[WIN:WIN + 50].mean())),
        "bottom": candidates(rows[::-1], float(rows[h - WIN - 50:h - WIN].mean())),
        "left": candidates(cols, float(cols[WIN:WIN + 50].mean())),
        "right": candidates(cols[::-1], float(cols[w - WIN - 50:w - WIN].mean())),
    }
    # lay ung vien "sau" (viet nhung noi dung ben trong) de tranh bien phai
    picks = {}
    for k, lst in cands.items():
        if lst:
            picks[k] = max(lst, key=lambda t: t[1])[0]
    if len(picks) < 2:
        return None, cands
    vals = list(picks.values())
    if max(vals) - min(vals) > AGREE:
        return None, cands
    return int(max(vals)) + PAD, cands


def fix(name):
    p = BG / f"{name}.png"
    im = Image.open(p).convert("RGB")
    a = np.asarray(im.convert("L"), np.float32)
    crop, cands = find_frame(a)
    if crop is None:
        det = "; ".join(f"{k}={v[0][0]}px" for k, v in cands.items() if v)
        print(f"{name}: KHONG phai khung ve ({det or 'khong co duong net'})")
        return False
    RAW.mkdir(parents=True, exist_ok=True)
    bak = RAW / f"{name}.framefix.png"
    if not bak.exists():
        shutil.copy2(p, bak)
    out = im.crop((crop, crop, im.width - crop, im.height - crop)).resize(SIZE, Image.LANCZOS)
    out.save(p)
    print(f"{name}: cat {crop} px o ca 4 canh -> resize {SIZE} (goc: {bak.name})")
    return True


def manual(name, n):
    """Cat thu cong n px o ca 4 canh (khi khung ve lech nhau, detector tu choi)."""
    p = BG / f"{name}.png"
    im = Image.open(p).convert("RGB")
    RAW.mkdir(parents=True, exist_ok=True)
    bak = RAW / f"{name}.framefix.png"
    if not bak.exists():
        shutil.copy2(p, bak)
    out = im.crop((n, n, im.width - n, im.height - n)).resize(SIZE, Image.LANCZOS)
    out.save(p)
    print(f"{name}: cat thu cong {n} px o ca 4 canh -> resize {SIZE} (goc: {bak.name})")
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--manual":
        # dung: --manual <ten_anh> <so_px>   (hoac --manual <so_px> <ten_anh>...)
        if len(args) >= 3 and args[1].startswith("t"):
            name, px = args[1], int(args[2])
            manual(name, px)
        else:
            px = int(args[1])
            for n in args[2:]:
                manual(n, px)
    else:
        for n in args:
            fix(n)
