#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đếm từ tiếng Anh còn sót trong bản JA (mượn từ hợp lệ vs tên riêng)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).parent))
import make_ja_scripts as M  # noqa: E402

tot_loan = 0
tot_all = 0
for i in range(1, 30):
    ep = f"{i:02d}"
    p = M.KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not p.exists():
        continue
    ja = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
    vn = M.canonical_vn(ep).read_text(encoding="utf-8")
    ok = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9\-'.]{1,}", vn)}
    words = re.findall(r"[A-Za-z][A-Za-z0-9\-'.]{1,}", ja)
    unk = [w for w in words if w.lower() not in ok]
    tot_loan += len(unk)
    tot_all += len(words)
    if unk:
        print(f"  tap{ep}: {len(unk)}/{len(words)} từ không có trong VN -> "
              f"{sorted(set(unk))[:8]}")
print(f"\nTỔNG: {tot_loan} từ lạ / {tot_all} từ Latin toàn bộ")
