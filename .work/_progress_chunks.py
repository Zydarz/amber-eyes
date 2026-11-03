#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tien do chunk: doc bo dem khung tu log (UTF-16) cua tung chunk."""
import datetime
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path("D:/TEST/Gax/amber-eyes/.work")
FPS = 30
CH = {"A": (0, 16470), "B": (16470, 16470), "C": (32940, 16458)}


def read_log(p):
    b = p.read_bytes()
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return b.decode("utf-16")
    if b.count(0) > len(b) * 0.02:
        return b.decode("utf-16-le")
    return b.decode("utf-8-sig", errors="replace")


for k, (f0, nf) in CH.items():
    lg = W / f"_chunk_{k}_t03_en.log"
    d = W / f"video3_EN_t03_c{k}"
    parts = sorted(d.glob("part_*.mp4"))
    mb = sum(p.stat().st_size for p in parts) / 1e6
    # moi part: nf/6 khung -> byte cuoi cung ~ (nf/6/30)*0.375 MB
    want_mb = (nf / 6 / 30) * 0.375 * 6
    done = 0
    if lg.exists():
        txt = read_log(lg)
        vals = {}
        for m in re.finditer(r"\[part_(\d+)\.mp4\]\s+(\d+)/(\d+)", txt):
            vals[m.group(1)] = int(m.group(2))
        done = sum(vals.values())
    print(f"chunk {k}: {mb:7.1f}/{want_mb:.0f} MB ({100*mb/want_mb:5.1f}%) · "
          f"log frames {done}/{nf} · part {len(parts)}")
