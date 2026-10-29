import io, re
for tap, f in [('29', '01_KICH_BAN/Tap29/kichban_tap29_23102026.md'),
               ('04', '01_KICH_BAN/Tap04/kichban_tap04_23102026.md'),
               ('07', '01_KICH_BAN/Tap07/kichban_tap07_23102026.md')]:
    t = io.open(f, encoding='utf-8').read()
    sq = re.findall(r"'([^']{2,})'", t)
    cq = re.findall(r'\u2018([^\u2019]{2,})\u2019', t)
    dq = re.findall(r'"([^"]{2,})"', t)
    print('Tap%s raw: straight=%d curly=%d double=%d' % (tap, len(sq), len(cq), len(dq)))
    for x in sq[:4]:
        print('    SQ:', x[:110].replace('\n', ' '))
