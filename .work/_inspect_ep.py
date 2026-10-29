import sys, json
sys.stdout.reconfigure(encoding='utf-8')
ep = int(sys.argv[1]) if len(sys.argv) > 1 else 20
data = json.load(open(f'.work/temp_parse_t{ep:02d}.json', encoding='utf-8'))
print(f"Total elements: {len(data)}")
for e in data:
    s_cnt = len(e.get('sentences', []))
    desc = e.get('desc', '')
    role = e.get('role', '-')
    print(f"{e['id']} | {e['kind']:4} | role={role} | sents={s_cnt:2} | {desc[:60]}")
