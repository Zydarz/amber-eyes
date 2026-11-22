# -*- coding: utf-8 -*-
with open('01_KICH_BAN/Tap48_EN/kichban_tap48_EN.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace â€\x9d or â€ with ”
text = text.replace('\u00e2\u20ac\u009d', '”')
text = text.replace('\u00e2\u20ac', '”')
text = text.replace('‘”', '‘')

with open('01_KICH_BAN/Tap48_EN/kichban_tap48_EN.md', 'w', encoding='utf-8') as f:
    f.write(text)
print("Cleaned up quotes in EN!")
