# -*- coding: utf-8 -*-
import sys, json

sys.stdout.reconfigure(encoding='utf-8')

for lang, path in [
    ('VN', '.work/script_tap19.json'),
    ('EN', '.work/script_tap19_EN.json'),
    ('JA', '.work/script_tap19_JA.json'),
    ('KO', '.work/script_tap19_KO.json'),
]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    out_file = f".work/scratch/sentences_{lang.lower()}.txt"
    with open(out_file, 'w', encoding='utf-8') as out:
        for elem in data:
            if elem.get('sentences'):
                out.write(f"=== {elem['id']} ({elem.get('role', elem['kind'])}) ===\n")
                for s in elem['sentences']:
                    out.write(f"{s['id']}: {s['text']}\n")
    print(f"Wrote {out_file}")
