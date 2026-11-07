# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md')
loi = [e for e in p if e['kind'] == 'LOI']

issues = []
for e in loi:
    for s in e['sentences']:
        txt = s['text']
        sid = s['id']
        # Check if western comma ',' or western period '.' exists between Japanese characters
        m_comma = re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF],', txt)
        if m_comma:
            issues.append((sid, f"Western comma after JA character: '{m_comma.group()}'", txt))
        m_dot = re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]\.(?!\d)', txt)
        if m_dot:
            issues.append((sid, f"Western dot after JA character: '{m_dot.group()}'", txt))

print(f"JA issues found: {len(issues)}")
for iss in issues:
    print(f"[{iss[0]}] {iss[1]}: {iss[2]}")
