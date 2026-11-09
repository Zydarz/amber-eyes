import json, sys
sys.stdout.reconfigure(encoding='utf-8')
vn = json.load(open('.work/script_tap01_new_vn.json', encoding='utf-8'))
ko = json.load(open('.work/script_tap01_new_ko.json', encoding='utf-8'))
diff_ids = ['1.07', '1.13', '2.04', '2.07', '4.03', '4.05', '4.07', '4.09', '4.11', '4.14', '5.02', '5.04', '5.05', '5.10']
for target in diff_ids:
    v_el = next(e for e in vn if e['id'] == target)
    k_el = next(e for e in ko if e['id'] == target)
    print(f"=== {target} VN ({len(v_el['sentences'])}) vs KO ({len(k_el['sentences'])}) ===")
    for i, s in enumerate(v_el['sentences']):
        print(f"  VN {i+1}: {s['text']}")
    for i, s in enumerate(k_el['sentences']):
        print(f"  KO {i+1}: {s['text']}")
