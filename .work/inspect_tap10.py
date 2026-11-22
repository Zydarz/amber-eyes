import json

with open('.work/tap10_test.json', 'r', encoding='utf-8') as f:
    els = json.load(f)

for e in els:
    if e['kind'] == 'LOI':
        print(f"{e['id']}: role={e['role']}, sentences={len(e['sentences'])}, direction={e.get('direction', '')}")
    else:
        print(f"{e['id']}: kind={e['kind']}, desc={e.get('desc', '')[:30]}")
