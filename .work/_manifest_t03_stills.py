#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — chụp hash ảnh tĩnh 3 ngôn ngữ (trước / sau render) để chứng minh cái gì đổi.

Dùng:  py -3 .work/_manifest_t03_stills.py <tag>
"""
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
TAG = sys.argv[1] if len(sys.argv) > 1 else "before"

DIRS = {
    "vi": WORK / "video3_t03" / "stills",
    "en": WORK / "video3_EN_t03" / "stills",
    "ja": WORK / "video3_JA_t03" / "stills",
}

out = {}
for lang, d in DIRS.items():
    files = sorted(d.glob("*.png"))
    man = {}
    for p in files:
        b = p.read_bytes()
        man[p.name] = {"sha256": hashlib.sha256(b).hexdigest()[:16], "size": len(b)}
    out[lang] = man
    print(f"[{lang}] {len(man)} ảnh · tổng {sum(v['size'] for v in man.values())/1e6:.1f} MB")

path = WORK / f"_cu/t03_20261105_1800/stills_manifest_{TAG}.json"
path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("->", path)
