import json

meta = json.load(open('.work/_accurate_final_report.json', encoding='utf-8'))
for r in meta[28:]:
    print(f"Tap {r['ep']:02d}: {r['title'][:40]} | QG: {r['country']} | Imgs: {r['images']}")
