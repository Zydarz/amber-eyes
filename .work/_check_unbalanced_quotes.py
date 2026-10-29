import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data = json.load(open('.work/script_tap04_test.json', encoding='utf-8'))
for e in data:
    if e['kind'] == 'LOI':
        for s in e['sentences']:
            t = s['text']
            # count opening and closing quotes
            open_q = t.count('“') + t.count('"')
            close_q = t.count('”') + t.count('"')
            # If standard curly quotes:
            o_c = t.count('“')
            c_c = t.count('”')
            if o_c != c_c:
                print(f"Unbalanced quotes in {s['id']}: open={o_c}, close={c_c}")
                print(f"   Text: {t}")
