import io, re, glob, os

RE = re.compile(r'\u2018(.*?)\u2019', re.S)
LAT = re.compile(r'[A-Za-z]')
HANG = re.compile(r'[\uac00-\ud7a3]')
VIET = re.compile(r'[\u00c0-\u1ef9]')

vns = {}
for p in sorted(glob.glob('01_KICH_BAN/Tap[0-9][0-9]/kichban_tap*.md')):
    tap = re.search(r'Tap(\d+)', p).group(1)
    vns[tap] = p

print('tap | VNpairs type1(latin) type2(other) || KOpairs type1(latin) type2(hangul) ko_lat_in_quotes')
for tap in sorted(vns):
    vn = io.open(vns[tap], encoding='utf-8').read()
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    if not os.path.exists(kp):
        print('%s | (no KO file)' % tap)
        continue
    ko = io.open(kp, encoding='utf-8').read()
    vq = RE.findall(vn)
    kq = RE.findall(ko)
    v1 = sum(1 for q in vq if LAT.search(q))
    v2 = len(vq) - v1
    k1 = sum(1 for q in kq if LAT.search(q))
    k2 = sum(1 for q in kq if HANG.search(q))
    # English-looking whole phrase inside KO quotes (>=3 latin words)
    eng = sum(1 for q in kq if len(re.findall(r"[A-Za-z]{2,}", q)) >= 3)
    print('%s | %3d  %3d %3d || %3d %3d %3d   eng_phrases=%d' % (tap, len(vq), v1, v2, len(kq), k1, k2, eng))
