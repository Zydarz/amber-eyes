import re
vn_lines = open("02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md", encoding="utf-8").readlines()
for l in vn_lines:
    if "4-13" in l or "4-14" in l:
        print(l.strip())
