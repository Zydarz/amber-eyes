# -*- coding: utf-8 -*-
"""Kiểm toán: liệt kê CHÍNH XÁC các dòng đã đổi trong edition.py so với bản gốc."""
import difflib
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = pathlib.Path(__file__).resolve().parents[1] / ".work"

ORIG = WORK / "_cu" / "edition.py.bak_bgm_261025_151456"      # ban goc truoc khi va
CUR = WORK / "edition.py"

a = ORIG.read_text(encoding="utf-8").splitlines()
b = CUR.read_text(encoding="utf-8").splitlines()
diff = list(difflib.unified_diff(a, b, lineterm="", n=0))
print(f"So dong thay doi: {len([l for l in diff if l.startswith(('+','-')) and not l.startswith(('+++','---'))])}")
print()
for l in diff:
    if l.startswith(("+++", "---")):
        continue
    if l.startswith("@@"):
        continue
    print("  " + l.strip())
