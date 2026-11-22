import json

data = json.load(open('.work/_episodes_data_final.json', encoding='utf-8'))
for r in data[30:50]:
    print(f"Tập {r['ep']:02d}: {r['clean_title'][:28]} | QG: {r['country']} | Câu: {r['sentences']} | Ảnh: {r['images']} | Shot: {r['expected_shots']}")
