# -*- coding: utf-8 -*-
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_19112026.md", "r", encoding="utf-8") as f:
    text = f.read()

old_s = "“Hiệu ứng hào quang” đã một lần nữa làm mờ mắt các nhà điều tra giàu kinh nghiệm nhất."
new_s = "Chính hiệu ứng hào quang đã một lần nữa làm mờ mắt các nhà điều tra giàu kinh nghiệm nhất."

assert old_s in text, "old_s not in text!"
text = text.replace(old_s, new_s)

with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_19112026.md", "w", encoding="utf-8") as f:
    f.write(text)

import subprocess
subprocess.run(["py", "-3", ".work/parse_kichban.py", "01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_19112026.md", ".work/t32_vn.json"])
print("Fixed successfully!")
