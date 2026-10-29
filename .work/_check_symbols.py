import json, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data = json.load(open('.work/script_tap04_test.json', encoding='utf-8'))
symbols = ['%', '$', 'km', 'kg', 'mg', 'ml', '°', '&', '#', '@']
for e in data:
    if e['kind'] == 'LOI':
        for s in e['sentences']:
            t = s['text']
            found = [sym for sym in symbols if sym in t]
            if found:
                print(f"{s['id']}: found {found} in -> {t}")
