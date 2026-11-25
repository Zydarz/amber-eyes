# -*- coding: utf-8 -*-
"""Kiem tra phu con: 54 shot cua 5 clip TikTok Tap 05 co nen doc 9:16 hay chua.

- Tu bang shot trong KE_HOACH_CLIP_TAP05.md -> ten nen can dung
- Kiem tra assets/bg/tk05_<ten>.png ton tai + dung kich thuoc 1080x1920
- Kiem tra dong tuong ung trong provenance.json (AI that vs du phong)
- H22: 0 nen sinh ra ma khong dung · 0 shot muon nen · moi nen <= 3 shot / 30 s
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_scan_t05 import per, uniq  # noqa: E402
from _tk_src_t05 import PAIRS  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
DST = os.path.join(ROOT, "assets/bg")
PROV = os.path.join(ROOT, "provenance.json")

from PIL import Image  # noqa: E402

prov = json.loads(io.open(PROV, encoding="utf-8-sig").read())
items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
by_file = {it.get("file"): it for it in items}

print("=== PHU CO 54 SHOT / 5 CLIP (Tap 05) ===")
missing = []
badsize = []
ai = fb = 0
used = set()
per_bg = {}
for clip, rows in per.items():
    n_ok = 0
    for code, bg, mv in rows:
        used.add(bg)
        name = "tk05_%s" % bg[3:]
        p = os.path.join(DST, name + ".png")
        if not os.path.exists(p):
            missing.append((code, name))
            continue
        with Image.open(p) as im:
            if im.size != (1080, 1920):
                badsize.append((name, im.size))
        n_ok += 1
    print("  %s : %d/%d shot co nen doc" % (clip, n_ok, len(rows)))

print("\nshot thieu nen:", missing if missing else "KHONG CO")
print("nen sai kich thuoc:", badsize if badsize else "KHONG CO")

print("\n=== %d NEN DUNG TRONG CLIP ===" % len(used))
print("%-38s %10s %8s %s" % ("nen", "kich thuoc", "KB", "nguon"))
for bg in sorted(used):
    name = "tk05_%s" % bg[3:]
    p = os.path.join(DST, name + ".png")
    with Image.open(p) as im:
        size = "%dx%d" % im.size
    kb = os.path.getsize(p) / 1024
    row = by_file.get("assets/bg/%s.png" % name) or {}
    if row.get("prompt"):
        ai += 1
        src = "AI that"
    else:
        fb += 1
        src = "du phong crop 16:9"
    print("%-38s %10s %8.0f %s" % (name, size, kb, src))
print("\nTONG: %d nen · AI that %d · du phong %d" % (len(used), ai, fb))
missing_prov = [b for b in sorted(used) if ("assets/bg/tk05_%s.png" % b[3:]) not in by_file]
print("thieu dong provenance:", missing_prov if missing_prov else "khong co")

# ---- H22: nen sinh ra nhung khong dung / phan bo shot ----
declared = {n for n, _ in PAIRS}
unused = sorted(declared - {"tk05_%s" % b[3:] for b in used})
print("\nH22a nen sinh ra MA KHONG DUNG:", unused if unused else "KHONG CO")

import collections  # noqa: E402
dur = {}
for clip, rows in per.items():
    for code, bg, mv in rows:
        dur.setdefault(bg, []).append(code)
print("\nH22c phan bo nen (nguong: <=3 shot / <=30 s):")
viol = []
for bg in sorted(used):
    n = len(dur[bg])
    if n > 3:
        viol.append(bg)
    print("  %-38s %d shot  %s" % (bg, n, "<<< VI PHAM" if n > 3 else ""))
print("  VI PHAM:", viol if viol else "KHONG CO")
