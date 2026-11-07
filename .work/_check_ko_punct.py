# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md')
loi = [e for e in p if e['kind'] == 'LOI']

issues = []
for e in loi:
    for s in e['sentences']:
        txt = s['text']
        sid = s['id']
        # space before punct
        if re.search(r'\s+[,.?!]', txt):
            issues.append((sid, "Space before punct", txt))
        # double space
        if '  ' in txt:
            issues.append((sid, "Double space", txt))
        # missing space after dot/comma
        m_dot = re.search(r'([가-힣a-zA-Z0-9])([.?!])([가-힣a-zA-Z])', txt)
        if m_dot:
            issues.append((sid, f"Missing space after punct '{m_dot.group()}'", txt))
            
print(f"KO issues found: {len(issues)}")
for iss in issues:
    print(f"[{iss[0]}] {iss[1]}: {iss[2]}")
