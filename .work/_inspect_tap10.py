import sys
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
for e in p:
    if e['kind'] == 'LOI':
        print(f"{e['id']} | Act {e['act']} | Role {e['role']} | {len(e['sentences'])} sents | {e['sentences'][0]['text'][:40]}")
    else:
        desc = str(e.get('desc', '') or e.get('sec', ''))[:40]
        print(f"{e['id']} | Act {e['act']} | {e['kind']} | {desc}")
