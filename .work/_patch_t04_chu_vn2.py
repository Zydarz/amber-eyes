#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bản vá 2 — Tập 04: trích dẫn trên hình phải NGUYÊN VĂN (đúng cả hoa thường).

Cổng QC `_qc_tap02_shots.py` kiểm trích dẫn bằng `frag not in ctx` ⇒ phân biệt
hoa/thường. Các trích dẫn tự do phải lấy đúng một mảnh nguyên văn của câu.
"""
from pathlib import Path

P = Path(__file__).resolve().parent / "_t04_chu_vn.py"
src = P.read_text(encoding="utf-8")

FIX = [
    # 1-08: câu #5 trong script bắt đầu bằng "Cho đến khi" → trích nguyên cả câu
    ('→ `#5`: “Tất cả chúng tôi đều lạnh sống lưng vì nhận ra mình đã cùng làm việc bên cạnh một kẻ sát nhân hàng loạt nguy hiểm nhất.”',
     '→ `#5`: “Cho đến khi sự thật vở lở, tất cả chúng tôi đều lạnh sống lưng vì nhận ra mình đã cùng làm việc bên cạnh một kẻ sát nhân hàng loạt nguy hiểm nhất.”'),
    # 4-07: "Anh ấy biết bệnh tim của tôi." trong script có dấu phẩy, không có dấu chấm
    ('→ `#2`: “Anh ấy biết bệnh tim của tôi.”',
     '→ `#2`: “Anh ấy biết bệnh tim của tôi, luôn nhận làm giúp tôi những phần việc nặng”'),
    # 4-09: hai trích dẫn phải lấy nguyên câu (chữ hoa ở đầu câu trong script)
    ('“Người đàn ông hiền lành ngồi ăn khuya cùng tôi bấy lâu nay lại là một kẻ gieo rắc cái chết trong bóng tối.”',
     '“Tôi nhận ra người đàn ông hiền lành ngồi ăn khuya cùng tôi bấy lâu nay lại là một kẻ gieo rắc cái chết trong bóng tối.”'),
    ('→ `#6`: “Tôi biết mình không có quyền im lặng để tội ác tiếp tục diễn ra.”',
     '→ `#6`: “Dù vô cùng sợ hãi cho mạng sống của bản thân và tương lai của các con, tôi biết mình không có quyền im lặng để tội ác tiếp tục diễn ra.”'),
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
