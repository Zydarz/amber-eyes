import io, re

t = io.open('01_KICH_BAN/Tap04/kichban_tap04_23102026.md', encoding='utf-8').read()
sq = re.findall(r"'([^']{6,})'", t)
print('VN Tap04 straight-quote pairs:', len(sq))
for q in sq[:14]:
    print('  *', q[:160].replace('\n', ' '))

print()
print('--- QC quote logic ---')
s = io.open('.work/_qc_ko_parity.py', encoding='utf-8').read()
for i, l in enumerate(s.split('\n'), 1):
    if 'quote' in l.lower() or '\u2018' in l or '\u2019' in l:
        print('%4d: %s' % (i, l.rstrip()))
