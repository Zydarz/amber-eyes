import json
with open('.work/tap48_vn.json', 'r', encoding='utf-8') as f: vn = json.load(f)
with open('.work/tap48_ja.json', 'r', encoding='utf-8') as f: ja = json.load(f)

for v, j in zip(vn, ja):
    if v['kind'] == 'LOI':
        v_cnt = len(v['sentences'])
        j_cnt = len(j['sentences'])
        if v_cnt != j_cnt:
            print(f"{v['id']}: VN={v_cnt}, JA={j_cnt}")
            for idx, s in enumerate(j['sentences']):
                print(f"   JA #{idx+1}: {s['text']}")
            for idx, s in enumerate(v['sentences']):
                print(f"   VN #{idx+1}: {s['text']}")
