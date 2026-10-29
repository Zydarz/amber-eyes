import json, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data = json.load(open('.work/script_tap04_test.json', encoding='utf-8'))
for e in data:
    if e['kind'] == 'LOI':
        for s in e['sentences']:
            t = s['text']
            # find digits
            digits = re.findall(r'\b\d+[\d.,/-]*\b', t)
            if digits:
                print(f"{s['id']}: {digits} in -> {t}")
