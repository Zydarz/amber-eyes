import json
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/_tap11_sentences.json', 'r', encoding='utf-8') as f:
    raw_sentences = json.load(f)

grouped = defaultdict(list)
for item in raw_sentences:
    grouped[item['elem_id']].append(item)

with open('.work/_tap11_all_dialogue.txt', 'w', encoding='utf-8') as f:
    for elem_id, items in grouped.items():
        role = items[0]['role']
        f.write(f"=== ELEMENT {elem_id} [{role}] ({len(items)} sentences) ===\n")
        for it in items:
            s_obj = it['text']
            sid = s_obj['id']
            txt = s_obj['text']
            f.write(f"  {sid}: {txt}\n")
        f.write("\n")

print(f"Grouped into {len(grouped)} dialogue elements.")
