import json, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data = json.load(open('.work/script_tap04_test.json', encoding='utf-8'))
for e in data:
    if e['kind'] == 'LOI':
        for s in e['sentences']:
            t = s['text']
            # check pronouns
            pronouns = re.findall(r'\b(hắn|hắn ta|ông|ông ấy|bà|bà ấy|anh|anh ấy|cô|cô ấy)\b', t, re.I)
            if pronouns:
                print(f"{s['id']} [{e['role']}]: {pronouns} in -> {t}")
