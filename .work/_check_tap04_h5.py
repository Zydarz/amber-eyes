import json, sys
sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('.work/script_tap04.json', encoding='utf-8'))
for x in data:
    if x['act'] == 5 and x['id'] in ('5.01', '5.02', '5.03'):
        print(x['id'], x.get('kind'), x.get('desc', '') or x.get('text', '')[:40])
