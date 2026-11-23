# -*- coding: utf-8 -*-
with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap48/kichban_tap48_19112026.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix repeated words
text = text.replace(
    'biến bi kịch của đấng sinh thành thành một nhiệm vụ cơ học cần phải hoàn thành.',
    'biến bi kịch của đấng sinh thành trở thành một nhiệm vụ cơ học cần phải hoàn thành.'
)
text = text.replace(
    'Đây là sự hối hận mang tính tính toán thực dụng,',
    'Đây là sự hối hận mang tính toan tính thực dụng,'
)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap48/kichban_tap48_19112026.md', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated VN script word repetition!")
