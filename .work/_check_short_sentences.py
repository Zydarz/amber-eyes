import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data = json.load(open('.work/script_tap04_test.json', encoding='utf-8'))
print("=== SHORT SENTENCES (< 6 words) ===")
for e in data:
    if e['kind'] == 'LOI':
        for s in e['sentences']:
            words = s['text'].split()
            if len(words) < 6:
                print(f"{s['id']} ({len(words)} w, role={e['role']}): {s['text']}")
