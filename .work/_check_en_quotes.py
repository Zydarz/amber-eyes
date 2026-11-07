# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md')
loi = [e for e in p if e['kind'] == 'LOI']

for e in loi:
    for s in e['sentences']:
        txt = s['text']
        # remove internal apostrophes
        clean_txt = re.sub(r'([a-zA-Z])[’\']([a-zA-Z])', r'\1\2', txt)
        curly_open = clean_txt.count('“')
        curly_close = clean_txt.count('”')
        if curly_open != curly_close:
            print(f"[{s['id']}] Curly quote mismatch: {curly_open} vs {curly_close} in: {txt}")
        straight_q = clean_txt.count('"')
        if straight_q % 2 != 0:
            print(f"[{s['id']}] Straight quote mismatch: {straight_q} in: {txt}")
