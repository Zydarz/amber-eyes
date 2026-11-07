# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

issues = []
for e in loi:
    for s in e['sentences']:
        txt = s['text'].strip()
        sid = s['id']
        # check start capitalized
        clean_start = txt.lstrip('“"\'‘')
        if clean_start and clean_start[0].islower():
            issues.append((sid, "Start with lowercase", txt))
        # check end punctuation
        if not txt.endswith(('.', '!', '?', '”', '"')):
            issues.append((sid, "No end punctuation", txt))

print(f"VN structure issues: {len(issues)}")
for iss in issues:
    print(f"[{iss[0]}] {iss[1]}: {iss[2]}")
