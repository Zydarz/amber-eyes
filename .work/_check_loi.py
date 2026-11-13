import sys
sys.path.insert(0, '.work')
import parse_kichban as PK
vn = PK.parse_file('01_KICH_BAN/Tap11/kichban_tap11_23102026.md')
for el in vn:
    if el['kind'] == 'LOI':
        print(f"{el['id']}: role={el['role']} sents={len(el['sentences'])}")
