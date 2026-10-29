import json
from pathlib import Path

jobs = json.load(open('.work/bg_jobs_tap06.json', encoding='utf-8'))
bg = Path('assets/bg')
missing = [j for j in jobs if not (bg / f"{j['name']}.png").exists()]
print(f"Missing {len(missing)} of {len(jobs)}")
for m in missing[:5]:
    print(" -", m['name'])
