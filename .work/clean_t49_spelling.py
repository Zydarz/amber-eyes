# -*- coding: utf-8 -*-
import json
import re

src = open('01_KICH_BAN/Ho_So_Toi_Pham/Tap49/kichban_tap49_19112026.md', encoding='utf-8').read()

# Replace digits with Vietnamese words
replacements = [
    ("thập niên 1970", "thập niên một nghìn chín trăm bảy mươi"),
    ("năm 1944", "năm một nghìn chín trăm bốn mươi tư"),
    ("năm 1975", "năm một nghìn chín trăm bảy mươi lăm"),
    ("năm 1976", "năm một nghìn chín trăm bảy mươi sáu"),
    ("tháng 7 năm 1976", "tháng bảy năm một nghìn chín trăm bảy mươi sáu"),
    ("năm 1986", "năm một nghìn chín trăm tám mươi sáu"),
    ("tháng 3 năm 1986", "tháng ba năm một nghìn chín trăm tám mươi sáu"),
    ("năm 1997", "năm một nghìn chín trăm chín mươi bảy"),
    ("tháng 9 năm 2003", "tháng chín năm hai nghìn không trăm lẻ ba"),
    ("năm 2003", "năm hai nghìn không trăm lẻ ba"),
    ("tháng 12 năm 2022", "tháng mười hai năm hai nghìn không trăm hai mươi hai"),
    ("hai mươi hai,", "hai mươi hai,"),
]

for old, new in replacements:
    src = src.replace(old, new)

# Standardize curly quotes in text
# Replace single and double curved quotes with simple ones or proper text
src = src.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')

open('01_KICH_BAN/Ho_So_Toi_Pham/Tap49/kichban_tap49_19112026.md', 'w', encoding='utf-8').write(src)
print("Updated script with Vietnamese text numbers and clean formatting.")
