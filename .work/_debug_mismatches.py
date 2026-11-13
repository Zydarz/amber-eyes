# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p_vn = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
p_en = PK.parse_file('01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md')
p_ja = PK.parse_file('01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md')
p_ko = PK.parse_file('01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md')

def compare_el(el_id):
    vn_el = next(e for e in p_vn if e['id'] == el_id)
    en_el = next(e for e in p_en if e['id'] == el_id)
    ja_el = next(e for e in p_ja if e['id'] == el_id)
    ko_el = next(e for e in p_ko if e['id'] == el_id)
    print(f"\n=== ELEMENT {el_id} ===")
    print(f"VN ({len(vn_el['sentences'])}):")
    for i, s in enumerate(vn_el['sentences']):
        print(f"  {i+1}: {s['text']}")
    print(f"EN ({len(en_el['sentences'])}):")
    for i, s in enumerate(en_el['sentences']):
        print(f"  {i+1}: {s['text']}")
    print(f"JA ({len(ja_el['sentences'])}):")
    for i, s in enumerate(ja_el['sentences']):
        print(f"  {i+1}: {s['text']}")
    print(f"KO ({len(ko_el['sentences'])}):")
    for i, s in enumerate(ko_el['sentences']):
        print(f"  {i+1}: {s['text']}")

compare_el('3.08')
compare_el('4.05')
compare_el('4.09')
