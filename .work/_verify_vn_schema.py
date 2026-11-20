# -*- coding: utf-8 -*-
"""Verification of VN Act 1-5 against target schema."""
import sys, json
sys.path.insert(0, '.work')
import _tap38_act1
import _tap38_act2_5

with open('.work/_tap38_target_schema.json', encoding='utf-8') as f:
    target = json.load(f)

all_items = []
all_acts = [_tap38_act1.get_acts(), _tap38_act2_5.get_act2(), _tap38_act2_5.get_act3(), _tap38_act2_5.get_act4(), _tap38_act2_5.get_act5()]
for act_idx, act in enumerate(all_acts, 1):
    for elem_idx, elem in enumerate(act, 1):
        el_id = f"{act_idx}.{elem_idx:02d}"
        kind = elem[0]
        if kind == 'LOI':
            role = elem[1]
            s_cnt = len(elem[2])
        else:
            role = None
            s_cnt = 0
        all_items.append({'id': el_id, 'act': act_idx, 'kind': kind, 'role': role, 's_count': s_cnt})

assert len(all_items) == len(target)
for i in range(len(target)):
    t = target[i]
    a = all_items[i]
    assert t['id'] == a['id']
    assert t['kind'] == a['kind']
    assert t['role'] == a['role']
    assert t['s_count'] == a['s_count']
print("VN structure matches target schema 100% perfectly!")
