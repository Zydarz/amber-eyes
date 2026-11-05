#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sửa bảng shot Tập 03 theo QC (V3/A9.2) — chỉ sửa CHỮ TRÊN HÌNH, không đụng lời đọc.

Mỗi thay thế có điều kiện (old phải tồn tại đúng 1 lần) ⇒ fail rõ ràng nếu
hồ sơ đã đổi. Ghi bản sao lưu trước khi ghi (L5).

    py -3 .work/_patch_shots_t03.py
"""
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")
PLAN = ROOT / "02_SAN_XUAT" / "Tap03" / "KeHoach_Video_Tap03.md"

# (mã shot, old, new, lý do)
PATCH = [
    ("1-05",
     "*Hắn đã sát hại mẹ mình*",
     "*Hắn đã giết mẹ mình*",
     "A9.2: 'sát hại' là từ cấm; câu 1.03#8 đọc 'hắn đã giết mẹ mình' → lấy nguyên văn"),
    ("2-10",
     "*Thi thể rải rác dưới những vực sâu hẻo lánh*",
     "*Dấu vết của các nạn nhân được tìm thấy rải rác ở những vùng hẻo lánh*",
     "A9.2/V9: 'thi thể' là từ cấm; câu 2.06#1 nói 'Dấu vết của các nạn nhân ... rải rác ở những vùng hẻo lánh'"),
    ("3-12",
     "Bệnh viện Atascadero: 5 năm",
     "Bệnh viện Atascadero: NĂM NĂM",
     "A9.2: số '5' không có trong câu (3.08#4 đọc 'năm năm') → viết bằng chữ, đúng chuẩn Tập 02"),
    ("3-18",
     "*Quan sát cơn khát máu như nhà khoa học theo dõi thí nghiệm*",
     "*Không có cảm xúc tội lỗi như người bình thường*",
     "A9.2/V9: 'máu' là từ cấm; lấy nguyên văn câu 3.11#4 (cùng shot)"),
    ("4-11",
     "**3 KHÁI NIỆM MANG TÍNH CÁCH MẠNG**",
     "**BA KHÁI NIỆM MANG TÍNH CÁCH MẠNG**",
     "A9.2: số '3' không có trong câu (4.07#1 đọc 'Ba khái niệm') → viết bằng chữ"),
    ("5-04",
     "Bị bác ân xá hơn 10 lần",
     "Bị bác ân xá hơn MƯỜI LẦN",
     "A9.2: số '10' không có trong câu (5.02#9 đọc 'hơn mười lần') → viết bằng chữ"),
]

txt = PLAN.read_text(encoding="utf-8")
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
bk = ROOT / ".work" / "_cu" / f"plan_t03_qc_{stamp}"
bk.mkdir(parents=True, exist_ok=True)
shutil.copy2(PLAN, bk / "KeHoach_Video_Tap03.md.bak")
print(f"BACKUP: {bk}")

ok = True
for sid, old, new, why in PATCH:
    n = txt.count(old)
    if n != 1:
        print(f"  [LOI] {sid}: tìm thấy {n} lần (cần đúng 1) — {old!r}")
        ok = False
        continue
    txt = txt.replace(old, new)
    print(f"  [OK  ] {sid}: {old!r}\n         -> {new!r}\n         ({why})")

if not ok:
    print("\nKHÔNG ghi file (có dòng không khớp).")
    sys.exit(1)

PLAN.write_text(txt, encoding="utf-8")
print(f"\nĐã ghi: {PLAN}")
print(f"Backup : {bk / 'KeHoach_Video_Tap03.md.bak'}")
