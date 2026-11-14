# -*- coding: utf-8 -*-
"""Script to apply in-depth psychological expansions to Tap 16 in VN, EN, JA, and KO."""
import re, sys, io
sys.path.insert(0, '.work')
import parse_kichban as PK

# Check before state
files = {
    'VN': '01_KICH_BAN/Tap16/kichban_tap16_23102026.md',
    'EN_main': '01_KICH_BAN/Tap16/kichban_tap16_EN.md',
    'EN_sub': '01_KICH_BAN/Tap16_EN/kichban_tap16_EN.md',
    'JA': '01_KICH_BAN/Tap16_JA/kichban_tap16_JA.md',
    'KO': '01_KICH_BAN/Tap16_KO/kichban_tap16_KO.md',
}

for k, p in files.items():
    parsed = PK.parse_file(p)
    loi = [e for e in parsed if e['kind'] == 'LOI']
    sentences = sum(len(x.get('sentences', [])) for x in loi)
    print(f"{k} before: {len(parsed)} elements, {sentences} sentences")
