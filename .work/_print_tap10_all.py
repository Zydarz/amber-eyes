# -*- coding: utf-8 -*-
"""Đọc và kiểm tra văn phong, dấu câu, từ ngữ từng hồi của Tập 10."""
import sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

for e in loi:
    print(f"\n=== ELEMENT {e['id']} ({e['role']}) ===")
    for s in e['sentences']:
        print(f"  {s['id']}: {s['text']}")
