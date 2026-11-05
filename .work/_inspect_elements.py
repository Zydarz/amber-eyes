# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

sc = json.load(open('.work/script_tap06_EN.json', encoding='utf-8'))
for el in sc:
    if el.get('kind') == 'LOI':
        s_ids = [s['id'] for s in el['sentences']]
        print(f"{el['id']} ({el.get('role')}): {len(s_ids)} cau -> {s_ids[0]} .. {s_ids[-1]}")
