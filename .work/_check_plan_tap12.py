# -*- coding: utf-8 -*-
import re, os

text = open('02_SAN_XUAT/Tap12/KeHoach_Video_Tap12.md', encoding='utf-8').read()
rows = [l for l in text.splitlines() if re.match(r'\|\s*[1-5]-\d+', l)]
print('Total shot rows:', len(rows))

bgs_in_rows = set()
for r in rows:
    for bg in re.findall(r'`(t12_[^`]+|void)`', r):
        bgs_in_rows.add(bg)

print('Distinct backgrounds in shot rows:', len(bgs_in_rows))

missing = [bg for bg in bgs_in_rows if bg != 'void' and not os.path.exists(f'assets/bg/{bg}.png')]
print('Missing backgrounds in assets/bg/:', missing)

# Check all 249 sentences
import json
script = json.loads(open('.work/script_tap12.json', encoding='utf-8').read())
sids = [s['id'] for e in script if e['kind'] == 'LOI' for s in e['sentences']]
print('Total sentences in script:', len(sids))

found_sids = []
for r in rows:
    m = re.findall(r'`(\d\.\d+#\d+)`', r)
    found_sids.extend(m)

print('Total mapped sentence IDs in plan:', len(found_sids))
print('Difference (sids - found_sids):', set(sids) - set(found_sids))
print('Difference (found_sids - sids):', set(found_sids) - set(sids))
