# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

for ep in ['01', '02', '07', '08']:
    path = f'01_KICH_BAN/Tap{ep}/kichban_tap{ep}_23102026.md'
    try:
        p = PK.parse_file(path)
        loi = [e for e in p if e['kind'] == 'LOI']
        sentences = sum(len(e['sentences']) for e in loi)
        print(f"Tap {ep}: {len(p)} elements, {len(loi)} LOI, {sentences} sentences")
    except Exception as ex:
        print(f"Tap {ep}: Error {ex}")
