import json, sys
sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('.work/script_tap05.json', encoding='utf-8'))
for x in data:
    if x['id'] in ('4.12', '4.13', '4.14', '4.15'):
        print(x['id'], x.get('kind'), x.get('text', '') or x.get('desc', ''))
