# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md')
loi = [e for e in p if e['kind'] == 'LOI']

words = set()
for e in loi:
    for s in e['sentences']:
        txt = s['text']
        tokens = re.findall(r"\b[A-Za-z]+(?:'[A-Za-z]+)?\b", txt)
        for t in tokens:
            words.add(t)

with open('.work/_en_vocab_tap10.txt', 'w', encoding='utf-8') as f:
    for w in sorted(words, key=lambda x: x.lower()):
        f.write(w + '\n')

print(f"Exported {len(words)} EN words to .work/_en_vocab_tap10.txt")
