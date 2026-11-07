# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md')
loi = [e for e in p if e['kind'] == 'LOI']

for e in loi:
    for s in e['sentences']:
        txt = s['text']
        for o_c in [('「', '」'), ('『', '』'), ('“', '”')]:
            open_c = txt.count(o_c[0])
            close_c = txt.count(o_c[1])
            if open_c != close_c:
                print(f"[{s['id']}] JA mismatch {o_c}: {open_c} vs {close_c} in: {txt}")
