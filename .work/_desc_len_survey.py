# -*- coding: utf-8 -*-
"""Đo số ký tự thật của mô tả Tập 13–17 mọi ngôn ngữ (so sánh trần 5000)."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
S = ROOT / "02_SAN_XUAT"

targets = []
for ep in ["13", "14", "15", "16", "17"]:
    for suf in ["", "_EN", "_JA", "_KO"]:
        d = S / f"Tap{ep}{suf}"
        for fn in ["mo_ta.txt", "description.txt"]:
            p = d / fn
            if p.exists():
                targets.append((f"T{ep}{suf}/{fn}", p))
            p2 = d / "xuat_ban" / fn
            if p2.exists():
                targets.append((f"T{ep}{suf}/xuat_ban/{fn}", p2))

seen = {}
for label, p in targets:
    t = p.read_text(encoding="utf-8").strip()
    seen[(label, len(t))] = t

for (label, n), _ in sorted(seen.items(), key=lambda kv: (kv[0][0].split("/")[0], kv[0][0])):
    flag = "PASS" if n <= 5000 else "OVER"
    print(f"{label:34s} {n:5d} ký tự  {flag}")
