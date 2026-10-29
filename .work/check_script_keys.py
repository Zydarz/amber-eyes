import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap06.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

print(f"Sample item keys: {list(sc[0].keys())}")
print(f"Sample item: {sc[0]}")
for s in sc[:10]:
    print(f"id: {s.get('id')}, code: {s.get('code')}, sec: {s.get('sec')}")
