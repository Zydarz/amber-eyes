# -*- coding: utf-8 -*-
"""Kiem tra muc dich: 32 nen 9:16 Tap 05 dung kich thuoc + nguong vung chu + provenance."""
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
HOOK = (270, 730)
SUB = (996, 1254)
SX0, SX1 = 120, 780
TH = 120

bad = []
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
    st_h = float((g[HOOK[0]:HOOK[1], SX0:SX1] > TH).mean(axis=1).max())
    st_s = float((g[SUB[0]:SUB[1], SX0:SX1] > TH).mean(axis=1).max())
    streak = max(st_h, st_s)
    ok = hook <= 58.0 and sub <= 72.0 and streak <= 0.70
    if not ok:
        bad.append((name, "hook=%.1f sub=%.1f streak=%.2f" % (hook, sub, streak)))
    rows.append((name, hook, sub, streak, "OK" if ok else "FAIL"))

print("%-36s %7s %7s %7s  %s" % ("nen", "hook", "sub", "streak", "trang thai"))
for r in rows:
    print("%-36s %7.1f %7.1f %7.2f  %s" % r)

prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
tk05 = [it for it in items if "tk05_" in str(it.get("file", ""))]
ai = [it for it in tk05 if it.get("prompt")]
fb = [it for it in tk05 if not it.get("prompt")]
print("\ntong nen TK05 trong provenance: %d (AI that %d · du phong %d)" % (len(tk05), len(ai), len(fb)))
print("file co tren dia: %d / 32" % len(rows))
if bad:
    print("\nLOI (%d):" % len(bad))
    for n, m in bad:
        print("  %-36s %s" % (n, m))
else:
    print("\nKHONG CO LOI KICH THUOC / NGUONG VUNG CHU")
