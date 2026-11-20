import json

data = json.load(open('.work/script_tap23.json', encoding='utf-8'))
lines = []
for el in data:
    if el.get('kind') == 'LOI':
        for s in el.get('sentences', []):
            lines.append(f"{el['act']}\t{s['id']}\t{el.get('role')}\t{s['text']}")

with open('.work/tap23_all_sentences.tsv', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Exported {len(lines)} sentences to .work/tap23_all_sentences.tsv")
