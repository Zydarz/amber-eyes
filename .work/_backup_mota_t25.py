# -*- coding: utf-8 -*-
"""Sao lưu file mô tả Tap25 trước khi ghi đè (L5) vào .work/_cu/mo_ta_t25_20261126/."""
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
SAN = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"
BK = ROOT / ".work" / "_cu" / "mo_ta_t25_20261126"

TARGETS = [
    "Tap25/mo_ta.txt", "Tap25/xuat_ban/mo_ta.txt", "Tap25/nguon_mo_ta.txt",
    "Tap25_EN/description.txt", "Tap25_EN/mo_ta.txt", "Tap25_EN/nguon_mo_ta_EN.txt",
    "Tap25_EN/xuat_ban/description.txt", "Tap25_EN/xuat_ban/mo_ta.txt",
    "Tap25_JA/description.txt", "Tap25_JA/mo_ta.txt", "Tap25_JA/nguon_mo_ta_JA.txt",
    "Tap25_JA/xuat_ban/description.txt", "Tap25_JA/xuat_ban/mo_ta.txt",
    "Tap25_KO/description.txt", "Tap25_KO/mo_ta.txt", "Tap25_KO/nguon_mo_ta_KO.txt",
    "Tap25_KO/xuat_ban/description.txt", "Tap25_KO/xuat_ban/mo_ta.txt",
]
n = 0
for rel in TARGETS:
    src = SAN / rel
    if not src.exists():
        print(f"  - moi tao (chua co): {rel}")
        continue
    dst = BK / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  + backup: {rel}  ({src.stat().st_size} bytes)")
    n += 1
print(f"\nDa sao luu {n} file vao {BK.relative_to(ROOT)}")
