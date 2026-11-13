# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
target_ids = [
    '1.02#7', '1.02#8', '1.02#9', '1.02#10',
    '2.04#5', '2.04#6', '2.04#7', '2.04#8',
    '2.06#5', '2.06#6', '2.06#7', '2.06#8',
    '3.07#6', '3.07#7', '3.07#8',
    '3.08#5', '3.08#6', '3.08#7',
    '4.03#4', '4.03#5', '4.03#6',
    '4.04#2',
    '4.05#1', '4.05#2', '4.05#3', '4.05#4', '4.05#5', '4.05#6', '4.05#7', '4.05#8',
    '4.09#3', '4.09#4', '4.09#5',
    '4.10#5',
    '5.03#4',
    '5.04#4', '5.04#5'
]

for e in p:
    if e['kind'] == 'LOI':
        for s in e['sentences']:
            if s['id'] in target_ids:
                print(f"[{s['id']}] ({e['role']}): {s['text']}")
