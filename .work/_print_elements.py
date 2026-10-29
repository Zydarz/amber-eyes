import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
data = json.load(open('.work/script_tap04.json', encoding='utf-8'))
for e in data:
    role = f":{e['role']}" if 'role' in e else ""
    content = e.get('desc', e.get('text', ''))[:65]
    print(f"{e['id']} ({e['kind']}{role}): {content}")
