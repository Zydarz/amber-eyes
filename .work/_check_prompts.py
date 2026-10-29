import json, sys
sys.stdout.reconfigure(encoding='utf-8')

jobs = json.load(open('.work/bg_jobs_tap05.json', encoding='utf-8'))
for j in jobs:
    name = j['name']
    prompt = j['prompt'].lower()
    # Check for suspicious prompt words: face, victim, girl, woman, letter, text, words, license plate
    suspicious = []
    if 'face' in prompt and 'faceless' not in prompt and 'no face' not in prompt and 'silhouette' not in prompt:
        suspicious.append('face')
    if 'victim' in prompt:
        suspicious.append('victim')
    if 'text' in prompt or 'letter' in prompt or 'words' in prompt:
        suspicious.append('text/letters')
    if suspicious:
        print(f"{name:<35} | {suspicious} | {j['prompt'][:80]}")
