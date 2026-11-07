# -*- coding: utf-8 -*-
"""Check Vietnamese words against a dictionary or find rare syllables."""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

words = set()
for e in loi:
    for s in e['sentences']:
        tokens = re.findall(r'[^\s.,:;?!"“”()\'’/\\–-]+', s['text'])
        for t in tokens:
            if not t.isdigit():
                words.add(t)

known_terms = {
    'Colleen', 'Stan', 'Cameron', 'Hooker', 'Janice', 'Red', 'Bluff', 'Westwood', 'Eugene',
    'Riverside', 'Tehama', 'The', 'Company', 'Martin', 'Seligman', 'Patrick', 'Carnes',
    'Chris', 'Hatcher', 'Clarence', 'Knight', 'Richard', 'Tedeschi', 'Lawrence', 'Calhoun',
    'Gavin', 'de', 'Becker', 'Gifts', 'of', 'Life', 'Gift', 'Fear', 'Amber', 'Eyes', 'BGM',
    'California', 'Sykes', 'Matza', 'Compartmentalization', 'Growth', 'Sheriff’s', 'Office',
    'Post-Traumatic', 'Stockholm', 'Trauma', 'Bonding', 'Simple', 'County', 'Post', 'Traumatic'
}

vn_words = sorted([w for w in words if w not in known_terms], key=lambda x: x.lower())

# Let's inspect all words alphabetically in chunks of 50 or write to a text file to review
with open('.work/_vn_vocab_tap10.txt', 'w', encoding='utf-8') as f:
    for w in vn_words:
        f.write(w + '\n')

print(f"Đã xuất {len(vn_words)} từ vào .work/_vn_vocab_tap10.txt để rà soát.")
