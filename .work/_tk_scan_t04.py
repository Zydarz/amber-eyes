# -*- coding: utf-8 -*-
"""Quet bang shot cua clip TikTok Tap 04 -> danh sach nen doc can sinh."""
import collections
import glob
import io
import json
import os
import re

ROOT = r"D:/TEST/Gax/amber-eyes"
PLAN = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK/Tap04/KE_HOACH_CLIP_TAP04.md")
BT = chr(96)  # backtick

ROW = re.compile(r"\|\s*" + BT + r"(TK\d\.01#\d+)" + BT + r"\s*\|\s*\w+\s*\|\s*\w+\s*\|\s*[-0-9.]+\s*\|\s*"
                 r"[0-9.]+\s*\|\s*" + BT + r"(t4_[a-z0-9_]+)" + BT + r"\s*\|\s*(\w+)\s*\|")

txt = io.open(PLAN, encoding="utf-8").read()
rows = ROW.findall(txt)
per = collections.OrderedDict()
for code, bg, mv in rows:
    per.setdefault(code.split(".")[0], []).append((code, bg, mv))

allbg = []
print("=== BANG SHOT / NEN ===")
for k, v in per.items():
    print("%s : %d shot" % (k, len(v)))
    for c, b, m in v:
        print("   %-10s %-26s %s" % (c, b, m))
    allbg += [b for _, b, _ in v]

uniq = sorted(set(allbg))
print("\nTONG shot = %d · nen duy nhat = %d" % (len(rows), len(uniq)))

# shot trong bang co the bi bo qua boi regex (kiểm tra)
allcodes = re.findall(r"\|\s*" + BT + r"(TK\d\.01#\d+)" + BT + r"\s*\|", txt)
missing = [c for c in allcodes if c not in [r[0] for r in rows]]
print("code khong khop duoc (thi cong):", sorted(set(missing)))

RAW = os.path.join(ROOT, "assets/bg/_raw")
print("\n=== NGUON 16:9 ===")
miss = []
for b in uniq:
    cands = sorted(glob.glob(os.path.join(RAW, b + ".*")))
    if not cands:
        miss.append(b)
        print("  THIEU %s" % b)
    else:
        print("  %-26s <- %s" % (b, ", ".join(os.path.basename(c) for c in cands)))
print("\nTHIEU NGUON (can khop lai):", miss)

out = os.path.join(ROOT, ".work/_tk04_bg_needed.json")
io.open(out, "w", encoding="utf-8").write(json.dumps(
    {"per_clip": {k: v for k, v in per.items()}, "unique": uniq, "thieu_nguon": miss},
    ensure_ascii=False, indent=1))
print("-> " + out)
