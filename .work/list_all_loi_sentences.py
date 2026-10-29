import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap06.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

for s in sc:
    if s.get('kind') == 'LOI':
        print(f"--- {s['id']} (Act {s['act']}, Role {s['role']}) ---")
        for sub in s.get('sentences', []):
            print(f"  {sub['id']}: {sub['text']}")
