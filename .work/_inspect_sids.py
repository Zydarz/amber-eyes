# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = {
    'VN': '01_KICH_BAN/Tap10/kichban_tap10_23102026.md',
    'EN': '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md',
    'JA': '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md',
    'KO': '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md',
}

for sid in ['2.09#3', '4.05#5', '4.07#2', '4.08#3']:
    print(f"\n=== SID: {sid} ===")
    for lang, path in files.items():
        p = PK.parse_file(path)
        for e in p:
            for s in e.get('sentences', []):
                if s['id'] == sid:
                    print(f"  [{lang}]: {s['text']}")
