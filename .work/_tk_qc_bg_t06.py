# -*- coding: utf-8 -*-
"""QC so do nen doc TikTok Tap 06 (asset cuoi cua assets/bg/tk06_*.png).

Do bang GRAYSCALE L (cung cach QC chinh cua kenh):
  · hook  y 270-730  <= 58
  · sub   y 996-1254 <= 72
  · x 120-780 (vung chu an toan TikTok)
  · khong dong nao > 70% pixel vuot nguong sang 120
Kiem tra them: kich thuoc 1080x1920 + token trong ke hoach/spec da co file that.
"""
import json
import pathlib
import re
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t06 import PAIRS  # noqa: E402

ROOT = HERE.parent
DST = ROOT / "assets" / "bg"
TIK = ROOT / "02_SAN_XUAT" / "TIKTOK"

HOOK = (270, 730)
SUB = (996, 1254)
SX0, SX1 = 120, 780
T_HOOK, T_SUB = 58.0, 72.0
STREAK_TH, STREAK_PCT = 120, 0.70

rows = []
bad = 0
for name, ref in PAIRS:
    p = DST / (name + ".png")
    if not p.exists():
        rows.append((name, "THIEU FILE", "", "", "", ""))
        bad += 1
        continue
    with Image.open(p) as im:
        size = im.size
        g = np.asarray(im.convert("L"), dtype=np.float32)
    hook = float(g[HOOK[0]:HOOK[1], SX0:SX1].mean())
    sub = float(g[SUB[0]:SUB[1], SX0:SX1].mean())
    streak = 0.0
    for y0, y1 in (HOOK, SUB):
        reg = g[y0:y1, SX0:SX1]
        if reg.size:
            streak = max(streak, float((reg > STREAK_TH).mean(axis=1).max()))
    ok = (size == (1080, 1920) and hook <= T_HOOK and sub <= T_SUB and streak <= STREAK_PCT)
    if not ok:
        bad += 1
    rows.append((name, "OK" if ok else "LOI", "%dx%d" % size,
                 "%.1f" % hook, "%.1f" % sub, "%.2f" % streak))

print("%-40s %-5s %-10s %7s %7s %7s" % ("nen", "kq", "size", "hook", "sub", "streak"))
for r in rows:
    print("%-40s %-5s %-10s %7s %7s %7s" % r)

print("\nVI PHAM: %d / %d" % (bad, len(PAIRS)))

print("\n=== token trong ke hoach/spec ===")
files = {n for n, _ in PAIRS}
for d, fn in (("Tap06", "KE_HOACH_CLIP_TAP06.md"), ("Tap06_EN", "KE_HOACH_CLIP_TAP06_EN.md"),
              ("Tap06_JA", "KE_HOACH_CLIP_TAP06_JA.md"), ("Tap06", "SPEC_AUDIO_CLIP_TAP06.json"),
              ("Tap06_EN", "SPEC_AUDIO_CLIP_TAP06.json"), ("Tap06_JA", "SPEC_AUDIO_CLIP_TAP06.json")):
    p = TIK / d / fn
    txt = p.read_text(encoding="utf-8-sig")
    toks = set(re.findall(r"tk06_[a-z0-9_]+", txt))
    ngoai = sorted(t for t in toks if t not in files)
    thieu = sorted(t for t in toks if not (DST / (t + ".png")).exists())
    print("%-34s token=%2d · ngoai danh sach=%s · thieu file=%s"
          % (d + "/" + fn, len(toks), ngoai or "khong co", thieu or "khong co"))

# so nen dung trong tung clip
for d in ("Tap06", "Tap06_EN", "Tap06_JA"):
    spec = json.loads((TIK / d / "SPEC_AUDIO_CLIP_TAP06.json").read_text(encoding="utf-8"))
    used = set()
    for c in spec["clips"].values():
        for ln in c["lines"]:
            used.add(ln["bg"])
    print("%-10s nen dung trong spec: %d / %d" % (d, len(used), len(PAIRS)))
