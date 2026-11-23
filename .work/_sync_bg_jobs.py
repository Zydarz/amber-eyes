import json, os, re, shutil

shuffle_data = json.load(open('.work/_proposed_shuffle.json', encoding='utf-8'))
mapping = {item['old_ep']: item['new_ep'] for item in shuffle_data}

# Staging directory for bg_jobs
staging_dir = ".work/_staging_bg_jobs"
if os.path.exists(staging_dir):
    shutil.rmtree(staging_dir)
os.makedirs(staging_dir, exist_ok=True)

# 1. Read old job files and transform keys/names to new episode prefix
transformed = {}
for old_ep, new_ep in mapping.items():
    old_fn = f".work/bg_jobs_tap{old_ep:02d}.json"
    if os.path.exists(old_fn):
        d = json.load(open(old_fn, encoding='utf-8'))
        # Replace prefix inside data: t{old_ep}_ -> t{new_ep}_
        old_pref = f"t{old_ep}_"
        new_pref = f"t{new_ep}_"
        
        new_data = []
        if isinstance(d, list):
            for item in d:
                if 'name' in item:
                    item['name'] = item['name'].replace(old_pref, new_pref)
                if 'prompt' in item:
                    # also replace inside prompt if mentioned
                    item['prompt'] = item['prompt'].replace(old_pref, new_pref)
                new_data.append(item)
        elif isinstance(d, dict):
            new_data = {}
            for k, v in d.items():
                new_k = k.replace(old_pref, new_pref)
                new_data[new_k] = v
                
        # Save to staging
        staged_path = os.path.join(staging_dir, f"bg_jobs_tap{new_ep:02d}.json")
        open(staged_path, 'w', encoding='utf-8').write(json.dumps(new_data, ensure_ascii=False, indent=2))
        transformed[new_ep] = staged_path

# 2. Move from staging to final .work/bg_jobs_tap{new_ep}.json
for new_ep, staged_path in transformed.items():
    dst = f".work/bg_jobs_tap{new_ep:02d}.json"
    shutil.copy2(staged_path, dst)

print(f"Successfully synchronized {len(transformed)} bg_jobs files with new episode numbers!")
