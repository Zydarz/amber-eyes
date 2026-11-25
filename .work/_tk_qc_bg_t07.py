# -*- coding: utf-8 -*-
"""QC nen doc TikTok Tap 07 (assets/bg/tk07_*.png) + kiem tra token ke hoach/spec.

Do bang GRAYSCALE L (cung cach QC chinh cua kenh):
  · hook  y 270-730  <= 58
  · sub   y 996-1254 <= 72
  · x 120-780 (vung chu an toan TikTok)
  · khong dong nao > 70% pixel vuot nguong sang 120
Kiem tra them:
  · kich thuoc 1080x1920
  · token trong ke hoach/spec da co file that
  · H22: moi nen <= 3 shot VA <= 30 s (thoi luong uoc luong theo so ky tu cau)
"""
import collections
import json
import pathlib
import re
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t07 import PAIRS  # noqa: E402

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

print("%-44s %-10s %-10s %7s %7s %7s" % ("nen", "kq", "size", "hook", "sub", "streak"))
for r in rows:
    print("%-44s %-10s %-10s %7s %7s %7s" % r)

print("\nVI PHAM / THIEU: %d / %d" % (bad, len(PAIRS)))

# ---------------------------------------------------------------- token
print("\n=== token trong ke hoach/spec ===")
files = {n for n, _ in PAIRS}
for d, fn in (("Tap07", "KE_HOACH_CLIP_TAP07.md"), ("Tap07_EN", "KE_HOACH_CLIP_TAP07_EN.md"),
              ("Tap07_JA", "KE_HOACH_CLIP_TAP07_JA.md"), ("Tap07", "SPEC_AUDIO_CLIP_TAP07.json"),
              ("Tap07_EN", "SPEC_AUDIO_CLIP_TAP07.json"), ("Tap07_JA", "SPEC_AUDIO_CLIP_TAP07.json")):
    p = TIK / d / fn
    txt = p.read_text(encoding="utf-8-sig")
    toks = set(re.findall(r"tk07_[a-z0-9_]+", txt))
    ngoai = sorted(t for t in toks if t not in files)
    thieu = sorted(t for t in toks if not (DST / (t + ".png")).exists())
    print("%-34s token=%2d · ngoai danh sach=%s · thieu file=%d %s"
          % (d + "/" + fn, len(toks), ngoai or "khong co", len(thieu), thieu or ""))

# ---------------------------------------------------------------- H22
print("\n=== H22 (moi nen <= 3 shot VA <= 30 s / tap) ===")
for d in ("Tap07", "Tap07_EN", "Tap07_JA"):
    spec = json.loads((TIK / d / "SPEC_AUDIO_CLIP_TAP07.json").read_text(encoding="utf-8"))
    shots = collections.Counter()
    secs = collections.defaultdict(float)
    for cname, c in spec["clips"].items():
        # thoi luong uoc luong: ty le theo so ky tu (chu) cua tung cau
        total_chars = sum(len(ln["text"]) for ln in c["lines"]) or 1
        total_dur = c.get("estimated_duration", 0) or 0
        if not total_dur:
            continue
        for ln in c["lines"]:
            dur = total_dur * len(ln["text"]) / total_chars
            shots[ln["bg"]] += 1
            secs[ln["bg"]] += dur
    v = []
    for bg, n in shots.morted if False else shots.most_common():
        if n > 3 or secs[bg] > 30.0:
            v.append("%s (%d shot, %.1f s)" % (bg, n, secs[bg]))
    print("%-10s nen=%d · VI PHAM H22: %s" % (d, len(shots), "; ".join(v) if v else "khong co"))
    for bg, n in shots.most_common():
        if n > 3:
            print("     (the CTA dong ket: %s — %d shot)" % (bg, n))
