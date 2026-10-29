import json, sys
sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('.work/script_tap05.json', encoding='utf-8'))
for x in data:
    if 'pause' in str(x).lower() or x.get('kind') not in ('LOI', 'BGM', 'SFX'):
        print(x)
