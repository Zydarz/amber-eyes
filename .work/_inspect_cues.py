import json, sys
sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('.work/script_tap05.json', encoding='utf-8'))
for x in data:
    kind = x.get('kind')
    if kind in ('BGM', 'SFX', 'PAUSE'):
        t = x.get('text', '') or x.get('desc', '')
        dur = x.get('duration_s', '')
        print(f"{x.get('id'):<6} | {kind:<5} | {dur:<4} | {t}")
