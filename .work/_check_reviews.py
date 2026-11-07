# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for p in ['01_KICH_BAN/Tap10/REVIEW_kichban_tap10_10chiau.md', '01_KICH_BAN/Tap10/REVIEW_kichban_tap10_multilingual.md']:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    for search_term in ['Cameron không hề thuộc về', 'Cameron does not belong', 'The Company”에 대한', 'Sheriff’s Office']:
        if search_term in content:
            print(f"Found '{search_term}' in {p}")
