import io, re, os

SRC = {'01': 'Tap01/kichban_tap01_22102026_v2.md',
       '02': 'Tap02/kichban_tap02_22102026.md',
       '03': 'Tap03/kichban_tap03_22102026.md'}
for n in range(4, 30):
    SRC['%02d' % n] = 'Tap%02d/kichban_tap%02d_23102026.md' % (n, n)

EN = {k: '01_KICH_BAN/Tap%s_EN/kichban_tap%s_EN.md' % (k, k) for k in SRC}

VIET_DIAC = set('ạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđĐăăâêôơưĂÂÊÔƠƯ')
EN_LEX = set(('the a an and or but if i you he she they we my your his her their our to of in on at for with '
              'not is are was were do does did can could will would shall should it its this that these those '
              'there here so just only want wanted know think me him us what how why when where who whom '
              'than then all any some one two more very too out up down about after before no yes have has '
              'had be been being am said says tell told take took make made give gave get got god lord '
              'save kill killed kills mother father family answer answers patients healthy life lives '
              'suffer suffering end watch steal stealing stopped stop child children people person man '
              'woman girl boy always really anymore right wrong better worse help helped feel felt '
              'think thought keep kept put bring brought leave left find found pay paid buy bought sell '
              'sold meet met teach taught read write speak spoke listen heard thank thanks please sorry '
              'course sure lot lots bit much many little own same other another each every both few several '
              'next last new old young great long time times day days week month year world mind heart '
              'study studies discover what makes like me we do did nothing everything something anything '
              'place places').split())

VN_Q = re.compile(r"'([^']{2,})'")
KO_Q = re.compile(r"\u2018([^\u2019]{2,})\u2019")


def is_english(s):
    if any(ch in VIET_DIAC for ch in s):
        return False
    return sum(1 for w in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", s.lower()) if w in EN_LEX) >= 2


def norm(s):
    return re.sub(r'[^a-z0-9 ]+', '', s.lower()).strip()


for tap in sorted(SRC):
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    ep = EN[tap]
    if not os.path.exists(kp) or not os.path.exists(ep):
        continue
    vn = io.open('01_KICH_BAN/' + SRC[tap], encoding='utf-8').read()
    ko = io.open(kp, encoding='utf-8').read()
    en = io.open(ep, encoding='utf-8').read()
    en_norm = norm(en)
    vq = VN_Q.findall(vn)
    kq = KO_Q.findall(ko)
    for i in range(min(len(vq), len(kq))):
        a, b = vq[i], kq[i]
        if is_english(a):
            continue          # type-1 rõ ràng: VN đã tiếng Anh -> giữ tiếng Anh
        if not is_english(b):
            continue          # KO đã dịch -> đúng
        # VN tiếng Việt, KO tiếng Anh -> kiểm tra EN: EN giữ tiếng Anh (type-1) hay EN dịch (type-2)
        en_has = norm(b) in en_norm
        tag = 'EN giữ tiếng Anh -> TYPE-1, KO OK' if en_has else 'EN đã dịch -> TYPE-2, cần dịch sang Hán <<< FIX'
        print('Tap%s #%d: %s' % (tap, i + 1, tag))
        print('    VN:', a[:130])
        print('    KO:', b[:130])
