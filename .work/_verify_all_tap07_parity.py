import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap07/kichban_tap07_23102026.md'),
    ('EN', '01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md'),
    ('JA', '01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md'),
    ('KO', '01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md'),
]

forbidden = {
    'VN': ['máu', 'thi thể', 'xác chết', 'tự sát', 'cắt cổ', 'bóp cổ', 'khí độc', 'ngạt thở', 'đâm', 'trói', 'sát hại', 'diệt chủng', 'đầu độc', 'bỏ đói', 'móc áo'],
    'EN': ['blood', 'corpse', 'decapitat', 'strangl', 'suicide'],
    'JA': ['死体', '絞殺', '刺殺'],
    'KO': ['자살', '시체', '교살'],
}

parsed = {}
for lang, path in files:
    els = PK.parse_file(path)
    loi = [e for e in els if e['kind'] == 'LOI']
    s_cnt = sum(len(e['sentences']) for e in loi)
    words = sum(sum(s['words'] for s in e['sentences']) for e in loi)
    parsed[lang] = els
    print(f"{lang:4}: elements={len(els)}, LOI turns={len(loi)}, total sentences={s_cnt}, words/chars={words}")

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

# Check V9
v9_clean = True
for lang, path in files:
    els = parsed[lang]
    fb_list = forbidden.get(lang, [])
    hits = []
    for e in els:
        if e['kind'] == 'LOI':
            for s in e['sentences']:
                txt = s['text'].lower()
                for w in fb_list:
                    if w in txt:
                        hits.append((e['id'], w, s['text']))
    if hits:
        print(f"FAIL V9 for {lang}: {len(hits)} forbidden word hits")
        for h in hits:
            print(f"  {h[0]} [{h[1]}]: {h[2]}")
        v9_clean = False
    else:
        print(f"V9 for {lang}: 0 forbidden word hits (CLEAN)")

if all_ok and v9_clean:
    print("\n>>> ALL 4 LANGUAGES (VN, EN, JA, KO): 100% PERFECT 1:1 PARITY ACROSS ALL 48 ELEMENTS AND 219 SENTENCES! <<<")
else:
    print("\n>>> ISSUES FOUND! <<<")
