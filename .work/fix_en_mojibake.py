# -*- coding: utf-8 -*-
with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap48_EN/kichban_tap48_EN.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace mojibake sequences common from UTF-8 misinterpreted as CP1252
replacements = [
    ('\u00e2\u20ac\u201c', '–'),    # â€“ -> en-dash
    ('\u00e2\u20ac\u201d', '—'),    # â€” -> em-dash
    ('\u00e2\u20ac\u0153', '“'),    # â€œ -> left double quote
    ('\u00e2\u20ac\u009d', '”'),    # â€ -> right double quote
    ('\u00e2\u20ac\u02dc', '‘'),    # â€˜ -> left single quote
    ('\u00e2\u20ac\u2122', '’'),    # â€™ -> right single quote
    ('\u00c2\u00b7', '·'),          # Â· -> middle dot
]

for old, new in replacements:
    count = text.count(old)
    if count > 0:
        print(f"Replacing {count} occurrences of {repr(old)} with {repr(new)}")
        text = text.replace(old, new)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap48_EN/kichban_tap48_EN.md', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated Tap 48 EN encoding clean-up!")
