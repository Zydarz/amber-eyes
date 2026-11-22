import json

d = json.load(open('.work/_parsed_Tap68.json', encoding='utf-8'))
print('Tap 68 elements in parsed json:', len(d))
for i, elem in enumerate(d):
    k = elem.get('kind')
    r = elem.get('role')
    t = elem.get('text', '')
    sents = elem.get('sentences', [])
    print(f"{i}: id={elem.get('id')} kind={k} role={r} sents_cnt={len(sents)} text_sample={t[:50]}")
