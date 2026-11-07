# -*- coding: utf-8 -*-
import sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

for lang, path in [
    ('VN', '.work/script_tap19.json'),
    ('EN', '.work/script_tap19_EN.json'),
    ('JA', '.work/script_tap19_JA.json'),
    ('KO', '.work/script_tap19_KO.json'),
]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {lang} SCRIPT AUDIT ===")
    sentences = []
    for elem in data:
        for s in elem.get('sentences', []):
            sentences.append((s['id'], s['text']))
    print(f"Total sentences: {len(sentences)}")

    # Check for double spaces, punctuation errors, trailing/leading spaces
    issues = []
    for sid, txt in sentences:
        if '  ' in txt:
            issues.append((sid, 'Double space', txt))
        if re.search(r'\s[,\.\?!:;]', txt):
            issues.append((sid, 'Space before punctuation', txt))
        if re.search(r'[,;:](?!\s)', txt):
            # check if comma/semicolon without following space
            issues.append((sid, 'No space after comma/semicolon', txt))
        if txt != txt.strip():
            issues.append((sid, 'Leading/trailing whitespace', txt))
        # check quotes
        if txt.count("'") % 2 != 0 and txt.count('"') % 2 != 0:
            # unclosed quote? Note in EN contractions like don't, it's can cause odd counts
            if lang != 'EN':
                issues.append((sid, 'Possible unclosed quote', txt))
    print(f"Punctuation & whitespace issues in {lang}: {len(issues)}")
    for sid, issue_type, txt in issues:
        print(f"  [{sid}] {issue_type}: {txt}")
