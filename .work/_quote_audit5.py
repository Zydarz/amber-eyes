import io, re, glob, os, json

VIET_DIAC = set('ạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđĐăăâêôơưĂÂÊÔƠƯ')
EN_LEX = set(('the a an and or but if i you he she they we my your his her their our to of in on at for with '
              'not is are was were do does did can could will would shall should it its this that these those '
              'there here so just only want wanted know think me him us what how why when where who whom '
              'than then all any some one two more very too out up down about after before no yes have has '
              'had be been being am said says tell told take took make made give gave get got god lord '
              'save kill killed kills mother father family answer answers patients healthy life lives '
              'suffer suffering end watch steal stealing stealing stopped stop child children people '
              'person man woman girl boy always really anymore right wrong better worse help helped '
              'feel felt think thought keep kept put bring brought leave left find found pay paid '
              'buy bought sell sold meet met teach taught read write speak spoke listen heard '
              'thank thanks please sorry course sure lot lots bit much many little own same other '
              'another each every both few several own next last new old young great little long '
              'time times day days week month year world life man woman human mind heart mind '
              'study studies discover what makes like me we do did nothing everything something '
              'anything everything nothing place places').split())
HANG = re.compile(r'[\uac00-\ud7a3]')

VN_Q = re.compile(r"'([^']{2,})'")
KO_Q = re.compile(r"\u2018([^\u2019]{2,})\u2019")


def tokens(s):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", s)


def is_english(s):
    if any(ch in VIET_DIAC for ch in s):
        return False
    t = tokens(s.lower())
    hits = sum(1 for w in t if w in EN_LEX)
    return hits >= 2


SRC = {'01': 'Tap01/kichban_tap01_22102026_v2.md',
       '02': 'Tap02/kichban_tap02_22102026.md',
       '03': 'Tap03/kichban_tap03_22102026.md'}
for n in range(4, 30):
    SRC['%02d' % n] = 'Tap%02d/kichban_tap%02d_23102026.md' % (n, n)
vns = {k: '01_KICH_BAN/' + v for k, v in SRC.items()}

report = {}
for tap in sorted(vns):
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    if not os.path.exists(kp):
        continue
    vn = io.open(vns[tap], encoding='utf-8').read()
    ko = io.open(kp, encoding='utf-8').read()
    vq = VN_Q.findall(vn)
    kq = KO_Q.findall(ko)
    bad = []
    if len(vq) != len(kq):
        bad.append(('COUNT', 'VN=%d KO=%d' % (len(vq), len(kq)), '', ''))
    for i in range(min(len(vq), len(kq))):
        a, b = vq[i], kq[i]
        ven, ken = is_english(a), is_english(b)
        if ven != ken:
            bad.append(('TYPE' if ven else 'TYPE2', a, b, i + 1))
    if bad:
        report[tap] = bad
        print('===== Tap%s  (%d violations; VN=%d KO=%d pairs)' % (tap, len(bad), len(vq), len(kq)))
        for kind, a, b, i in bad:
            print('  [%s #%s] VN: %s' % (kind, i, a[:170]))
            print('        KO: %s' % b[:170])
print()
print('files with violations:', len(report), 'total:', sum(len(v) for v in report.values()))
json.dump({k: v for k, v in report.items()}, io.open('.work/_quote_violations.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
