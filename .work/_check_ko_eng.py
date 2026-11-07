# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md')
loi = [e for e in p if e['kind'] == 'LOI']

eng_words_ko = set()
for e in loi:
    for s in e['sentences']:
        tokens = re.findall(r'[a-zA-Z]+', s['text'])
        for t in tokens:
            eng_words_ko.add(t)

print("Các từ tiếng Anh trong kịch bản KO:")
print(sorted(eng_words_ko))
