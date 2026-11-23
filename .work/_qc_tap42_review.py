# -*- coding: utf-8 -*-
import re

files = [
    ('VN', '01_KICH_BAN/Ho_So_Toi_Pham/Tap42/kichban_tap42_19112026.md'),
    ('EN', '01_KICH_BAN/Ho_So_Toi_Pham/Tap42_EN/kichban_tap42_EN.md'),
    ('JA', '01_KICH_BAN/Ho_So_Toi_Pham/Tap42_JA/kichban_tap42_JA.md')
]

for tag, path in files:
    text = open(path, encoding='utf-8').read()
    lines = text.splitlines()
    print(f"=== CHECKING {tag} ({path}) ===")
    print(f"Total lines: {len(lines)}")
    
    # 1. Ellipsis (Rule G1)
    for i, l in enumerate(lines):
        if l.startswith('**[') or l.startswith('#') or l.startswith('|') or not l.strip():
            continue
        if '...' in l or '\u2026' in l:
            print(f"  [G1 Warning] Line {i+1} has ellipsis: {l}")
            
    # 2. Duplicate consecutive words
    for i, l in enumerate(lines):
        if l.startswith('**[') or l.startswith('#') or l.startswith('|') or not l.strip():
            continue
        words = re.findall(r'\b\w+\b', l.lower(), flags=re.UNICODE)
        for w1, w2 in zip(words[:-1], words[1:]):
            if w1 == w2 and len(w1) > 1 and not w1.isdigit():
                print(f"  [Repetition] Line {i+1} word '{w1}': {l}")

    # 3. Unbalanced pairs
    for i, l in enumerate(lines):
        if l.count('(') != l.count(')'):
            print(f"  [Unbalanced ()] Line {i+1}: {l}")
        if l.count('\u201c') != l.count('\u201d'):
            print(f"  [Unbalanced double quotes] Line {i+1}: {l}")
        if l.count('\u300c') != l.count('\u300d'):
            print(f"  [Unbalanced Japanese brackets] Line {i+1}: {l}")

    # 4. End of line punctuation for dialogue
    roles = ['HOST', 'ĐIỀU TRA VIÊN', 'CHUYÊN GIA TÂM LÝ', 'NGƯỜI BÌNH THƯỜNG',
             'INVESTIGATOR', 'PSYCHOLOGIST', 'CRIMINAL PSYCHOLOGIST', 'ORDINARY PERSON',
             'ホスト', '捜査官', '心理学者', '一般人']
    in_dialogue = False
    for i, l in enumerate(lines):
        if any(l.startswith(f"**{r}**") for r in roles):
            in_dialogue = True
            continue
        if l.startswith('**[') or l.startswith('##') or l.startswith('---') or not l.strip():
            in_dialogue = False
            continue
        if in_dialogue:
            last_char = l.strip()[-1]
            valid_puncts = ['.', '!', '?', ':', ';', '…', '"', "'", '”', '’', '。', '！', '？', '」', '—', '-']
            if last_char not in valid_puncts:
                print(f"  [No punctuation] Line {i+1} ending with '{last_char}': {l}")

print("\nScan completed successfully.")
