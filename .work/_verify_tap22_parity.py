# -*- coding: utf-8 -*-
import json

files = {
    'VN': '.work/script_tap22.json',
    'EN': '.work/script_tap22_EN.json',
    'JA': '.work/script_tap22_JA.json',
    'KO': '.work/script_tap22_KO.json',
}

data = {k: json.load(open(v, encoding='utf-8')) for k, v in files.items()}

mismatches = []
for i in range(len(data['VN'])):
    el_id = data['VN'][i]['id']
    counts = {k: len(data[k][i].get('sentences', [])) for k in files}
    if len(set(counts.values())) > 1:
        mismatches.append((i, el_id, counts))

print("Total elements:", len(data['VN']))
print("Mismatches across 4 languages:", len(mismatches))
if mismatches:
    for m in mismatches:
        print(" ", m)
else:
    print("PERFECT PARITY! Every single element has identical sentence counts across all 4 languages.")
