#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So số VN vs JA theo GIÁ TRỊ (bỏ qua khác biệt định dạng) và in ngữ cảnh lệch."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402


def nums(text):
    out = {}
    for m in re.finditer(r"\d[\d.,]*", text):
        s = m.group(0).rstrip(".,")
        if not s:
            continue
        # chuẩn hoá về giá trị: 1.600 -> 1600 ; 0,13 -> 0.13
        t = s.replace(".", "").replace(",", ".")
        try:
            v = float(t)
        except ValueError:
            continue
        out.setdefault(v, []).append((s, m.start()))
    return out


eps = sys.argv[1:] or [f"{i:02d}" for i in range(1, 30)]
for ep in eps:
    p = M.KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not p.exists():
        continue
    ja = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
    vn = M.canonical_vn(ep).read_text(encoding="utf-8")
    nj, nv = nums(ja), nums(vn)
    only_vn = sorted(set(nv) - set(nj))
    only_ja = sorted(set(nj) - set(nv))
    if not only_vn and not only_ja:
        continue
    print(f"\n##### Tap{ep} #####")
    for v in only_vn:
        s, i = nv[v][0]
        print(f"  VN-only {s:>10s} : ...{vn[max(0,i-55):i+55]!r}")
    for v in only_ja:
        s, i = nj[v][0]
        print(f"  JA-only {s:>10s} : ...{ja[max(0,i-55):i+55]!r}")
