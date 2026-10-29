import io, re, glob, os, sys

LAT = re.compile(r'[A-Za-z]')
Q = re.compile(r'\u201c([^\u201d]{2,})\u201d')

sys.path.insert(0, '.work')
import parse_kichban as pk

vns = {}
for p in sorted(glob.glob('01_KICH_BAN/Tap[0-9][0-9]/kichban_tap*.md')):
    vns[re.search(r'Tap(\d+)', p).group(1)] = p

bad = 0
for tap in sorted(vns):
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    if not os.path.exists(kp):
        continue
    ve = pk.parse_file(vns[tap])
    ke = pk.parse_file(kp)
    if len(ve) != len(ke):
        print('Tap%s: element count differs, skip' % tap)
        continue
    for a, b in zip(ve, ke):
        vq = Q.findall(a.get('text', ''))
        kq = Q.findall(b.get('text', ''))
        if len(vq) != len(kq):
            bad += 1
            print('Tap%s %s: quote count VN=%d KO=%d  <<< FIX' % (tap, a['id'], len(vq), len(kq)))
            for x in vq:
                print('    VN:', x[:130])
            for x in kq:
                print('    KO:', x[:130])
            continue
        for i, (x, y) in enumerate(zip(vq, kq), 1):
            v1, k1 = bool(LAT.search(x)), bool(LAT.search(y))
            if v1 != k1:
                bad += 1
                print('Tap%s %s quote#%d: %s' % (tap, a['id'], i,
                      'VN=EN -> KO must keep English' if v1 else 'VN=translated -> KO must be Korean'))
                print('    VN:', x[:150])
                print('    KO:', y[:150])
print()
print('TOTAL quote-type problems:', bad)
