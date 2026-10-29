#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đổi thang lệch tốc độ trong KEY của make_acting_tap03.py cho khớp độ phân bố đã duyệt
của Tập 02 (51% ở -0,06 · 26% ở -0,04 · đuôi -0,02/-0,03/-0,05 rõ ràng).

Lý do: BASE_DELTA đã âm sẵn, nên giá trị KEY cũ (-0,05…-0,02) cộng vào đều bị kẹp về
-0,06 ⇒ 65% câu cùng một tốc độ, mất tương phản. Thang mới chỉ 4 bậc, mỗi bậc lệch
nhau 0,01 nên các vai khác nhau vẫn tự tạo thêm bậc.
"""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

F = Path(r"D:\TEST\Gax\Audi\.work\make_acting_tap03.py")
raw = F.read_text(encoding="utf-8")

REMAP = {"-0.05": "-0.02", "-0.04": "-0.01", "-0.03": "-0.01", "-0.02": "0.0",
         "0.0": "0.0", "0.02": "0.02"}

pat = re.compile(r'^(\s*"[\d.]+#\d+": \["[a-z]+", )(-?[\d.]+)(, )', re.M)
counts = {}


def sub(m):
    old = m.group(2)
    new = REMAP.get(old)
    if new is None:
        raise SystemExit(f"gia tri lap chua biet remap: {old}")
    counts[old] = counts.get(old, 0) + 1
    return m.group(1) + new + m.group(3)


out = pat.sub(sub, raw)
F.write_text(out, encoding="utf-8")
print("Da doi thang lech toc do:")
for k in sorted(counts):
    print(f"  {k:>6} x{counts[k]:>3}  ->  {REMAP[k]}")
print(f"  tong {sum(counts.values())} moc")
