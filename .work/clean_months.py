# -*- coding: utf-8 -*-
src = open('01_KICH_BAN/Ho_So_Toi_Pham/Tap49/kichban_tap49_19112026.md', encoding='utf-8').read()

src = src.replace("tháng 7 năm một nghìn chín trăm bảy mươi sáu", "tháng bảy năm một nghìn chín trăm bảy mươi sáu")
src = src.replace("tháng 3 năm một nghìn chín trăm tám mươi sáu", "tháng ba năm một nghìn chín trăm tám mươi sáu")
src = src.replace("Tháng 9 năm hai nghìn không trăm lẻ ba", "Tháng chín năm hai nghìn không trăm lẻ ba")

open('01_KICH_BAN/Ho_So_Toi_Pham/Tap49/kichban_tap49_19112026.md', 'w', encoding='utf-8').write(src)
print("Replaced all month digits.")
