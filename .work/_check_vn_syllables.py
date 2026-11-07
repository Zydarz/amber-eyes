# -*- coding: utf-8 -*-
"""Check Vietnamese syllable validity and phonological structure."""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

words = set()
for e in loi:
    for s in e['sentences']:
        # Tokenize words
        tokens = re.findall(r'[a-zA-ZÀ-ỹ]+', s['text'])
        for t in tokens:
            words.add(t)

# Proper nouns and known English words to skip
known_foreign = {
    'Colleen', 'Stan', 'Cameron', 'Hooker', 'Janice', 'Red', 'Bluff', 'Westwood', 'Eugene',
    'Riverside', 'Tehama', 'The', 'Company', 'Martin', 'Seligman', 'Patrick', 'Carnes',
    'Chris', 'Hatcher', 'Clarence', 'Knight', 'Richard', 'Tedeschi', 'Lawrence', 'Calhoun',
    'Gavin', 'de', 'Becker', 'Gifts', 'of', 'Life', 'Gift', 'Fear', 'Amber', 'Eyes', 'BGM',
    'LOI', 'ACT', 'Simple', 'County', 'Sheriff', 'Stockholm', 'Trauma', 'Bonding'
}

print(f"Tổng số từ vựng đơn nhất: {len(words)}")

# Check Vietnamese valid initials, vowels, codas
# Vietnamese vowels: a, ă, â, e, ê, i, y, o, ô, ơ, u, ư
# Diacritics: huyền, sắc, hỏi, ngã, nặng
# Let's inspect syllables containing unusual characters or foreign letter combinations (f, w, z, j)
unusual = []
for w in sorted(words):
    if w in known_foreign:
        continue
    # check if word contains f, w, z, j
    if re.search(r'[fwzj]', w, re.IGNORECASE):
        unusual.append((w, "Chứa chữ f, w, z, j"))
    # check if word contains uppercase in the middle (e.g. Mc, CamelCase)
    if re.search(r'[a-zà-ỹ][A-ZÀ-Ỹ]', w):
        unusual.append((w, "Chữ hoa ở giữa từ"))

print(f"Số từ có yếu tố bất thường: {len(unusual)}")
for u in unusual:
    print(f"  {u[0]}: {u[1]}")
