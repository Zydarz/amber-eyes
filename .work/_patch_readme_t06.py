#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat dong Tap06 trong README.md bang so do thuc te."""
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

p = Path(r"D:/TEST/Gax/amber-eyes/README.md")
t = p.read_text(encoding="utf-8-sig")
lines = t.split("\n")

NEW = (
    "| **06 · Nụ cười chú hề & 29 bí mật** | `02_SAN_XUAT/Tap06/` — kế hoạch (73 shot), "
    "ảnh (64 nền), âm thanh, phụ đề | ✅ `Tap06_master.mp4` **21:05** (1.265,4 s · 458,2 MB · "
    "1920×1080@30 · H.264+AAC) — **giọng tiếng Việt Higgs Audio v3** · **QC A9.1–A9.4 đạt 23/23** "
    "(lệch hình/tiếng **0,0 ms** · −16,0 LUFS · true peak −1,8 dBTP · giải mã 0 lỗi · "
    "0 khoảng lặng) · bảng shot **viết lại theo 154 câu** (A11 #67) + sửa lỗi cột handoff "
    "(A11 #77) | còn: nghe duyệt + điền nguồn |"
)

hit = 0
for i, l in enumerate(lines):
    if l.startswith("| **06 · Nụ cười chú hề"):
        lines[i] = NEW
        hit += 1
p.write_text("\n".join(lines), encoding="utf-8")
print("thay", hit, "dong")
for l in lines:
    if l.startswith("| **06 · Nụ cười chú hề"):
        print(l[:160], "...")
