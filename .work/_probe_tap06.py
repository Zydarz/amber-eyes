import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap06.json', encoding='utf-8') as f:
    data = json.load(f)

for t in data:
    if t.get('kind') == 'LOI':
        sents = t.get('sentences', [])
        s_ids = f"{sents[0]['id']}..{sents[-1]['id']}" if sents else ""
        first_txt = sents[0]['text'][:45] if sents else ""
        print(f"Hoi {t.get('act')} | Turn {t.get('id'):<5} | Role {t.get('role')} | {len(sents):>2} c | {s_ids:<14} | {first_txt}...")
