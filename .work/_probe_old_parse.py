#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thử parser CŨ trên 1 dòng markdown cụ thể để thấy đúng hành vi."""
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")
src = subprocess.run(["git", "show", "HEAD:.work/parse_kichban.py"], cwd=ROOT,
                     capture_output=True).stdout.decode("utf-8")
tmp = Path(tempfile.gettempdir()) / "_pk_o.py"
tmp.write_text(src, encoding="utf-8")
spec = importlib.util.spec_from_file_location("pk_o", tmp)
OLD = importlib.util.module_from_spec(spec)
spec.loader.exec_module(OLD)

print("--- HEAD parse_kichban.py, đoạn xử lý dòng ---")
import re
for i, l in enumerate(src.splitlines()):
    if "re.sub(r\"'(" in l or "strip('" in l or "replace('**'" in l:
        print(f"{i+1}: {l}")

LINES = [
    '"Trên trang Facebook chung của hai mẹ con nổi tiếng nhất vùng – bà Dee Dee Blanchard và cô con gái tật nguyền Gypsy Rose – bỗng xuất hiện một dòng trạng thái ngắn ngủi nhưng khiến cả khu phố chết lặng: *\'Con khốn đó chết rồi.\'*',
    'Trenton không chỉ là căn cứ quân sự đơn thuần, mà là nơi đón nhận linh cữu các liệt sĩ Canada từ chiến trường Afghanistan trở về dọc \'Con lộ Anh hùng\'. Người đứng đầu nghi lễ thiêng liêng ấy chính là Williams."',
    "'Tôi đã giết mẹ tôi và người bạn của bà.",
    "Tôi có thể chỉ cho các anh biết tôi đã chôn những mảnh vụn của họ ở đâu.'",
    "Đó là 'Big Ed' – một gã thanh niên 24 tuổi, cao 2 mét 06, nặng khoảng 127 ký.",
]
for L in LINES:
    t = re.sub(r"^\*\s+", "", L)
    t = re.sub(r"^\d+\.\s+", "", t)
    t = t.replace("**", "").replace("*", "")
    t = t.strip().strip('"“”').strip()
    t = re.sub(r"'([^']+)'", r"“\1”", t)
    print("\nRAW :", L[:90])
    print("SAU :", t[:150])
