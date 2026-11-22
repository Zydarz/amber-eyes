# -*- coding: utf-8 -*-
"""Kiem tra spec clip TikTok: truong nen (bg/nen) dang tro toi ten nao."""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"

PAT = re.compile(r'"(?:bg|nen|background)"\s*:\s*"([a-z0-9_]+)"')

for tag in ("Tap02", "Tap03"):
    for lang in ("", "_EN", "_JA"):
        p = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK", tag + lang, "SPEC_AUDIO_CLIP_%s%s.json" % (tag, lang))
        if not os.path.exists(p):
            continue
        s = io.open(p, encoding="utf-8-sig").read()
        bgs = sorted(set(PAT.findall(s)))
        pref = {}
        for b in bgs:
            pref[b.split("_")[0]] = pref.get(b.split("_")[0], 0) + 1
        print("%-28s %2d nen duy nhat · tien to: %s" % (os.path.basename(p), len(bgs), pref))
        print("     ", bgs[:6], "...")
