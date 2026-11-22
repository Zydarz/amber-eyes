import json

with open('.work/tap10_test.json', 'r', encoding='utf-8') as f:
    els = json.load(f)

loi_els = [e for e in els if e['kind'] == 'LOI']
print('Total LOI elements:', len(loi_els))
counts = [len(e['sentences']) for e in loi_els]
print('Counts:', counts)
print('Sum:', sum(counts))
