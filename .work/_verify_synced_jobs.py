import os, json

for ep in [30, 31, 34, 38, 40]:
    fn = f".work/bg_jobs_tap{ep:02d}.json"
    d = json.load(open(fn, encoding='utf-8'))
    sample = d[0]['name'] if isinstance(d, list) else list(d.keys())[0]
    matching = [f for f in os.listdir('assets/bg') if f.startswith(f"t{ep}_")]
    print(f"Tap {ep:02d}: job sample='{sample}' | matching files in assets/bg={len(matching)}")
