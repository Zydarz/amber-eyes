import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap06.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

for s in sc:
    if s.get('kind') == 'LOI':
        print(f"Sample LOI item: {s}")
        break
