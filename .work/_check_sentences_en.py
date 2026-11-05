# -*- coding: utf-8 -*-
"""Inspect sentences for each shot mapping."""
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

sc = json.load(open('.work/script_tap06_EN.json', encoding='utf-8'))
S = {}
for el in sc:
    if el.get('kind') == 'LOI':
        for s in el['sentences']:
            S[s['id']] = s['text']

print(f"Total sentences: {len(S)}")
# Print some key sentences to verify text
for k in ['1.02#1', '1.02#2', '1.06#1', '1.06#6', '1.06#7', '1.06#8', '1.08#1', '1.08#4', '1.09#1', '2.03#1', '2.06#2', '3.02#1', '3.12#1', '4.04#1', '4.08#1', '5.02#1', '5.04#1', '5.06#1', '5.06#4', '5.06#16', '5.06#17']:
    print(f"[{k}] {S.get(k)}")
