# -*- coding: utf-8 -*-
"""Kiem tra cuoi: 34 nen doc Tap 05 — kich thuoc, nguong vung chu, phu 54 shot, provenance.

Do theo luminance L (nhu QC), kiem tra 3 ngon ngu VI/EN/JA.
"""
import collections
import json
import pathlib
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t05 import PAIRS  # noqa: E402

ROOT = HERE.parent
DST = ROOT / "assets" / "bg"
PROV = ROOT / "provenance.json"
BASE = ROOT / "02_SAN_XUAT" / "TIKTOK"

HOOK = (270, 730)
SUB = (996, 1254)
SX0, SX1 = 120, 780
TH = 120
T_HOOK, T_SUB, T_STREAK = 58.0, 72.0, 0.70

print("=== A. NEN DOC (34) ===")
bad = []
ai = fb = 0
rows = []
for name, ref in PAIRS:
    p = DST / ("%s.png" % name)
    if not p.exists():
        bad.append((name, "THIEU FILE"))
        continue
    with Image.open(p) as im:
        if im.size != (1080, 1920):
            bad.append((name, "SAI KICH THUOC %s" % (im.size,)))
            continue
        g = np.asarray(im.convert("L"), dtype=np.float32)
    hook = float(g[HOOK[0]:HOOK[1], SX0:SX1].mean())
    sub = float(g[SUB[0]:SUB[1], SX0:SX1].mean())
    streak = max(float((g[HOOK[0]:HOOK[1], SX0:SX1] > TH).mean(axis=1).max()),
                 float((g[SUB[0]:SUB[1], SX0:SX1] > TH).mean(axis=1).max()))
    ok = hook <= T_HOOK and sub <= T_SUB and streak <= T_STREAK
    if not ok:
        bad.append((name, "hook=%.1f sub=%.1f streak=%.2f" % (hook, sub, streak)))
    rows.append((name, hook, sub, streak, ok))
print("%-36s %7s %7s %7s  %s" % ("nen", "hook", "sub", "streak", "trang thai"))
for r in rows:
    print("%-36s %7.1f %7.1f %7.2f  %s" % (r[0], r[1], r[2], r[3], "OK" if r[4] else "FAIL"))
if not rows:
    print("KHONG CO NEN NAO")
else:
    print("TB hook=%.1f · TB sub=%.1f" % (np.mean([r[1] for r in rows]), np.mean([r[2] for r in rows])))

print("\n=== B. PHU 54 SHOT × 3 NGON NGU ===")
for d in ("Tap05", "Tap05_EN", "Tap05_JA"):
    sp = json.loads((BASE / d / "SPEC_AUDIO_CLIP_TAP05.json").read_text(encoding="utf-8"))
    miss = []
    n = 0
    per = collections.Counter()
    for ck, c in sp["clips"].items():
        for ln in c["lines"]:
            n += 1
            per[ln["bg"]] += 1
            if not (DST / (ln["bg"] + ".png")).exists():
                miss.append((ck, ln["clip_line_id"], ln["bg"]))
    mx = max(per.values())
    print("%-9s shot=%d · nen duy nhat=%d · thieu file=%d · max shot/nen=%d"
          % (d, n, len(per), len(miss), mx))
    if miss:
        for m in miss:
            print("     THIEU:", m)

print("\n=== C. PROVENANCE ===")
prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
tk05 = [it for it in items if "tk05_" in str(it.get("file", ""))]
ai = [it for it in tk05 if it.get("prompt")]
fb = [it for it in tk05 if not it.get("prompt")]
print("dong tk05_ trong provenance: %d (AI that %d · du phong %d)" % (len(tk05), len(ai), len(fb)))
need = {"assets/bg/%s.png" % n for n, _ in PAIRS}
have = {it.get("file") for it in tk05}
print("thieu dong cho nen:", sorted(need - have) if need - have else "khong co")
for it in tk05:
    for k in ("cong_cu", "ngay", "dieu_khoan", "kiem_tra_thuong_mai"):
        if not it.get(k):
            print("  THIEU truong %-20s %s" % (k, it.get("file")))

print("\n=== D. KET LUA ===")
if bad:
    print("LOI (%d):" % len(bad))
    for n, m in bad:
        print("  %-36s %s" % (n, m))
else:
    print("34 nen: kich thuoc dung 1080x1920, nguong vung chu dat, khong vet ngang")
