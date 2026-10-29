import json
import sys

with open('.work/script_tap06.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

lines = []
for s in sc:
    if s.get('kind') == 'LOI':
        lines.append(f"--- {s['id']} (Act {s['act']}, Role {s['role']}) ---")
        for sub in s.get('sentences', []):
            lines.append(f"  {sub['id']}: {sub['text']}")

with open('.work/all_loi_sentences.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Wrote .work/all_loi_sentences.txt")
