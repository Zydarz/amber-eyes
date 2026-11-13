import sys
sys.path.insert(0, '.work')
import parse_kichban as PK

vn = PK.parse_file('01_KICH_BAN/Tap11/kichban_tap11_23102026.md')
en = PK.parse_file('01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md')

for i in range(max(len(vn), len(en))):
    v = vn[i] if i < len(vn) else {}
    e = en[i] if i < len(en) else {}
    vid, eid = v.get('id'), e.get('id')
    vs, es = len(v.get('sentences', [])), len(e.get('sentences', []))
    if vid != eid or vs != es or v.get('kind') != e.get('kind') or v.get('role') != e.get('role'):
        print(f"MISMATCH at idx {i}: VN[{vid}] kind={v.get('kind')} role={v.get('role')} sents={vs} vs EN[{eid}] kind={e.get('kind')} role={e.get('role')} sents={es}")
