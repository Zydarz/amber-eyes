#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them NHIEU dong manifest mot luc (theo dung thu tu bam tai).

Dung:  <file.tsv> | pipe bang stdin
Moi dong: ten_track <TAB> ma_sfx <TAB> loai <TAB> dest <TAB> the_loai <TAB> thoi_luong_giay
Ghi append vao .work/yt_map.tsv. Bo qua dong trung nghiem tuyet doi.
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / ".work" / "yt_map.tsv"

src = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else sys.stdin.read()
new = []
for raw in src.splitlines():
    if not raw.strip() or raw.startswith("#"):
        continue
    p = raw.split("\t")
    if len(p) < 6:
        raise SystemExit(f"Dong khong du 6 truong: {raw!r}")
    new.append("\t".join(x.strip() for x in p[:6]))

existing = set()
if MAP.exists():
    for l in MAP.read_text(encoding="utf-8-sig").splitlines():
        if l.strip():
            existing.add(l.rstrip())

add, skip = [], 0
for l in new:
    if l in existing:
        skip += 1
    else:
        add.append(l)
        existing.add(l)

with MAP.open("a", encoding="utf-8") as f:
    for l in add:
        f.write(l + "\n")

print(f"manifest: +{len(add)} dong moi, bo qua {skip} trung, tong {len(existing)} dong")
for l in add:
    p = l.split("\t")
    print(f"  + {p[0]}  ->  {p[1]}  ({p[5]}s)")
