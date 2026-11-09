import json, sys
sys.stdout.reconfigure(encoding='utf-8')
vn = json.load(open('.work/script_tap01_new_vn.json', encoding='utf-8'))
ko = json.load(open('.work/script_tap01_new_ko.json', encoding='utf-8'))

for target in ['2.04', '2.07', '4.03', '4.05', '4.07', '4.09', '4.11', '4.14', '5.02', '5.04', '5.05', '5.10']:
    v_el = next(e for e in vn if e['id'] == target)
    k_el = next(e for e in ko if e['id'] == target)
    print(f"=== {target} (VN={len(v_el['sentences'])}, KO={len(k_el['sentences'])}) ===")
    max_len = max(len(v_el['sentences']), len(k_el['sentences']))
    for i in range(max_len):
        vs = v_el['sentences'][i]['text'][:40] if i < len(v_el['sentences']) else "---"
        ks = k_el['sentences'][i]['text'][:40] if i < len(k_el['sentences']) else "---"
        print(f"  {i+1:2d} | VN: {vs:<42} | KO: {ks}")
