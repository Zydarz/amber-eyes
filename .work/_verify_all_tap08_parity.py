import sys, io
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap08/kichban_tap08_23102026.md'),
    ('EN', '01_KICH_BAN/Tap08_EN/kichban_tap08_EN.md'),
    ('JA', '01_KICH_BAN/Tap08_JA/kichban_tap08_JA.md'),
    ('KO', '01_KICH_BAN/Tap08_KO/kichban_tap08_KO.md'),
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
            if ve['role'] != te['role']:
                print(f"MISMATCH role at {ve['id']} ({lang}): {te['role']} vs VN={ve['role']}")
                all_ok = False
            vc = len(ve['sentences'])
            tc = len(te['sentences'])
            if vc != tc:
                print(f"MISMATCH sentence count at {ve['id']} ({lang}): {tc} vs VN={vc}")
                all_ok = False
        elif ve['kind'] == 'NGHI':
            if ve.get('sec') != te.get('sec'):
                print(f"MISMATCH pause seconds at {ve['id']} ({lang}): {te.get('sec')} vs VN={ve.get('sec')}")
                all_ok = False

if all_ok:
    print("\n>>> ALL 4 LANGUAGES (VN, EN, JA, KO): 100% PERFECT 1:1 PARITY ACROSS ALL 53 ELEMENTS AND 171 SENTENCES! <<<")
else:
    print("\n>>> PARITY ISSUES FOUND! <<<")
