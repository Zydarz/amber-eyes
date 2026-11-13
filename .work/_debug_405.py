# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p_ja = PK.parse_file('01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md')
p_ko = PK.parse_file('01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md')

ja_405 = next(e for e in p_ja if e['id'] == '4.05')
print(f"JA 4.05 ({len(ja_405['sentences'])}):")
for i, s in enumerate(ja_405['sentences']):
    print(f"  {i+1}: {s['text']}")

ko_405 = next(e for e in p_ko if e['id'] == '4.05')
print(f"\nKO 4.05 ({len(ko_405['sentences'])}):")
for i, s in enumerate(ko_405['sentences']):
    print(f"  {i+1}: {s['text']}")
