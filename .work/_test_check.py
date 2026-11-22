import json
rows = json.load(open('.work/_final_verified_report.json', encoding='utf-8'))
for r in rows:
    if r['ep'] in [6, 21, 22, 23, 24, 31, 32, 33, 34, 35, 53, 54, 55, 68]:
        print(f"Tap {r['ep']:02d}: {r['title'][:35]} | QG: {r['country']} | Cau: {r['sentences']} | Anh: {r['images']} | Shot: {r['shots']}")
