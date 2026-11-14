# -*- coding: utf-8 -*-
import json

with open('.work/script_tap22.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for el in data:
    if el.get('kind') == 'LOI':
        s_list = el.get('sentences', [])
        first_text = s_list[0]['text'][:45] if s_list else ''
        print(f"{el['id']}: act={el['act']}, role={el['role']}, count={len(s_list)}, start='{first_text}...'")
