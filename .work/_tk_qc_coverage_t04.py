# -*- coding: utf-8 -*-
"""Kiem tra phu con: 48 shot cua 5 clip TikTok Tap 04 co nen doc 9:16 hay chua.

- Tu bang shot trong KE_HOACH_CLIP_TAP04.md -> ten nen can dung
- Kiem tra assets/bg/tk04_<ten>.png ton tai + dung kich thuoc 1080x1920
- Kiem tra dong tuong ung trong provenance.json (AI that vs du phong)
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_scan_t04 import per  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
DST = os.path.join(ROOT, "assets/bg")
PROV = os.path.join(ROOT, "provenance.json")

prov = json.loads(io.open(PROV, encoding="utf-8-sig").read())
items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
by_file = {it.get("file"): it for it in items}

from PIL import Image  # noqa: E402

print("=== PHU CO 48 SHOT / 5 CLIP ===")
missing = []
bad_size = []
ai = fb = 0
used = set()
for clip, rows in per.items():
    n_ok = 0
    for code, bg, mv in rows:
        used.add(bg)
        name = "tk04_%s" % bg[3:]
        p = os.path.join(DST, name + ".png")
        if not os.path.exists(p):
            missing.append((code, name))
            continue
        with Image.open(p) as im:
            if im.size != (1080, 1920):
                bad_size.append((name, im.size))
        n_ok += 1
    print("  %s : %d/%d shot co nen doc" % (clip, n_ok, len(rows)))

print("\nshot thieu nen:", missing if missing else "KHONG CO")
print("nen sai kich thuoc:", bad_size if bad_size else "KHONG CO")

print("\n=== %d NEN DUNG TRONG CLIP ===" % len(used))
print("%-30s %10s %8s %s" % ("nen", "kich thuoc", "KB", "nguon"))
for bg in sorted(used):
    name = "tk04_%s" % bg[3:]
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
    print("%-30s %10s %8.0f %s" % (name, size, kb, src))
print("\nTONG: %d nen · AI that %d · du phong %d" % (len(used), ai, fb))
missing_prov = [b for b in sorted(used)
                if ("assets/bg/tk04_%s.png" % b[3:]) not in by_file]
print("thieu dong provenance:", missing_prov if missing_prov else "khong co")
