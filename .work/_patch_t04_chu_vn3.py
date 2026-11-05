#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bản vá 3 — Tập 04: loại từ bị cấm A9.2 khỏi chữ trên hình.

Cổng QC `_qc_tap02_shots.py` cấm các từ: sát hại, đầu độc, máu, thi thể, …
Mỗi mảnh thay thế vẫn phải là chuỗi từ LIÊN TÚC trong câu đang đọc.
"""
from pathlib import Path

P = Path(__file__).resolve().parent / "_t04_chu_vn.py"
src = P.read_text(encoding="utf-8")

FIX = [
    # 1-18: "Sát hại khoảng 40 bệnh nhân" -> bỏ "Sát hại"
    ("*Sát hại khoảng 40 bệnh nhân*", "*Khoảng 40 bệnh nhân*"),
    # 2-08: "NẤC THANG THỨ HAI: SÁT HẠI BỆNH NHÂN HẤP HỐI" -> bỏ "SÁT HẠI"
    ("**NẤC THANG THỨ HAI: SÁT HẠI BỆNH NHÂN HẤP HỐI**", "**NẤC THANG THỨ HAI** · *Bệnh nhân hấp hối*"),
    # 2-09: "Đầu độc ngẫu nhiên các túi dịch truyền" -> bỏ "Đầu độc"
    ("*Đầu độc ngẫu nhiên các túi dịch truyền*", "*Ngẫu nhiên các túi dịch truyền*"),
    # 2-10: "Sát hại cả những bệnh nhân trẻ tuổi…" -> bỏ "Sát hại"
    ("*Sát hại cả những bệnh nhân trẻ tuổi đang bình phục khỏe mạnh*",
     "*Cả những bệnh nhân trẻ tuổi đang bình phục khỏe mạnh*"),
    # 3-11: "…sau mỗi ca trực đẫm máu" -> bỏ "đẫm máu"
    ("*Vô hiệu hóa cảm giác tội lỗi và ngủ ngon sau mỗi ca trực đẫm máu*",
     "*Vô hiệu hóa cảm giác tội lỗi và ngủ ngon sau mỗi ca trực*"),
]

miss = []
for old, new in FIX:
    if old not in src:
        miss.append(old[:70])
    else:
        src = src.replace(old, new, 1)
P.write_text(src, encoding="utf-8", newline="\n")
print("đã vá:", len(FIX) - len(miss), "· không tìm thấy:", len(miss))
for m in miss:
    print("  ✗", m)
