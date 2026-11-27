# -*- coding: utf-8 -*-
"""Kiem tra chieu rong CSV: header vs tung dong (ke ca dong 'Tap04,...' 8 cot bi thua truoc)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CSV = pathlib.Path(r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv")
txt = CSV.read_bytes().decode("utf-8")
parts = re.split(r"(\r\n|\n|\r)", txt)
rows = []
for i in range(0, len(parts), 2):
    ln = parts[i]
    if ln.strip():
        rows.append(ln)
hdr = rows[0].split(",")
print("header:", len(hdr), "o ->", hdr)
for ln in rows[1:]:
    c = ln.split(",")
    if len(c) != len(hdr):
        print(f"  LECH {len(c):2} o (header {len(hdr)}) : {ln[:80]}")
