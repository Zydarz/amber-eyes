import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

data = json.load(open('.work/script_tap04.json', encoding='utf-8'))
sents = [s for e in data if e['kind'] == 'LOI' for s in e['sentences']]
print(f"Total elements: {len(data)}")
print(f"Total sentences: {len(sents)}")
print(f"Total words: {sum(s['words'] for s in sents)}")

unb = []
for s in sents:
    t = s['text']
    o_c = t.count('“')
    c_c = t.count('”')
    if o_c != c_c:
        unb.append((s['id'], o_c, c_c, t))

print(f"Unbalanced quotes count: {len(unb)}")
for item in unb:
    print(item)

print("\n--- Ellipses in sentences ---")
ellipses = [(s['id'], s['text']) for s in sents if '...' in s['text'] or '…' in s['text']]
print(f"Ellipses count: {len(ellipses)}")
for item in ellipses:
    print(item)

print("\n--- Short sentences (< 5 words) ---")
for s in sents:
    words = s['text'].split()
    if len(words) < 5:
        print(f"{s['id']} ({len(words)} w): {s['text']}")
