import json, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
data = json.load(open('.work/script_tap04.json', encoding='utf-8'))

print("=== SCRIPT ELEMENTS AND SENTENCES ===")
for e in data:
    if e['kind'] == 'LOI':
        s_ids = [s['id'] for s in e['sentences']]
        print(f"{e['id']} ({e['role']}): {len(s_ids)} sents -> {s_ids[0]} to {s_ids[-1]}")
