# -*- coding: utf-8 -*-
"""Quet bang shot clip TikTok Tap 05 -> danh sach nen DOC can sinh (tk05_*).

Nguon 16:9 goc: assets/bg/_raw/t5_* (64 anh) — nen DOC 9:16 cho clip TikTok Tap 05
chua ton tai (assets/bg/tk05_*.png = 0).

Output: .work/_tk05_bg_needed.json
"""
import collections
import glob
import io
import json
import os
import re

ROOT = r"D:/TEST/Gax/amber-eyes"
PLAN = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK/Tap05/KE_HOACH_CLIP_TAP05.md")
BT = chr(96)

ROW = re.compile(r"\|\s*" + BT + r"(TK\d\.01#\d+)" + BT + r"\s*\|\s*\w+\s*\|\s*\w+\s*\|\s*[-0-9.]+\s*\|\s*"
                 r"[0-9.]+\s*\|\s*" + BT + r"(t5_[a-z0-9_]+)" + BT + r"\s*\|\s*(\w+)\s*\|")

txt = io.open(PLAN, encoding="utf-8").read()
rows = ROW.findall(txt)
per = collections.OrderedDict()
for code, bg, mv in rows:
    per.setdefault(code.split(".")[0], []).append((code, bg, mv))

allbg = []
print("=== BANG SHOT / NEN TAP 05 ===")
for k, v in per.items():
    print("%s : %d shot" % (k, len(v)))
    for c, b, m in v:
        print("   %-10s %-34s %s" % (c, b, m))
    allbg += [b for _, b, _ in v]

uniq = sorted(set(allbg))
print("\nTONG shot = %d · nen duy nhat = %d" % (len(rows), len(uniq)))

allcodes = re.findall(r"\|\s*" + BT + r"(TK\d\.01#\d+)" + BT + r"\s*\|", txt)
matched = [r[0] for r in rows]
missing = [c for c in allcodes if c not in matched]
print("code khong khop duoc (thi cong):", sorted(set(missing)))

RAW = os.path.join(ROOT, "assets/bg/_raw")
print("\n=== NGUON 16:9 ===")
miss = []
src = {}
for b in uniq:
    cands = sorted(glob.glob(os.path.join(RAW, b + ".*")))
    if not cands:
        miss.append(b)
        print("  THIEU %s" % b)
    else:
        src[b] = os.path.basename(cands[0])
        print("  %-34s <- %s" % (b, src[b]))
print("\nTHIEU NGUON (can khop lai):", miss)

# nen doc da co san?
DST = os.path.join(ROOT, "assets/bg")
have = []
for b in uniq:
    p = os.path.join(DST, "tk05_%s.png" % b[len("t5_"):])
    if os.path.exists(p):
        have.append(b)
print("nen doc da co (tk05_*): %d" % len(have), have)

out = os.path.join(ROOT, ".work/_tk05_bg_needed.json")
io.open(out, "w", encoding="utf-8", newline="\n").write(json.dumps(
    {"per_clip": {k: v for k, v in per.items()}, "unique": uniq,
     "thieu_nguon": miss, "source": src, "da_co": have},
    ensure_ascii=False, indent=1))
print("-> " + out)
