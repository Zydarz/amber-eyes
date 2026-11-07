import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('.work/script_tap10.json', encoding='utf-8'))
sents = [s['text'] for e in d if e.get('kind') == 'LOI' for s in e.get('sentences', [])]
q = [s for s in sents if '“' in s or '”' in s or "'" in s]
print('Total sentences:', len(sents), 'Sentences with quotes:', len(q))
roles = {}
for e in d:
    if e.get('kind') == 'LOI':
        r = e.get('role')
        roles[r] = roles.get(r, 0) + len(e.get('sentences', []))
print('Role counts:', roles)
