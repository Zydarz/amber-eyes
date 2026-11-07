# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = {
    'VN': '01_KICH_BAN/Tap10/kichban_tap10_23102026.md',
    'EN': '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md',
    'JA': '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md',
    'KO': '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md',
}

for lang, path in files.items():
    print(f"\n=================== QUOTES IN {lang} ===================")
    p = PK.parse_file(path)
    loi = [e for e in p if e['kind'] == 'LOI']
    for e in loi:
        for s in e['sentences']:
            txt = s['text']
            if any(q in txt for q in ['“', '”', '「', '」', '『', '』']):
                print(f"[{s['id']}] {txt}")
