import json

with open('.work/script_tap17.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

with open('.work/tap17_all_sentences.txt', 'w', encoding='utf-8') as out:
    for elem in sc:
        if elem.get('kind') == 'LOI':
            sents = elem.get('sentences', [])
            out.write(f"=== {elem['id']} | Act {elem['act']} | Role {elem['role']} | {len(sents)} sents ===\n")
            for s in sents:
                out.write(f"  {s['id']}: {s['text']}\n")

print("Done writing .work/tap17_all_sentences.txt")
