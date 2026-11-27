#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC ảnh nền Tập 31 + Tập 32 (đo tự động + dựng tờ soi mắt theo hồi).

Đo:
  - đủ số ảnh theo bg_jobs_tapXX.json, mở được, đúng 2112x1188, >100 KB
  - ảnh gần trùng nhau (hash perceptual rời) → cảnh báo lặp
  - ảnh quá tối / quá sáng / phẳng (std thấp) → cảnh báo
  - dải viền trắng đều (frame) → dùng lại logic qc_bg.py

Dựng tờ soi mắt: .work/qc_montage/sheet_tXX_actN.jpg  (4 cột, nhãn tên rõ)

Dùng: py -3 .work/_qc_t31_32.py 31 32
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
WORK = ROOT / ".work"
OUT = WORK / "qc_montage"
SIZE = (2112, 1188)


def dhash(path, size=16):
    with Image.open(path) as im:
        g = im.convert("L").resize((size + 1, size), Image.LANCZOS)
        a = np.asarray(g, np.float32)
    return (a[:, 1:] > a[:, :-1]).flatten()


def hamming(a, b):
    return int(np.count_nonzero(a != b))


def edge_flags(path):
    """Dải viền đều sáng + nhảy ngay biên (logic từ qc_bg.py)."""
    with Image.open(path) as im:
        a = np.asarray(im.convert("L"), np.float32)
    flags = []
    for key, axis, rev in (("top", 1, False), ("bottom", 1, True),
                           ("left", 0, False), ("right", 0, True)):
        prof = a.std(axis=axis)
        seq = prof[::-1] if rev else prof
        n = 0
        for v in seq:
            if v < 6.0:
                n += 1
            else:
                break
        if n < 12:
            continue
        means = a.mean(axis=1) if axis == 1 else a.mean(axis=0)
        mseq = means[::-1] if rev else means
        inside = float(mseq[:n].mean())
        win = mseq[n:n + 40]
        outside = float(win.mean()) if len(win) else inside
        if float(mseq[:n].std()) < 2.0 and abs(inside - outside) > 25.0:
            flags.append(f"{key}={n}px")
    return flags


def sheet(files, out_path, cols=4, cw=512):
    if not files:
        return None
    lab, pad = 30, 6
    ch = int(cw * 9 / 16)
    rows = (len(files) + cols - 1) // cols
    sh = Image.new("RGB", (cols * (cw + pad), rows * (ch + lab + pad)), (10, 10, 12))
    d = ImageDraw.Draw(sh)
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
    for i, p in enumerate(files):
        c, r = i % cols, i // cols
        with Image.open(p) as im:
            sh.paste(im.convert("RGB").resize((cw, ch), Image.LANCZOS), (c * (cw + pad), r * (ch + lab + pad)))
        d.text((c * (cw + pad) + 4, r * (ch + lab + pad) + ch + 4),
               p.stem, font=font, fill=(240, 240, 245))
    sh.save(out_path, quality=88)
    return out_path


def run(ep):
    jobs = json.loads((WORK / f"bg_jobs_tap{ep:02d}.json").read_text(encoding="utf-8"))
    names = [j["name"] for j in jobs]
    print(f"\n===== TAP {ep:02d} · {len(names)} job =====")

    missing, broken, wrong_size, small, dark, flat, framed = [], [], [], [], [], [], []
    hashes = {}
    for nm in names:
        p = BG / f"{nm}.png"
        if not p.exists():
            missing.append(nm)
            continue
        kb = p.stat().st_size // 1024
        if kb < 100:
            small.append(f"{nm} ({kb}KB)")
        try:
            with Image.open(p) as im:
                im.load()
                if im.size != SIZE:
                    wrong_size.append(f"{nm} {im.size}")
                g = np.asarray(im.convert("L"), np.float32)
        except Exception as e:
            broken.append(f"{nm}: {e}")
            continue
        if g.mean() < 12:
            dark.append(f"{nm} mean={g.mean():.1f}")
        if g.mean() > 235:
            dark.append(f"{nm} mean={g.mean():.1f} (qua sang)")
        if g.std() < 12:
            flat.append(f"{nm} std={g.std():.1f}")
        ef = edge_flags(p)
        if ef:
            framed.append(f"{nm}: {','.join(ef)}")
        h = dhash(p)
        hashes[nm] = h

    # gần trùng
    dup = []
    items = list(hashes.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            d = hamming(items[i][1], items[j][1])
            if d <= 12:
                dup.append((items[i][0], items[j][0], d))

    def rep(title, arr):
        print(f"  {title}: {len(arr)}")
        for x in arr[:12]:
            print("     -", x)

    rep("THIEU FILE", missing)
    rep("FILE HONG", broken)
    rep("SAI KICH THUOC", wrong_size)
    rep("NHO HON 100KB", small)
    rep("SANG/TOI", dark)
    rep("PHANG (std thap)", flat)
    rep("VIEN TRANG", framed)
    rep("GAN TRUNG (dhash)", [f"{a} ~ {b} (d={c})" for a, b, c in dup])
    print(f"  -> tong loi can xu ly: "
          f"{len(missing)+len(broken)+len(wrong_size)+len(small)+len(dark)+len(flat)+len(framed)+len(dup)}")

    # tờ soi mắt theo hồi
    OUT.mkdir(parents=True, exist_ok=True)
    acts = {}
    for j in jobs:
        acts.setdefault(j.get("act", 1), []).append(BG / f"{j['name']}.png")
    for act, files in sorted(acts.items()):
        files = [f for f in files if f.exists()]
        p = OUT / f"sheet_t{ep:02d}_act{act}.jpg"
        sheet(files, p)
        print(f"  sheet {p.name}: {len(files)} anh")
    return len(missing) + len(broken) + len(wrong_size)


def main():
    eps = [int(a) for a in sys.argv[1:]] or [31, 32]
    bad = 0
    for ep in eps:
        bad += run(ep)
    print(f"\nTONG loi chan (thieu/hong/sai kich thuoc): {bad}")


if __name__ == "__main__":
    main()
