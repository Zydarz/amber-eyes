import sys, json

ep = sys.argv[1]
data = json.load(open(f'.work/temp_parse_t{ep}.json', encoding='utf-8'))
out_path = f'.work/tap{ep}_dump.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    out.write(f'Total elements: {len(data)}\n')
    for e in data:
        if e['kind'] == 'LOI':
            out.write(f"{e['id']} | LOI | {e['role']} | {len(e['sentences'])} sents | {e.get('direction', '')}\n")
            for s in e['sentences']:
                out.write(f"   {s['id']}: {s['text']}\n")
        elif e['kind'] in ('SFX', 'BGM'):
            out.write(f"{e['id']} | {e['kind']} | {e['desc']}\n")
        elif e['kind'] == 'NGHI':
            out.write(f"{e['id']} | NGHI | {e['sec']}s | {e.get('desc', '')}\n")
print(f"Dumped to {out_path}")

