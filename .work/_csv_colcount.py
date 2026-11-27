# -*- coding: utf-8 -*-
"""Sua lai DONG CSV cua TK04_EN_2 (ghi chu co dau phay => split sai) + dem so cot tung dong."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CSV = pathlib.Path(r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv")
raw = CSV.read_bytes()
txt = raw.decode("utf-8")
parts = re.split(r"(\r\n|\n|\r)", txt)

for i in range(0, len(parts), 2):
    ln = parts[i]
    if ln.startswith("TK0"):
        print(f"{ln.split(',')[0]:12} so o = {len(ln.split(','))}")
