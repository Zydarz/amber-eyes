import io, re, os

SRC = {'01': 'Tap01/kichban_tap01_22102026_v2.md',
       '02': 'Tap02/kichban_tap02_22102026.md',
       '03': 'Tap03/kichban_tap03_22102026.md'}
for n in range(4, 30):
    SRC['%02d' % n] = 'Tap%02d/kichban_tap%02d_23102026.md' % (n, n)

HANG = re.compile(r'[\uac00-\ud7a3]')
Q = re.compile(r'\u2018([^\u2019]{2,300})\u2019')
LAT = re.compile(r'[A-Za-z]{2,}')


def gloss_ok(line, m):
    """Hangul phải tồn tại NGOÀI dấu nháy."""
    before = line[:m.start()]
    after = line[m.end():]
    return bool(HANG.search(before) or HANG.search(after))


for tap in sorted(SRC):
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    if not os.path.exists(kp):
        continue
    lines = io.open(kp, encoding='utf-8').read().split('\n')
    hits = []
    for i, l in enumerate(lines, 1):
        for m in Q.finditer(l):
            content = m.group(1)
            if len(LAT.findall(content)) < 2:
                continue  # không phải quote tiếng Anh
            if not gloss_ok(l, m):
                hits.append((i, content))
    if hits:
        print('===== Tap%s: %d quote tiếng Anh thiếu nghĩa Hàn NGOÀI ngoặc' % (tap, len(hits)))
        for i, c in hits:
            print('   line %4d: %s' % (i, c[:160]))
