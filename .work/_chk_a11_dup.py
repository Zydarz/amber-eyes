# -*- coding: utf-8 -*-
"""Kiem tra so A11: duyet va trung so TRONG bang A11 (khong dem cac bang khac trong file)."""
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = pathlib.Path(__file__).resolve().parents[1] / "00_TIEU_CHUAN" / "TIEU_CHUAN_DUNG_VIDEO.md"
raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
lines = raw.split(nl)

# tim dong tieu de bang A11
start = None
for i, l in enumerate(lines):
    if re.match(r"^#{2,4}\s*A11", l.strip()) or re.match(r"^#+\s*A11\b", l.strip()):
        start = i
        break
print("A11 heading tai dong:", start, "|", lines[start].strip()[:80] if start is not None else None)

# quet den khi gap bang moi (dong tieu de khac) hoac het file
nums = []
for l in lines[start:]:
    if re.match(r"^#{1,6}\s", l) and not re.match(r"^#{2,4}\s*A11", l.strip()):
        break
    m = re.match(r"^\| (\d+) \|", l)
    if m:
        nums.append(int(m.group(1)))
c = collections.Counter(nums)
print("so muc trong bang A11:", len(nums), "| max:", max(nums) if nums else None)
print("trung so:", {k: v for k, v in c.items() if v > 1})
missing = [n for n in range(1, max(nums) + 1) if n not in c]
print("thieu so:", missing)
