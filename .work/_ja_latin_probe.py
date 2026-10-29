#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In chính xác các token Latin bị gắn cờ 'rác' kèm ngữ cảnh VN tương ứng."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402
from _qc_ja import latin_junk  # noqa: E402

RE_TOK = re.compile(r"[A-Za-z][A-Za-z0-9\-'.]{1,}")
for i in range(1, 30):
    ep = f"{i:02d}"
    p = M.KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not p.exists():
        continue
    ja = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
    vn = M.canonical_vn(ep).read_text(encoding="utf-8")
    junk = latin_junk(ja, vn)
    if not junk:
        continue
    print(f"\n##### Tap{ep} #####")
    vn_toks = RE_TOK.findall(vn)
    for w in junk:
        hits = [m.start() for m in re.finditer(re.escape(w), ja)]
        i = hits[0] if hits else 0
        ctx = ja[max(0, i - 45):i + len(w) + 45].replace("\n", " ")
        # token VN chứa w
        near = [t for t in vn_toks if w.lower() in t.lower()][:3]
        print(f"  {w!r}  x{len(hits)}")
        print(f"     JA: ...{ctx}...")
        print(f"     token VN chứa nó: {near}")
