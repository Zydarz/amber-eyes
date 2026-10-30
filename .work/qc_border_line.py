#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Doi vien mong (1 dong net) — lo loi ma quet 'dai deu' bo sot.

Dai deu (std < 6) khong bat duoc duong 1-3 px ve mong. Day la detector theo
khu vuc: trong 40 px dau moi canh, tim hang/cot nao la "diem cuc bo toi" hon
hang/cot lien ke, va toi do hon bang nhieu so voi noi dung ben trong.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
BG = Path(__file__).resolve().parents[1] / "assets" / "bg"
WIN = 40          # khu vuc canh
MIN_DROP = 12     # toi thieu phai toi hon mot chuc so voi noi dung
MAX_LINE = 4      # do day toi toi da chap nhan (px)


def line_scan(prof, content_ref):
    """prof: mean brightness theo hang/cot. content_ref: gia tri noi dung ben trong."""
    best = None
    for i in range(WIN):
        v = prof[i]
        lo = max(0, i - 3)
        hi = min(len(prof), i + 4)
        neigh = np.concatenate([prof[lo:i], prof[i + 1:hi]])
        if len(neigh) == 0:
            continue
        drop = float(neigh.mean()) - float(v)
        if drop >= MIN_DROP and abs(v - content_ref) > MIN_DROP:
            if best is None or drop > best[1]:
                best = (i, drop, float(v))
    return best


def scan(pattern):
    files = sorted(BG.glob(f"{pattern}*.png"))
    flagged = []
    for f in files:
        a = np.asarray(Image.open(f).convert("L"), np.float32)
        h, w = a.shape
        rows = a.mean(axis=1)
        cols = a.mean(axis=0)
        hits = []
        # canh tren: noi dung = trung binh hang 40..90
        rref = float(rows[WIN:WIN + 50].mean())
        b = line_scan(rows, rref)
        if b:
            hits.append(f"top={b[0]}px(drop {b[1]:.0f},sang {b[2]:.0f})")
        # canh duoi
        rref_b = float(rows[h - WIN - 50:h - WIN].mean())
        rev = rows[::-1]
        b = line_scan(rev, rref_b)
        if b:
            hits.append(f"bottom={b[0]}px(drop {b[1]:.0f},sang {b[2]:.0f})")
        # canh trai
        cref = float(cols[WIN:WIN + 50].mean())
        b = line_scan(cols, cref)
        if b:
            hits.append(f"left={b[0]}px(drop {b[1]:.0f},sang {b[2]:.0f})")
        # canh phai
        cref_r = float(cols[w - WIN - 50:w - WIN].mean())
        b = line_scan(cols[::-1], cref_r)
        if b:
            hits.append(f"right={b[0]}px(drop {b[1]:.0f},sang {b[2]:.0f})")
        if hits:
            flagged.append((f.name, hits))
    print(f"{'anh':<28}{'viem mong (1 dong net)':<60}")
    print("-" * 90)
    for name, hits in flagged:
        print(f"{name:<28}{', '.join(hits)}")
    print("-" * 90)
    print(f"tong {len(files)} · co vien mong {len(flagged)} · sach {len(files) - len(flagged)}")
    return flagged


if __name__ == "__main__":
    pat = sys.argv[1] if len(sys.argv) > 1 else "t3"
    scan(pat)
