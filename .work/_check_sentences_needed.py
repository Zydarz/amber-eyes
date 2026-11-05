import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap02_temp.json', 'r', encoding='utf-8') as f:
    old_script = json.load(f)

for el_id in ['3.08', '4.11', '5.04']:
    match = [x for x in old_script if x['id'] == el_id]
    if match:
        print(f"OLD {el_id} sentence count: {len(match[0]['sentences'])}")
        for i, s in enumerate(match[0]['sentences'], 1):
            print(f"  OLD {el_id}#{i}: {s['text'][:70]}...")
