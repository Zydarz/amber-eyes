# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
for e in p:
    if e['id'] == '4.05':
        for s in e['sentences']:
            print(f"SID {s['id']}: raw text = {repr(s['text'])}")
