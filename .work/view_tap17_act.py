import json

with open('.work/script_tap17.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

for act in range(1, 6):
    print(f"\n=================== HỒI {act} ===================")
    for elem in sc:
        if elem.get('act') == act and elem.get('kind') == 'LOI':
            print(f"\n--- [{elem['id']}] Vai: {elem['role']} ({len(elem.get('sentences', []))} câu) ---")
            for s in elem.get('sentences', []):
                print(f"  {s['id']}: {s['text']}")
