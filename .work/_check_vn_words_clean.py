# -*- coding: utf-8 -*-
"""Check Vietnamese words accurately."""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

words = set()
for e in loi:
    for s in e['sentences']:
        # Tokenize words, stripping punctuation
        tokens = re.findall(r'[^\s.,:;?!"“”()\'’/\\–-]+', s['text'])
        for t in tokens:
            words.add(t)

known_terms = {
    'Colleen', 'Stan', 'Cameron', 'Hooker', 'Janice', 'Red', 'Bluff', 'Westwood', 'Eugene',
    'Riverside', 'Tehama', 'The', 'Company', 'Martin', 'Seligman', 'Patrick', 'Carnes',
    'Chris', 'Hatcher', 'Clarence', 'Knight', 'Richard', 'Tedeschi', 'Lawrence', 'Calhoun',
    'Gavin', 'de', 'Becker', 'Gifts', 'of', 'Life', 'Gift', 'Fear', 'Amber', 'Eyes', 'BGM',
    'California', 'Sykes', 'Matza', 'Compartmentalization', 'Growth', 'Sheriff’s', 'Office',
    'Post-Traumatic', 'Stockholm', 'Trauma', 'Bonding', 'Simple', 'County'
}

# Separate words into pure numbers, known terms, and Vietnamese words
vn_words = set()
for w in words:
    if w.isdigit():
        continue
    if w in known_terms:
        continue
    vn_words.add(w)

print(f"Tổng số từ cần kiểm tra: {len(vn_words)}")

# Check for mixed casing like camelCase
camel = []
for w in vn_words:
    # check if any uppercase letter occurs after index 0
    if any(c.isupper() for c in w[1:]):
        camel.append(w)

print(f"Từ có chữ hoa bất thường ở giữa: {camel}")

# Check for characters foreign to standard Vietnamese
foreign_chars = []
for w in vn_words:
    for c in w:
        if c.lower() in 'fwzj':
            foreign_chars.append((w, c))

print(f"Từ có ký tự f, w, z, j (ngoài tên riêng): {foreign_chars}")
