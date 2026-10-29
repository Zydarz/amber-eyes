#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xem ngữ cảnh của: Latin lạ, từ cấm, mất tên riêng, thuật ngữ thiếu."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from _qc_ja import BANNED_JA, latin_junk, names_of  # noqa: E402
from ja_glossary import TERMS  # noqa: E402

eps = sys.argv[1:] or ["01", "02", "03", "04"]
for ep in eps:
    ja_p = M.KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not ja_p.exists():
        continue
    vn_p = M.canonical_vn(ep)
    ja_text = ja_p.read_text(encoding="utf-8")
    ja_body = re.sub(r"<!--.*?-->", "", ja_text, flags=re.S)
    vn_text = vn_p.read_text(encoding="utf-8")
    print(f"\n########## Tap{ep} ##########")

    print("-- Latin không có trong VN --")
    for w in latin_junk(ja_body, vn_text):
        i = ja_body.find(w)
        print(f"   {w!r}: ...{ja_body[max(0,i-50):i+50]!r}")
        print(f"      có trong VN? {w in vn_text}  ·  lowercase? "
              f"{w.lower() in vn_text.lower()}")

    print("-- từ cấm --")
    for w, safe in BANNED_JA:
        probe = ja_body
        for s in safe:
            probe = probe.replace(s, "")
        if w in probe:
            i = probe.find(w)
            print(f"   {w!r}: ...{ja_body[max(0,ja_body.find(w)-45):ja_body.find(w)+45]!r}")
            print(f"      VN có tương ứng? "
                  f"{any(x in vn_text for x in {'máu','thi thể','sát hại','đòn','trói','bầm','đập','đầu độc','diệt cỏ','bỏ đói','móc áo','đồ lót','quan hệ tình dục','hiếp','cưỡng ép'})}")

    print("-- mất tên riêng --")
    for n in [x for x in names_of(vn_text) if vn_text.count(x) >= 3]:
        if n not in ja_text:
            print(f"   {n!r}")

    print("-- thuật ngữ chưa dùng --")
    for vi, ja_t in TERMS.items():
        if vi in vn_text and ja_t not in ja_text and len(vi) > 8:
            print(f"   {vi!r} -> {ja_t!r}")
            # tìm cụm tương đương trong JA
            key = vi.split()[0]
            i = ja_body.find(key)
            print(f"      JA quanh '{key}': ...{ja_body[max(0,i-40):i+90]!r}")
