# -*- coding: utf-8 -*-
import io, sys
s = io.open(r"D:/TEST/Gax/amber-eyes/.work/_build_tk_tap02.py", encoding="utf-8").read()
pats = [
    "dữ liệu có nguồn", "dữ kiện có nguồn",
    "toà", "trước toà", "hồ sơ toà án", "tòa án",
    "Chỉ dấu #", "chỉ dấu #",
    "“", "”", "„", '"',
    "dung nạp", "đói ảo tưởng",
    "NẤC 2", "NẤC 4", "bốn nấc thang",
    "BMW", "Cấp cao", "thương hại bản thân", "đau đớn",
    "trái ngược", "Gavin", "người phụ nữ hay gia đình",
    "toàn quyền", "Xem tập đầy đủ", "rình rập",
    "82 vụ", "Nguyên lý", "The Gift of Fear",
    "nữ nhân viên 27 tuổi", "Cảnh sát tỉnh Ontario mở cuộc",
]
for p in pats:
    print("%-30s %d" % (p, s.count(p)))
print("---- dong co 'toa' ----")
for i, line in enumerate(s.splitlines(), 1):
    if "toà" in line or "toả" in line:
        print(i, line.strip()[:150])
