import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open(Path(__file__).resolve().parent / 'script_tap05.json', encoding='utf-8'))
lois = [x for x in data if x.get('kind') == 'LOI']
print(f"Total LOI blocks: {len(lois)}")
for x in lois:
    s = x['sentences']
    print(f"Hoi {x['act']} | Block {x['id']:<5} | Vai: {x['role']:<2} | {len(s):>2} cau | {s[0]['id']:<7} -> {s[-1]['id']:<7} | {s[0]['text'][:60]}")
