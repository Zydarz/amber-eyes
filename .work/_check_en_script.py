import sys
sys.path.insert(0, '.work')
sys.stdout.reconfigure(encoding='utf-8')
import parse_kichban
import re

res = parse_kichban.parse_file('01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md')

issues = []
for elem in res:
    eid = elem.get('id', '')
    sents = elem.get('sentences', [])
    for s in sents:
        sid = s.get('id', '')
        txt = s.get('text', '')
        
        # Check double spaces
        if '  ' in txt:
            issues.append((sid, 'Double space', txt))
        # Check space before punctuation
        if re.search(r'\s+[,.:;?!]', txt):
            issues.append((sid, 'Space before punctuation', txt))
        # Check unmatched quotes
        if txt.count('“') != txt.count('”'):
            issues.append((sid, 'Mismatched curly quotes', txt))
        if txt.count('"') % 2 != 0:
            issues.append((sid, 'Mismatched straight quotes', txt))
        # Check repeated words
        m = re.findall(r'\b([a-zA-Z]+)\s+\1\b', txt, re.IGNORECASE)
        if m:
            if m[0].lower() not in ('that', 'had'):
                issues.append((sid, f'Repeated word {m}', txt))
        # Check if starts with lowercase
        first_char = txt.strip('“"\'')[0] if txt.strip('“"\'') else ''
        if first_char.islower():
            issues.append((sid, 'Starts with lowercase', txt))
        # Check if ends with punctuation
        if not txt.endswith(('.', '!', '?', '”', '"')):
            issues.append((sid, 'Does not end with terminal punctuation', txt))

print(f'Total issues in EN script: {len(issues)}')
for sid, err, txt in issues:
    print(f'[{sid}] {err}: {txt}')
