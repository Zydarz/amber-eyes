#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sửa bảng shot EN Tập 03 theo A9.2 (17 lỗi số / 13 shot).

Quy ước kênh (xem báo cáo Tập 02, shot 5-09): khi câu đọc VIẾT BẰNG CHỮ
("one thousand", "three", "ten") thì chữ trên hình cũng viết bằng chữ.
Chỉ sửa chữ trên hình, KHÔNG đụng lời đọc.

    py -3 .work/_patch_shots_t03_en.py
"""
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")
PLAN = ROOT / "02_SAN_XUAT" / "Tap03_EN" / "KeHoach_Video_Tap03_EN.md"

PATCH = [
    ("1-02", "OVER 1,000 MILES AWAY", "OVER ONE THOUSAND MILES AWAY",
     "câu 1.03#3 đọc 'Over one thousand miles away'"),
    ("1-03", "*6-foot-9 · 280 pounds*", "*SIX FEET NINE INCHES · 280 POUNDS*",
     "câu 1.03#6 đọc 'six feet nine inches tall, weighing around 280 pounds'"),
    ("1-22", "*6-foot-9 · IQ 145 · Top 0.13% of the human population*",
     "*SIX FEET NINE INCHES · IQ 145 · Top 0.13% of the human population*",
     "câu 1.13#2 đọc 'six feet nine inches ... IQ of 145 ... top 0.13 percent'"),
    ("2-05", "May 7, 1972:", "May 7th, 1972:",
     "câu 2.04#3 đọc 'On May 7th, 1972'"),
    ("2-06", "September 14, 1972:", "September 14th, 1972:",
     "câu 2.04#5 đọc 'On September 14th, 1972'"),
    ("2-06", "January 7, 1973:", "January 7th, 1973:",
     "câu 2.04#6 đọc 'On January 7th, 1973'"),
    ("2-17", "*Towering 6-foot-9 frame*", "*Towering six-foot-nine frame*",
     "câu 2.07#11 đọc 'Standing six-foot-nine'"),
    ("3-03", "**EXAMINING 3 DISTINCT PATHOLOGICAL LAYERS**",
     "**EXAMINING THREE DISTINCT PATHOLOGICAL LAYERS**",
     "câu 3.04#1 đọc 'the three deepest pathological layers'"),
    ("3-06", "**FROM AGE 8**", "**FROM AGE EIGHT**",
     "câu 3.05#6 đọc 'From the time Ed was eight years old'"),
    ("3-12", "Atascadero State Hospital: 5 years", "Atascadero State Hospital: FIVE YEARS",
     "câu 3.08#4 đọc 'He spent five years within that institution'"),
    ("4-11", "**3 REVOLUTIONARY CONCEPTS**", "**THREE REVOLUTIONARY CONCEPTS**",
     "câu 4.07#1 đọc 'Three revolutionary concepts'"),
    ("5-04", "Denied parole over 10 times", "Denied parole over TEN TIMES",
     "câu 5.02#9 đọc 'his petitions have been denied more than ten times'"),
    ("5-07", "**4 BEHAVIORAL RED FLAGS**", "**FOUR BEHAVIORAL RED FLAGS**",
     "câu 5.04#1 đọc 'outline four critical Red Flags'"),
    ("5-09", "Burying family cat alive at age 10", "Burying family cat alive at age TEN",
     "câu 5.05#4 đọc 'At age ten, the boy mistreated a family cat'"),
]

txt = PLAN.read_text(encoding="utf-8")
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
bk = ROOT / ".work" / "_cu" / f"plan_t03_en_qc_{stamp}"
bk.mkdir(parents=True, exist_ok=True)
shutil.copy2(PLAN, bk / "KeHoach_Video_Tap03_EN.md.bak")
print(f"BACKUP: {bk}")

ok = True
for sid, old, new, why in PATCH:
    n = txt.count(old)
    if n != 1:
        print(f"  [LOI] {sid}: tìm thấy {n} lần (cần đúng 1) — {old!r}")
        ok = False
        continue
    txt = txt.replace(old, new)
    print(f"  [OK  ] {sid}: {old!r} -> {new!r}\n         ({why})")

if not ok:
    print("\nKHÔNG ghi file.")
    sys.exit(1)

PLAN.write_text(txt, encoding="utf-8")
print(f"\nĐã ghi: {PLAN}")
print(f"Backup : {bk / 'KeHoach_Video_Tap03_EN.md.bak'}")
