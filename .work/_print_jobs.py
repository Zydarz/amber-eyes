import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
jobs = json.load(open('.work/bg_jobs_tap04.json', encoding='utf-8'))
print("Keys in job 0:", list(jobs[0].keys()))
for i, j in enumerate(jobs, 1):
    print(f"{i:02d}. {j['name']}: {j.get('prompt', '')[:60]}")
