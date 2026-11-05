import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap07/kichban_tap07_23102026.md'),
    ('EN', '01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md'),
    ('JA', '01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md'),
    ('KO', '01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md'),
]

parsed = {}
for lang, path in files:
    els = PK.parse_file(path)
    loi = [e for e in els if e['kind'] == 'LOI']
    s_cnt = sum(len(e['sentences']) for e in loi)
    parsed[lang] = els
    print(f"{lang:4}: elements={len(els)}, LOI turns={len(loi)}, total sentences={s_cnt}")

# Check parity turn-by-turn
vn_els = parsed['VN']
all_ok = True
for lang in ['EN', 'JA', 'KO']:
    target_els = parsed[lang]
    if len(target_els) != len(vn_els):
        print(f"MISMATCH element count {lang}: {len(target_els)} vs {len(vn_els)}")
        all_ok = False
        continue
    for i, (ve, te) in enumerate(zip(vn_els, target_els)):
        if ve['kind'] != te['kind']:
            print(f"MISMATCH kind at index {i} ({ve['id']}): {lang}={te['kind']} vs VN={ve['kind']}")
            all_ok = False
        if ve['kind'] == 'LOI':
            vc = len(ve['sentences'])
            tc = len(te['sentences'])
            if vc != tc:
                print(f"MISMATCH sentence count at {ve['id']} ({lang}): {tc} vs VN={vc}")
                all_ok = False

if all_ok:
    print("\n>>> ALL 4 LANGUAGES: 100% PERFECT 1:1 PARITY ACROSS ALL ELEMENTS AND SENTENCES! <<<")
else:
    print("\n>>> PARITY ISSUES FOUND! <<<")
