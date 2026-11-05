# -*- coding: utf-8 -*-
"""So sánh cấu trúc câu của 4 bản tập 2 (VN/EN/JA/KO) sau khi viết lại 05/11."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_kichban import parse_file

BASE = r'D:/TEST/Gax/amber-eyes'
FILES = {
    'VN': BASE + r'/01_KICH_BAN/Tap02/kichban_tap02_22102026.md',
    'EN': BASE + r'/01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md',
    'JA': BASE + r'/01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md',
    'KO': BASE + r'/01_KICH_BAN/Tap02_KO/kichban_tap02_KO.md',
}

data = {}
for lang, path in FILES.items():
    els = parse_file(path)
    data[lang] = els
    loi = [e for e in els if e['kind'] == 'LOI']
    nghi = [e for e in els if e['kind'] == 'NGHI']
    sfx = [e for e in els if e['kind'] in ('SFX', 'BGM')]
    ns = sum(len(e['sentences']) for e in loi)
    print(f'{lang}: element={len(els)} LOI={len(loi)} NGHI={len(nghi)} SFX/BGM={len(sfx)} cau={ns}')

# đối chiếu theo index element LOI
print('\n=== So sánh số câu từng element LOI (theo thứ tự) ===')
langs = ['VN', 'EN', 'JA', 'KO']
loi = {k: [e for e in v if e['kind'] == 'LOI'] for k, v in data.items()}
n = len(loi['VN'])
for k in langs:
    print(f'{k}: so element LOI = {len(loi[k])}')
maxn = max(len(loi[k]) for k in langs)
diff = 0
for i in range(maxn):
    row = []
    for k in langs:
        if i < len(loi[k]):
            row.append((loi[k][i]['id'], len(loi[k][i]['sentences'])))
        else:
            row.append(('-', 0))
    counts = {c for _, c in row}
    if len(counts) > 1:
        diff += 1
        print(f'  idx {i}: ' + ' | '.join(f'{k}={v[0]}({v[1]})' for k, v in zip(langs, row)))
print(f'\nTong so element LOI khac nhau giua 4 ban: {diff}/{maxn}')

# id element: so id VN vs EN
print('\n=== Mapping id: VN -> EN/JA/KO (theo index) ===')
bad = 0
for i in range(min(len(loi['VN']), len(loi['EN']))):
    ids = [loi[k][i]['id'] for k in langs if i < len(loi[k])]
    if len(set(ids)) > 1:
        bad += 1
        if bad <= 25:
            print(f'  idx {i}: ' + ' '.join(ids))
print(f'  element co id khac nhau: {bad}')

# lưu json đã parse
for k, v in data.items():
    out = BASE + f'/.work/script_tap02_{k}.json'
    json.dump(v, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'wrote {out}')
