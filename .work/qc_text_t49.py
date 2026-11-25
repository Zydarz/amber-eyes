# -*- coding: utf-8 -*-
import json
import re

data = json.load(open('.work/scratch_t49_parsed.json', encoding='utf-8'))
print(f"Loaded {len(data)} blocks.")
digit_count = 0
quote_count = 0
special_count = 0

for e in data:
    for s in e.get('sentences', []):
        t = s['text']
        # check digits
        m_digits = re.findall(r'\d+', t)
        if m_digits:
            digit_count += 1
            print(f"[DIGIT] {s['id']}: {m_digits} in: {t}")
        # check quotes
        if "'" in t or '"' in t or '“' in t or '”' in t:
            quote_count += 1
            # print(f"[QUOTE] {s['id']}: {t}")
        # check special characters
        m_spec = re.findall(r'[%$&@#^*_=+<>\[\]{}]', t)
        if m_spec:
            special_count += 1
            print(f"[SPECIAL] {s['id']}: {m_spec} in: {t}")

print(f"Summary: {digit_count} digits, {quote_count} quotes, {special_count} specials.")
