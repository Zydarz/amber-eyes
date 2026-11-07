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
        # remove quotes, punctuation
        tokens = re.findall(r"\b[A-Za-z]+(?:'[A-Za-z]+)?\b", txt)
        for t in tokens:
            words.add(t)

print(f"Total unique English words: {len(words)}")

# Check for repeated adjacent words in EN sentences
for e in loi:
    for s in e['sentences']:
        txt = s['text']
        m = re.search(r'\b([a-zA-Z]{2,})\s+\1\b', txt, re.IGNORECASE)
        if m:
            print(f"[{s['id']}] Repeated word: '{m.group()}' in: {txt}")

# Check for lowercase start of sentence
for e in loi:
    for s in e['sentences']:
        txt = s['text'].strip()
        # strip opening quotes if any
        clean = txt.lstrip('“"\'‘')
        if clean and clean[0].islower():
            print(f"[{s['id']}] Lowercase start: {txt}")
