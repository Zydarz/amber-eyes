import sys, json

ep = sys.argv[1]
data = json.load(open(f'.work/temp_parse_t{ep}.json', encoding='utf-8'))
out_lines = []
for e in data:
    kind = e['kind']
    if kind == 'LOI':
        out_lines.append(f"ELEMENT {e['id']} | ROLE: {e['role']} | DIR: {e.get('direction','')} | SENTS: {len(e['sentences'])}")
        for s in e['sentences']:
            out_lines.append(f"  {s['id']}: {s['text']}")
    elif kind in ('BGM', 'SFX'):
        out_lines.append(f"ELEMENT {e['id']} | {kind}: {e.get('desc','')}")
    elif kind == 'NGHI':
        out_lines.append(f"ELEMENT {e['id']} | PAUSE: {e.get('sec')}s - {e.get('desc','')}")
    else:
        out_lines.append(f"ELEMENT {e['id']} | {kind}: {e}")

with open(f'.work/dump_t{ep}.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines) + '\n')
print(f"Dumped {len(data)} elements to .work/dump_t{ep}.txt")
