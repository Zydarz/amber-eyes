import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap02.json', 'r', encoding='utf-8') as f:
    script = json.load(f)

for e in script:
    if e.get('kind') == 'LOI':
        print(f"=== {e['id']} ({e['role']}): {len(e['sentences'])} sentences ===")
        for i, s in enumerate(e['sentences'], 1):
            print(f"[{e['id']}#{i}] {s['text']}")
    else:
        print(f"--- {e['id']}: {e['kind']} ({e.get('desc', e.get('sec', ''))}) ---")
