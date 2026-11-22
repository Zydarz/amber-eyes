# -*- coding: utf-8 -*-
"""Backup thu muc san xuat TikTok Tap 03 (VN/EN/JA) truoc khi chay lai generator."""
import os
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"D:/TEST/Gax/amber-eyes"
BAK = os.path.join(ROOT, ".work", "_cu", "tk03_regen_%s" % time.strftime("%Y%m%d_%H%M"))
os.makedirs(BAK, exist_ok=True)
for d in ("Tap03", "Tap03_EN", "Tap03_JA"):
    src = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK", d)
    if os.path.exists(src):
        shutil.copytree(src, os.path.join(BAK, d))
        print("backup:", d)
print("->", BAK)
