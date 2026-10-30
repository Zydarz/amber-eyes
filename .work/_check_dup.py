#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rà file SFX trùng MD5 trong assets/sfx/ (2 mã dùng chung 1 track là chủ ý
=> đánh dấu ACCEPTED nếu mã nằm trong danh sách cho phép)."""
import hashlib
import io
import sys
from collections import defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
SFX = ROOT / "assets" / "sfx"
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
TICK = chr(96)

ACCEPT = {("fx_lav_mic_breathing", "fx_breathing_tense_close")}

files = sorted(p for p in SFX.rglob("*.wav"))
h = defaultdict(list)
for p in files:
    m = hashlib.md5(p.read_bytes()).hexdigest()
    h[m].append(p)

dups = {k: v for k, v in h.items() if len(v) > 1}
print("tong file wav:", len(files), "| nhom trung MD5:", len(dups))
for k, v in dups.items():
    names = sorted({p.stem for p in v})
    ok = any(set(x) == set(names) for x in ACCEPT)
    print(("  ACCEPT " if ok else "  !! CANH BAO ") + k[:8] + " -> " + ", ".join(names))

# kiem tra file rong / qua nho
short = [p for p in files if p.stat().st_size < 2000]
print("file qua nho/rong:", len(short))
for p in short:
    print("   ", p.relative_to(ROOT), p.stat().st_size)
