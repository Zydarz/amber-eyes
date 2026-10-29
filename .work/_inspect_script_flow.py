import json, sys
sys.stdout.reconfigure(encoding='utf-8')

script = json.load(open('.work/script_tap05.json', encoding='utf-8'))
for el in script:
    if el.get('kind') == 'LOI':
        s = el['sentences']
        print(f"{el['id']} ({el['role']}): {s[0]['id']} -> {s[-1]['id']} ({len(s)} cau): {s[0]['text'][:45]}...")
    elif el.get('kind') == 'NGHI':
        print(f"{el['id']} (NGHI {el['sec']}s): {el.get('desc')}")
