#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tìm từ Latin trong bản JA KHÔNG có trong bản VN (nghi rác model chèn vào) + ngữ cảnh.

    py -3 .work/_ja_latin_scan.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402

RX_TOK = re.compile(r"[A-Za-zÀ-ỹĐđ][A-Za-zÀ-ỹĐđ'’.-]*")

# các từ hợp lệ (nhãn vai, thuật ngữ, tên riêng quốc tế) -> bỏ qua
ALLOW = {
    "tap", "ksas", "testa", "narrator", "host", "post", "shot", "door", "foot",
    "ambient", "micro", "out", "video", "piano", "violin", "cello", "drone",
    "fade", "bass", "camera", "amenities", "naghten", "maghten", "him", "her",
    "and", "the", "of", "in", "to", "a", "is", "it", "he", "she", "they",
}


def toks(t):
    return {m.group(0).strip(".'’-").lower() for m in RX_TOK.finditer(t) if len(m.group(0)) > 2}


rows = []
for i in range(1, 30):
    ep = "%02d" % i
    vp = M.canonical_vn(ep)
    jp = Path(r"D:\TEST\Gax\Audi\01_KICH_BAN") / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not vp.exists() or not jp.exists():
        continue
    vn = vp.read_text(encoding="utf-8")
    ja = jp.read_text(encoding="utf-8")
    vt = toks(vn)
    jt = toks(ja)
    extra = sorted(t for t in jt - vt if t not in ALLOW)
    for t in extra:
        for m in RX_TOK.finditer(ja):
            w = m.group(0).strip(".'’-")
            if w.lower() != t:
                continue
            s = max(0, m.start() - 55)
            e = min(len(ja), m.end() + 55)
            rows.append((ep, w, ja[s:e].replace("\n", " ")))
            break

print(f"=== {len(rows)} từ Latin không có trong bản VN ===")
for ep, w, ctx in rows:
    print(f"  Tap{ep} [{w}] ...{ctx}...")
