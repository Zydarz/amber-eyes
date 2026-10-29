import io, re

vn = io.open('01_KICH_BAN/Tap04/kichban_tap04_23102026.md', encoding='utf-8').read()
ko = io.open('01_KICH_BAN/Tap04_KO/kichban_tap04_KO.md', encoding='utf-8').read()

print('VN contains latin words:')
for w in ['suffering', 'torment', 'watch', 'stealing', 'endless', 'Charlie']:
    print('  %-12s VN=%d  KO=%d' % (w, len(re.findall(r'\b' + w + r'\b', vn)),
                                   len(re.findall(r'\b' + w + r'\b', ko))))

print()
print('--- KO quotes that contain latin (Tap04) ---')
for i, q in enumerate(re.findall(r'\u2018([^\u2019]{2,})\u2019', ko)):
    if re.search(r'[A-Za-z]', q):
        print(' %2d: %s' % (i, q[:180]))

print()
print('--- matching VN context for the Cullen confession ---')
for m in re.finditer(r'[^.]{0,140}(khổ đau|đau đớn)[^.]{0,140}\.', vn):
    s = m.group(0).strip()
    if 'chỉ muốn' in s or 'kết thúc' in s:
        print(' *', s.replace('\n', ' ')[:300])
        break
