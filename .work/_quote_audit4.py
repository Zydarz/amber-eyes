import io, re, glob, os

VIET_DIAC = set('ạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđĐăăâêôơưĂÂÊÔƠƯ')
STOP = set(('the a an and or but if i you he she they we my your his her their our to of in on at for with '
            'not is are was were do does did can could will would shall should it its this that these those '
            'there here so just only want wanted know think me him us what how why when where who than then '
            'all any some one two more very too out up down about after before no yes have has had be been '
            'being am whom whose said says tell told take took make made give gave get got').split())

VN_RE = re.compile(r"'([^']{2,})'|\u2018([^\u2019]{2,})\u2019")
KO_RE = re.compile(r"\u2018([^\u2019]{2,})\u2019")


def is_english(s):
    if any(ch in VIET_DIAC for ch in s):
        return False
    toks = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", s.lower())
    return sum(1 for w in toks if w in STOP) >= 2


def grab(rx, text):
    out = []
    for m in rx.finditer(text):
        out.append(m.group(1) if m.group(1) is not None else m.group(2))
    return out


vns = {}
for p in sorted(glob.glob('01_KICH_BAN/Tap[0-9][0-9]/kichban_tap*.md')):
    vns[re.search(r'Tap(\d+)', p).group(1)] = p

tot = 0
for tap in sorted(vns):
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    if not os.path.exists(kp):
        continue
    vn = io.open(vns[tap], encoding='utf-8').read()
    ko = io.open(kp, encoding='utf-8').read()
    vq = grab(VN_RE, vn)
    kq = grab(KO_RE, ko)
    if not vq and not kq:
        continue
    print('--- Tap%s: VN=%d KO=%d pairs' % (tap, len(vq), len(kq)))
    if len(vq) != len(kq):
        tot += abs(len(vq) - len(kq))
    for i in range(min(len(vq), len(kq))):
        a, b = vq[i], kq[i]
        ven, ken = is_english(a), is_english(b)
        if ven != ken:
            tot += 1
            tag = 'VN=EN  -> KO phải giữ tiếng Anh' if ven else 'VN=dịch -> KO phải dịch ra Hán'
            print('   pair#%d %s' % (i + 1, tag))
            print('      VN:', a[:150])
            print('      KO:', b[:150])
print()
print('TOTAL quote-type problems:', tot)
