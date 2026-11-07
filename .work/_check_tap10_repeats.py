# -*- coding: utf-8 -*-
import sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

for e in loi:
    for s in e['sentences']:
        words = s['text'].split()
        for i in range(len(words)-1):
            w1 = re.sub(r'[^\w]', '', words[i]).lower()
            w2 = re.sub(r'[^\w]', '', words[i+1]).lower()
            if w1 and w1 == w2:
                print(f"{s['id']}: '{w1} {w2}' -> {s['text']}")
