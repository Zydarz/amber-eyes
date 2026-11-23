import json, os

shuffle_data = json.load(open('.work/_proposed_shuffle.json', encoding='utf-8'))
for item in shuffle_data:
    old_ep = item['old_ep']
    new_ep = item['new_ep']
    old_job = f".work/bg_jobs_tap{old_ep:02d}.json"
    t = item['title'][:25]
    print(f"New Tap {new_ep:02d} ({t}): was Tap {old_ep:02d}. Old job file exists: {os.path.exists(old_job)}")
