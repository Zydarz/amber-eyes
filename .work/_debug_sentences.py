# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap11/kichban_tap11_23102026.md'),
    ('EN', '01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md'),
    ('JA', '01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md'),
    ('KO', '01_KICH_BAN/Tap11_KO/kichban_tap11_KO.md'),
]

eids = ['2.04', '2.09', '4.04', '4.08', '5.07', '5.09']

for lang, f in files:
    parsed = {e['id']: e for e in PK.parse_file(f)}
    print(f"\n=== {lang} ===")
    for eid in eids:
        sents = parsed[eid].get('sentences', [])
        print(f"{eid} has {len(sents)} sentences:")
        for s in sents:
            print(f"  [{s['id']}] {s['text']}")
