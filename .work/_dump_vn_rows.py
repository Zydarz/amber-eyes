#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump the VN shot table rows (Shot / Câu / Chữ / Beat) for the EN overlay task."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]

lines = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(lines) if i > i0 and l.startswith("**Tổng:"))

out = []
for l in lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    c = l.strip().strip("|").split("|")
    sid = m.group(1)
    cau = c[1].strip()
    chu = c[5].strip()
    beat = c[6].strip()
    n_ph = len(re.findall(r'ở "([^"]+)"', beat))
    out.append(f"{sid}\t[{cau}]\tCHU={chu}\tBEAT={beat}\tnph={n_ph}")

txt = "\n".join(out)
(W := ROOT / ".work").joinpath("_vn_rows_dump.txt").write_text(txt, encoding="utf-8")
print("rows:", len(out))
print("with 'ở':", sum(1 for o in out if "nph=0" not in o))
