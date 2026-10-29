import io, re, glob, os

LAT = re.compile(r'[A-Za-z]')
HANG = re.compile(r'[\uac00-\ud7a3]')
VN_Q = re.compile(r"'([^']{2,})'")
KO_Q = re.compile(r"\u2018([^\u2019]{2,})\u2019")

vns = {}
for p in sorted(glob.glob('01_KICH_BAN/Tap[0-9][0-9]/kichban_tap*.md')):
    vns[re.search(r'Tap(\d+)', p).group(1)] = p

total_bad = 0
for tap in sorted(vns):
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    if not os.path.exists(kp):
        continue
    vn = io.open(vns[tap], encoding='utf-8').read()
    ko = io.open(kp, encoding='utf-8').read()
    vq = VN_Q.findall(vn)
    kq = KO_Q.findall(ko)
    if not vq:
        continue
    print('===== Tap%s  (%d pairs)' % (tap, len(vq)))
    for i, (a, b) in enumerate(zip(vq, kq), 1):
        v1 = bool(LAT.search(a))
        k1 = bool(LAT.search(b))
        if v1 != k1:
            total_bad += 1
            kind = 'TYPE1(VN=EN) KO=KO <<< FIX' if v1 else 'TYPE2(VN=ko) KO=EN <<< FIX'
            print('  [%2d] %s' % (i, kind))
            print('      VN: %s' % a[:150].replace('\n', ' '))
            print('      KO: %s' % b[:150].replace('\n', ' '))
print()
print('TOTAL mismatched pairs:', total_bad)
