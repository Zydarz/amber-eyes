# -*- coding: utf-8 -*-
import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

print("=== CHECKING SCRIPTS FOR SPELLING & FORMAT ISSUES (TAP 19) ===")

scripts = [
    ('VN', '.work/script_tap19.json'),
    ('EN', '.work/script_tap19_EN.json'),
    ('JA', '.work/script_tap19_JA.json'),
    ('KO', '.work/script_tap19_KO.json'),
]

for lang, path in scripts:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_sentences = 0
    issues = []
    for el in data:
        for s in el.get('sentences', []):
            total_sentences += 1
            txt = s['text']
            sid = s['id']
            
            # 1. Double space
            if '  ' in txt:
                issues.append((sid, 'Double space', txt))
            # 2. Leading/trailing space
            if txt != txt.strip():
                issues.append((sid, 'Leading/trailing whitespace', txt))
            # 3. Space before punctuation
            if re.search(r'\s[,\.\?!:;]', txt):
                issues.append((sid, 'Space before punctuation', txt))
            # 4. Comma without space
            if re.search(r'[,;:](?!\s)', txt):
                issues.append((sid, 'No space after comma/semicolon', txt))
            # 5. Repeated consecutive words
            words = txt.split()
            for i in range(len(words)-1):
                w1 = re.sub(r'^[^\w]+|[^\w]+$', '', words[i]).lower()
                w2 = re.sub(r'^[^\w]+|[^\w]+$', '', words[i+1]).lower()
                if w1 and w1 == w2:
                    # check exceptions like 'mãi mãi' in VN or 'twenty twenty' in EN
                    if lang == 'VN' and w1 in ['mãi']:
                        continue
                    if lang == 'EN' and w1 in ['twenty']:
                        continue
                    issues.append((sid, f'Repeated word: {w1}', txt))

    print(f"[{lang}] Scanned {total_sentences} sentences -> Issues found: {len(issues)}")
    for sid, itype, txt in issues:
        print(f"   {sid}: {itype} -> {txt}")

print("\n=== SPELL CHECK COMPLETE ===")
