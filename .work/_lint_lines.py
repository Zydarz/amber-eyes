import io, re, os

SRC = {'01': 'Tap01/kichban_tap01_22102026_v2.md',
       '02': 'Tap02/kichban_tap02_22102026.md',
       '03': 'Tap03/kichban_tap03_22102026.md'}
for n in range(4, 30):
    SRC['%02d' % n] = 'Tap%02d/kichban_tap%02d_23102026.md' % (n, n)

TOK = {'01': ['North'], '02': ['DNA', 'Flags', 'Red'], '03': ['Bureau', 'had'],
       '05': ['Church', 'DNA'], '06': ['Called', 'First', 'Lady', 'Monster', 'They'],
       '09': ['White', 'bonding', 'trauma'], '10': ['Deprivation', 'Extreme', 'Sensory', 'Syndrome'],
       '24': ['DNA']}

for tap, toks in TOK.items():
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    vp = '01_KICH_BAN/' + SRC[tap]
    if not os.path.exists(kp):
        continue
    kl = io.open(kp, encoding='utf-8').read().split('\n')
    vl = io.open(vp, encoding='utf-8').read().split('\n')
    print('########## Tap%s' % tap)
    for i, l in enumerate(kl, 1):
        hit = [t for t in toks if re.search(r'(?<![A-Za-z])' + re.escape(t) + r'(?![A-Za-z])', l)]
        if not hit:
            continue
        print('  KO %4d [%s] %s' % (i, ','.join(hit), l.strip()[:200]))
        # dòng VN gần nhất có chứa các token tương ứng (không dấu)
        plain = {t.lower() for t in hit}
        for j in range(max(0, i - 6), min(len(vl), i + 2)):
            vv = vl[j]
            low = re.sub(r'[^A-Za-z]', '', vv).lower()
            if any(t in low for t in plain):
                print('      VN %4d %s' % (j + 1, vv.strip()[:200]))
                break
