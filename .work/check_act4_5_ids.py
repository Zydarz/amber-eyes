import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap06.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

for row in sc:
    sec = str(row.get('sec', ''))
    if sec.startswith('4.') or sec.startswith('5.'):
        print(f"[{sec}#{row.get('stt_in_sec')}] ({row.get('role')}): {row.get('text')[:50]}...")
