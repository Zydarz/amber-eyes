import sys
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap11/kichban_tap11_23102026.md')
for el in p:
    eid = el.get('id')
    kind = el.get('kind')
    role = el.get('role', '')
    sents = len(el.get('sentences', []))
    print(f"{eid} | kind={kind:4s} | role={role:2s} | sents={sents:2d}")
