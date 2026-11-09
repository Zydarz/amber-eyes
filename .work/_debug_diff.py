import json, sys
sys.stdout.reconfigure(encoding='utf-8')
vn = json.load(open('.work/script_tap01_new_vn.json', encoding='utf-8'))
ja = json.load(open('.work/script_tap01_new_ja.json', encoding='utf-8'))
for target in ['4.05', '5.10', '5.12']:
    v_el = next(e for e in vn if e['id'] == target)
    j_el = next(e for e in ja if e['id'] == target)
    print(f"=== {target} VN ({len(v_el['sentences'])} sentences) ===")
    for s in v_el['sentences']: print('  VN:', s['text'])
    print(f"=== {target} JA ({len(j_el['sentences'])} sentences) ===")
    for s in j_el['sentences']: print('  JA:', s['text'])
