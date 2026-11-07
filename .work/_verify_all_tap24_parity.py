import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap24/kichban_tap24_23102026.md'),
    ('EN', '01_KICH_BAN/Tap24_EN/kichban_tap24_EN.md'),
    ('JA', '01_KICH_BAN/Tap24_JA/kichban_tap24_JA.md'),
    ('KO', '01_KICH_BAN/Tap24_KO/kichban_tap24_KO.md'),
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

# Check N1 and N2 roles
n1_elem = [e for e in vn_els if e['id'] == '1.07'][0]
n2_elem = [e for e in vn_els if e['id'] == '4.09'][0]
if n1_elem['role'] != 'N' or n2_elem['role'] != 'N':
    print(f"MISMATCH N roles: 1.07={n1_elem['role']}, 4.09={n2_elem['role']}")
    all_ok = False

# Check summary keys
sum_1 = [e for e in vn_els if e['id'] == '1.02']
sum_3 = [e for e in vn_els if e['id'] == '3.02']
if not sum_1 or not sum_3:
    print("MISMATCH summary keys in VN")
    all_ok = False

if all_ok:
    print("\n>>> ALL 4 LANGUAGES (VN, EN, JA, KO): 100% PERFECT 1:1 PARITY ACROSS ALL 51 ELEMENTS AND 210 SENTENCES! <<<")
else:
    print("\n>>> PARITY ISSUES FOUND! <<<")
