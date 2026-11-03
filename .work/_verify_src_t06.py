#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem chung LAN CUOI 20 nguon cua Tap06: status 200 + noi dung >= 500 byte.

Doc danh sach tu generator (nguon su that) + meta trong .work/_src_cache/.
"""
import hashlib
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
CACHE = ROOT / ".work" / "_src_cache"
GEN = ROOT / ".work" / "_gen_t06_sources.py"

g = GEN.read_text(encoding="utf-8-sig")
block = g[g.index("SOURCES = ["):g.index("# ------", g.index("SOURCES = ["))]
urls = re.findall(r'"(https?://[^"]+)"', block)
ok = 0
for u in urls:
    k = hashlib.sha1(u.encode()).hexdigest()[:16]
    m, b = CACHE / f"{k}.meta", CACHE / f"{k}.txt"
    if not m.exists():
        print(f"  THIEU CACHE  {u}")
        continue
    st = m.read_text(encoding="utf-8").split("\t")[0]
    n = b.stat().st_size if b.exists() else 0
    good = st == "200" and n >= 500
    ok += good
    print(f"  {'OK ' if good else 'LO '} {st:>8} {n:>7}B  {u[:95]}")
print(f"\n==> {ok}/{len(urls)} nguon chuan (HTTP 200 + >= 500 byte noi dung)")
print("Tat ca URL trong mo ta va bang nguon deu lay tu generator nay.")

# doi chieu: khoi nguon trong mo_ta.txt phai dung 20/20 URL
mo = (ROOT / "02_SAN_XUAT/Tap06/xuat_ban/mo_ta.txt").read_text(encoding="utf-8")
miss = [u for u in urls if u not in mo]
print(f"==> mo_ta.txt chua {len(urls) - len(miss)}/{len(urls)} URL" + (f" — THIEU: {miss}" if miss else ""))
tbl = (ROOT / "02_SAN_XUAT/Tap06/xuat_ban/nguon_tham_khao.md").read_text(encoding="utf-8")
miss2 = [u for u in urls if u not in tbl]
print(f"==> nguon_tham_khao.md chua {len(urls) - len(miss2)}/{len(urls)} URL" + (f" — THIEU: {miss2}" if miss2 else ""))
rows = sum(1 for L in tbl.splitlines() if L.startswith("| `"))
warn = sum(1 for L in tbl.splitlines() if L.rstrip().endswith("| ⚠ |"))
print(f"==> bang nguon: {rows} dong du lieu · {warn} dong muc ⚠ · {rows - warn} dong muc ✅")
