import io, re

def show(tap, src, pairs):
    kl = io.open('01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap), encoding='utf-8').read().split('\n')
    vl = io.open(src, encoding='utf-8').read().split('\n')
    print('########## Tap%s' % tap)
    for ln, needles in pairs:
        ko = kl[ln - 1]
        print('  KO %4d: %s' % (ln, ko))
        for j, vv in enumerate(vl):
            low = vv.lower()
            if any(n.lower() in low for n in needles):
                print('    VN %4d: %s' % (j + 1, vv[:300]))
        print()

show('03', '01_KICH_BAN/Tap03/kichban_tap03_22102026.md',
     [(189, ['Cục', 'FBI', 'Ressler']), (257, ['had', 'đã', 'mang', 'giải thưởng'])])
show('05', '01_KICH_BAN/Tap05/kichban_tap05_23102026.md',
     [(104, ['Lutheran', 'Giáo', 'nhà thờ']), (188, ['Lutheran', 'Company', 'Công ty']),
      (193, ['Lutheran', 'Wichita'])])
show('06', '01_KICH_BAN/Tap06/kichban_tap06_23102026.md',
     [(188, ['gọi là', 'Called', 'quái vật', 'Monster', 'They'])])
show('01', '01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md',
     [(31, ['Volunteer', 'North'])])
