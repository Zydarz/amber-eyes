import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p_vn = PK.parse_file('01_KICH_BAN/Tap07/kichban_tap07_23102026.md')
p_ja = PK.parse_file('01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md')
p_ko = PK.parse_file('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md')

def check_elem(eid):
    vn_e = next(e for e in p_vn if e['id'] == eid)
    ja_e = next(e for e in p_ja if e['id'] == eid)
    ko_e = next(e for e in p_ko if e['id'] == eid)
    print(f"\n================= {eid} =================")
    print(f"VN ({len(vn_e['sentences'])}):")
    for s in vn_e['sentences']:
        print("  ", s['id'], s['text'])
    print(f"JA ({len(ja_e['sentences'])}):")
    for s in ja_e['sentences']:
        print("  ", s['id'], s['text'])
    print(f"KO ({len(ko_e['sentences'])}):")
    for s in ko_e['sentences']:
        print("  ", s['id'], s['text'])

for eid in ['1.02', '2.08', '3.03', '3.05', '3.06', '4.08', '5.04']:
    check_elem(eid)
