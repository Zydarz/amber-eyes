# -*- coding: utf-8 -*-
import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/script_tap19_JA.json', 'r', encoding='utf-8') as f:
    ja_data = json.load(f)

with open('.work/script_tap19_KO.json', 'r', encoding='utf-8') as f:
    ko_data = json.load(f)

# Check KO repeated words
ko_issues = []
for el in ko_data:
    for s in el.get('sentences', []):
        tokens = s['text'].split()
        for i in range(len(tokens)-1):
            if tokens[i] == tokens[i+1]:
                ko_issues.append((s['id'], tokens[i], s['text']))

print(f"KO repeated words: {len(ko_issues)}")
for sid, w, txt in ko_issues:
    print(f"  [{sid}] '{w}': {txt}")

# Check JA repeated 3+ kana/kanji sequences (e.g. のの, にに, はは)
ja_issues = []
for el in ja_data:
    for s in el.get('sentences', []):
        m = re.findall(r'([のにはをもでへとが])\1', s['text'])
        if m:
            ja_issues.append((s['id'], m, s['text']))

print(f"JA repeated particles: {len(ja_issues)}")
for sid, m, txt in ja_issues:
    print(f"  [{sid}] {m}: {txt}")
