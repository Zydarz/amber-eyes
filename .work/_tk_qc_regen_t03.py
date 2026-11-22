# -*- coding: utf-8 -*-
"""Kiem tra sau khi chay lai generator: spec tro tk03_*, .md bang shot dung ten,
caption/mota khong doi so voi backup."""
import difflib
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
BAK = os.path.join(ROOT, ".work", "_cu", "tk03_regen_20261120_2316")

SPEC = re.compile(r'"(?:bg|nen|background)"\s*:\s*"([a-z0-9_]+)"')

for d in ("Tap03", "Tap03_EN", "Tap03_JA"):
    folder = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK", d)
    spec_p = os.path.join(folder, "SPEC_AUDIO_CLIP_TAP03.json")
    s = io.open(spec_p, encoding="utf-8-sig").read()
    bgs = sorted(set(SPEC.findall(s)))
    bad = [b for b in bgs if not b.startswith("tk03_")]
    miss = [b for b in bgs if not os.path.exists(os.path.join(ROOT, "assets", "bg", b + ".png"))]
    print("%-10s spec: %d nen · khong phai tk03_: %s · thieu file: %s"
          % (d, len(bgs), bad or "khong co", miss or "khong co"))

    # so sanh caption/mota voi backup
    for fn in sorted(os.listdir(folder)):
        if not (fn.startswith("Caption_") or fn.startswith("MoTa_")):
            continue
        new_p = os.path.join(folder, fn)
        old_p = os.path.join(BAK, d, fn)
        if not os.path.exists(old_p):
            print("   MOI:", fn)
            continue
        a = io.open(old_p, encoding="utf-8-sig").read()
        b = io.open(new_p, encoding="utf-8-sig").read()
        if a != b:
            print("   KHAC:", fn)
    print("   -> so sanh caption/mota xong")

# bang shot trong .md
for d, fn in (("Tap03", "KE_HOACH_CLIP_TAP03.md"),
               ("Tap03_EN", "KE_HOACH_CLIP_TAP03_EN.md"),
               ("Tap03_JA", "KE_HOACH_CLIP_TAP03_JA.md")):
    p = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK", d, fn)
    t = io.open(p, encoding="utf-8").read()
    rows = re.findall(r"\|\s*`TK\d\.01#\d+`\s*\|\s*`([a-z0-9_]+)`", t)
    if not rows:
        print("%-10s .md: khong co bang shot co cot nen" % d)
        continue
    bad = [r for r in rows if not r.startswith("tk03_")]
    print("%-10s .md: %d dong nen · khong phai tk03_: %s" % (d, len(rows), bad or "khong co"))
