import json

sc = json.load(open('.work/script_tap13.json', encoding='utf-8'))
jobs = json.load(open('.work/bg_jobs_tap13.json', encoding='utf-8'))
all_sents = [s['id'] for e in sc if 'sentences' in e for s in e['sentences']]
print('New script total sentences:', len(all_sents))
print(f'Total jobs: {len(jobs)}')
for i, j in enumerate(jobs):
    print(f'{i+1:02d}: {j["name"]} | Act {j["act"]} | {j["sentences"]} | {j.get("desc", "")[:40]}')
