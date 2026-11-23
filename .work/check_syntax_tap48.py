# -*- coding: utf-8 -*-
import re

files = {
    'VN': '01_KICH_BAN/Ho_So_Toi_Pham/Tap48/kichban_tap48_19112026.md',
    'EN': '01_KICH_BAN/Ho_So_Toi_Pham/Tap48_EN/kichban_tap48_EN.md',
    'JA': '01_KICH_BAN/Ho_So_Toi_Pham/Tap48_JA/kichban_tap48_JA.md'
}

for lang, path in files.items():
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    p_open = text.count('(')
    p_close = text.count(')')
    b_open = text.count('[')
    b_close = text.count(']')
    q_open = text.count('\u201c')
    q_close = text.count('\u201d')
    ja_open = text.count('「')
    ja_close = text.count('」')
    
    lines = text.splitlines()
    repeated = []
    trailing_issues = []
    ellipsis_issues = []
    
    for idx, l in enumerate(lines, 1):
        l_str = l.strip()
        if not l_str or l_str.startswith('#') or l_str.startswith('---') or l_str.startswith('|') or l_str.startswith('*') or l_str.startswith('['):
            continue
        if any(l_str.startswith(f"**{t}") for t in ['HOST', 'ĐIỀU TRA', 'CHUYÊN GIA', 'NGƯỜI', 'INVESTIGATOR', 'PSYCHOLOGIST', 'ORDINARY', 'ホスト', '捜査官', '心理専門家', '一般人']):
            continue
        
        # Check repeated words
        words = re.findall(r'\b\w+\b', l_str, re.UNICODE)
        for i in range(len(words)-1):
            w1 = words[i].lower()
            w2 = words[i+1].lower()
            if w1 == w2 and len(w1) > 1 and not w1.isdigit():
                repeated.append((idx, w1, l_str[:50]))
        
        # Check trailing punctuation
        if lang == 'JA':
            if not any(l_str.endswith(ch) for ch in ['。', '！', '？', '」']):
                trailing_issues.append((idx, l_str[-10:]))
        else:
            if not any(l_str.endswith(ch) for ch in ['.', '!', '?', '”', '"', ';']):
                trailing_issues.append((idx, l_str[-10:]))
                
        # Check ellipsis
        if '...' in l_str or '…' in l_str:
            ellipsis_issues.append((idx, l_str[:50]))
            
    print(f'=== {lang} ({path}) ===')
    print(f'Parens (): {p_open} vs {p_close} (diff={p_open-p_close})')
    print(f'Brackets []: {b_open} vs {b_close} (diff={b_open-b_close})')
    print(f'Quotes “”: {q_open} vs {q_close} (diff={q_open-q_close})')
    print(f'JA Quotes 「」: {ja_open} vs {ja_close} (diff={ja_open-ja_close})')
    print(f'Repeated words ({len(repeated)}): {repeated}')
    print(f'Trailing issues ({len(trailing_issues)}): {trailing_issues}')
    print(f'Ellipsis issues ({len(ellipsis_issues)}): {ellipsis_issues}')
