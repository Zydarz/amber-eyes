#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC bo nen 16:9 — kiem vien/frame thu, kich thuoc, va dung contact sheet.

usage:
  py -3 .work/qc_bg.py t3                 # quet tat ca assets/bg/t3_*.png
  py -3 .work/qc_bg.py t3 --sheet         # quet + dung contact sheet
  py -3 .work/qc_bg.py t3 --sheet --cols 5

PHAT HIEN VIEN (sua sau lan quet Tap03):
  - "dai deu" (std < 6 theo hang) KHONG du de ket luan co vien.
  - Vien that phai thoa 3 dieu kien cung luc:
      1) dai >= RUN_MAX px
      2) dai deu ve DO SANG (std cua cac do sang trong dai < 2.0)
      3) co "nhay" lien tut ngay tai bien (|do sang trong| - |do sang ngoai| > JUMP)
    -> phai co nhay de phan biet khung trang them (ravine) voi troi toi don (phone_booth).
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"D:\TEST\Gax\Audi")
BG = ROOT / "assets" / "bg"
STD_MAX = 6.0       # nguong "deu tuyet doi" theo chieu doc
RUN_MAX = 12        # do dai dai deu >= 12 px moi xet
FLAT_MAX = 2.0      # std do sang trong dai
JUMP = 25.0         # nhay lien tut tai bien
SIZE = (2112, 1188)


def _band(a, axis, reverse=False):
    """Tra (do dai dai deu, do sang trong dai, do sang ngoai dai) cho 1 canh."""
    prof = a.std(axis=axis)           # std theo chieu doc moi hang/cot
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
    # mau "noi dung" o xa bien: hang/cot ngay canh vien bi blend nen nhay bi ha
    win = mseq[n:n + 40]
    outside = float(win.mean()) if len(win) else inside
    flat = float(mseq[:n].std())
    return n, inside, outside, flat


def edges(a):
    out = {}
    for key, axis, rev in (("top", 1, False), ("bottom", 1, True),
                           ("left", 0, False), ("right", 0, True)):
        n, inside, outside, flat = _band(a, axis, rev)
        jump = abs(inside - outside)
        bad = (n >= RUN_MAX) and (flat < FLAT_MAX) and (jump > JUMP)
        out[key] = {"len": n, "inside": inside, "outside": outside,
                    "flat": flat, "jump": jump, "bad": bad}
    return out


def scan(pattern, verbose=True):
    files = sorted(BG.glob(f"{pattern}*.png"))
    if not files:
        print(f"khong tim thay anh {pattern}*.png")
        return []
    rows, problems = [], []
    for f in files:
        im = Image.open(f)
        a = np.asarray(im.convert("L"), np.float32)
        e = edges(a)
        bad = [k for k, v in e.items() if v["bad"]]
        note = []
        if im.size != SIZE:
            note.append(f"SAI KICH THUOC {im.size}")
        if bad:
            det = ", ".join(f"{k}={e[k]['len']}px(sang {e[k]['inside']:.0f}->{e[k]['outside']:.0f})" for k in bad)
            note.append(f"VIEN/FRAME {det}")
        if note:
            problems.append((f.name, "; ".join(note)))
        rows.append((f.name, im.size, e, note))
    if verbose:
        print(f"{'anh':<28}{'kich thuoc':<16}{'top/bot/left/right (px)':<26}trang thai")
        print("-" * 96)
        for name, size, e, note in rows:
            r = " / ".join(f"{e[k]['len']:>3}" for k in ("top", "bottom", "left", "right"))
            print(f"{name:<28}{str(size):<16}{r:<26}{'OK' if not note else ' | '.join(note)}")
        print("-" * 96)
        print(f"tong {len(rows)} anh · dat {len(rows)-len(problems)} · can sua {len(problems)}")
        for n, d in problems:
            print(f"  !! {n}: {d}")
    return rows, problems


def contact_sheet(pattern, cols=5, thumb_w=384):
    files = sorted(BG.glob(f"{pattern}*.png"))
    if not files:
        print("khong co anh de dung contact sheet")
        return None
    tw = thumb_w
    th = int(tw * 9 / 16)
    label_h = 30
    n = len(files)
    rows = (n + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * (th + label_h)), (14, 14, 16))
    d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 17)
    except Exception:
        font = ImageFont.load_default()
    for i, f in enumerate(files):
        r, c = divmod(i, cols)
        x, y = c * tw, r * (th + label_h)
        with Image.open(f) as im:
            sheet.paste(im.convert("RGB").resize((tw, th), Image.LANCZOS), (x, y))
        d.text((x + 7, y + th + 6), f.stem, fill=(215, 215, 220), font=font)
    ep_map = {f"t{i}": f"Tap{i:02d}" for i in range(2, 30)}
    folder = ep_map.get(pattern, f"Tap{int(pattern.replace('t', '')):02d}" if pattern.replace('t', '').isdigit() else "Tap03")
    out = ROOT / "02_SAN_XUAT" / folder
    out.mkdir(parents=True, exist_ok=True)
    dst = out / f"contact_sheet_{pattern}.png"
    sheet.save(dst)
    print(f"contact sheet: {dst}  ({sheet.size[0]}x{sheet.size[1]}, {n} anh)")
    return dst


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pattern = args[0] if args else "t3"
    scan(pattern)
    if "--sheet" in sys.argv:
        cols = 5
        if "--cols" in sys.argv:
            cols = int(sys.argv[sys.argv.index("--cols") + 1])
        contact_sheet(pattern, cols)


if __name__ == "__main__":
    main()
