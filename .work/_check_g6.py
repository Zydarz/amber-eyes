import json, sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

acting = json.load(open('.work/acting_tap04.json', encoding='utf-8'))
script = json.load(open('.work/script_tap04.json', encoding='utf-8'))

sents = {s['id']: s['text'] for e in script if e['kind'] == 'LOI' for s in e['sentences']}

mismatches = []
for sid, item in acting.items():
    if sid.startswith('_'):
        continue
    emo, dsp, pitch, alt = item
    orig = sents[sid].replace("“", "").replace("”", "").replace('"', "")
    if alt:
        # strip tags <#...#>
        alt_clean = re.sub(r'<#[^>]+>', '', alt)
        # normalize whitespace
        alt_norm = ' '.join(alt_clean.split())
        orig_norm = ' '.join(orig.split())
        if alt_norm != orig_norm:
            mismatches.append((sid, orig_norm, alt_norm))

if mismatches:
    print(f"G6 VIOLATION: {len(mismatches)} mismatches found!")
    for sid, o, a in mismatches:
        print(f"  {sid}:")
        print(f"    orig: {o}")
        print(f"    alt : {a}")
else:
    print("RULE G6 CHECK PASSED 100%: Lời đọc khớp từng chữ với câu gốc!")
