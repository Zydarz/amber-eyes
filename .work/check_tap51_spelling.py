# -*- coding: utf-8 -*-
import re

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap51/kichban_tap51_22112026.md', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

# 1. Check parenthetical balance
for i, l in enumerate(lines):
    if l.count('(') != l.count(')'):
        print(f'Mismatched (): Line {i+1}: {l}')
    if l.count('[') != l.count(']'):
        print(f'Mismatched []: Line {i+1}: {l}')

# 2. Check quotes
open_q = False
for i, l in enumerate(lines):
    for ch in l:
        if ch == '“':
            open_q = True
        elif ch == '”':
            open_q = False
print('Quotes balanced:', not open_q)

# 3. Check repeated consecutive words
for i, l in enumerate(lines):
    words = l.split()
    for j in range(len(words)-1):
        w1 = re.sub(r'[^\w]', '', words[j].lower())
        w2 = re.sub(r'[^\w]', '', words[j+1].lower())
        if w1 and w1 == w2 and len(w1) > 1:
            print(f'Repeated word on line {i+1}: "{w1}" -> {l}')

# 4. Check for ellipses
for i, l in enumerate(lines):
    if '...' in l or '…' in l:
        print(f'Ellipsis on line {i+1}: {l}')

# 5. Check Chinese characters if any slipped in
han = re.findall(r'[\u4e00-\u9fff]', text)
if han:
    print('Found Chinese characters:', set(han))
else:
    print('No unexpected Chinese characters.')

print('Done linguistic check!')
