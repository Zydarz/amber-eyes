#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rà chất lượng bản JA: cấu trúc (5 hồi, cue, vai) + mẫu ngẫu nhiên.

    py -3 .work/_ja_final_review.py [so_mau]
"""
import io
import random
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
KB = ROOT / "01_KICH_BAN"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

n_sample = int(sys.argv[1]) if len(sys.argv) > 1 else 2
random.seed(20261023)

print("=" * 78)
print("A. CẤU TRÚC 29 FILE JA")
print("=" * 78)
print(f"{'tập':<8}{'幕':<5}{'SFX':<6}{'BGM':<6}{'休止':<6}{'bảng':<6}{'vai':<6}{'dòng':<7}")
allok = True
for i in range(1, 30):
    ep = "%02d" % i
    f = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not f.exists():
        print(f"Tap{ep}: THIEU FILE")
        allok = False
        continue
    t = f.read_text(encoding="utf-8")
    acts = len(re.findall(r"^## 第\d+幕", t, re.M))
    sfx = len(re.findall(r"^\*\*\[SFX\]:\*\*", t, re.M))
    bgm = len(re.findall(r"^\*\*\[BGM\]:\*\*", t, re.M))
    pau = len(re.findall(r"^\*\*\[休止", t, re.M))
    tbl = len(re.findall(r"^\|.*\|$", t, re.M))
    rol = len(re.findall(r"^\*\*[^*]+\*\*", t, re.M))
    lines = len(t.splitlines())
    flag = "" if acts == 5 else "  <-- SO HOI KHONG DUNG 5"
    if acts != 5:
        allok = False
    print(f"Tap{ep:<5}{acts:<5}{sfx:<6}{bgm:<6}{pau:<6}{tbl:<6}{rol:<6}{lines:<7}{flag}")
print("=> moi tap deu co 5 hoi:", "DUNG" if allok else "SAI")

print()
print("=" * 78)
print("B. MAU NGUU NHIEN (doc tay)")
print("=" * 78)
pool = []
for i in range(1, 30):
    ep = "%02d" % i
    f = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    t = f.read_text(encoding="utf-8").splitlines()
    cand = [l for l in t
            if l.strip() and not l.startswith(("#", "|", "<!--"))
            and not l.startswith("**[") and not l.startswith("**原")
            and not l.startswith("**事実") and len(l) > 55]
    for c in cand:
        pool.append((ep, c))

for ep, line in random.sample(pool, 18):
    print(f"[Tap{ep}] {line[:230]}")

print()
print("=" * 78)
print("C. RAC LATIN - cho lay mau 5 dong")
print("=" * 78)
shown = 0
for i in range(1, 30):
    if shown >= 5:
        break
    ep = "%02d" % i
    f = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    for n, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if re.search(r"[A-Za-z]", l) and "日本語版" not in l and "原文" not in l:
            print(f"Tap{ep} d{n}: {l[:190]}")
            shown += 1
            break
