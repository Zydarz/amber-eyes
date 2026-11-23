# -*- coding: utf-8 -*-
import sys, re
sys.path.append('.work')
import parse_kichban

files = {
    'VN': '01_KICH_BAN/Ho_So_Toi_Pham/Tap40/kichban_tap40_19112026.md',
    'EN': '01_KICH_BAN/Ho_So_Toi_Pham/Tap40_EN/kichban_tap40_EN.md',
    'JA': '01_KICH_BAN/Ho_So_Toi_Pham/Tap40_JA/kichban_tap40_JA.md'
}

for lang, fpath in files.items():
    raw = open(fpath, encoding='utf-8').read().splitlines()
    els = parse_kichban.parse_lines(raw)
    sents = [s for e in els for s in e.get('sentences', [])]
    print(f'=== {lang} ({len(raw)} lines, {len(els)} elements, {len(sents)} sentences) ===')
    
    # 1. Bracket balance
    for s in sents:
        txt = s['text']
        sid = s['id']
        if txt.count('(') != txt.count(')'):
            print('  Mismatched () in', sid, ':', txt)
        if txt.count('“') != txt.count('”'):
            print('  Mismatched “” in', sid, ':', txt)
        if txt.count('「') != txt.count('」'):
            print('  Mismatched 「」 in', sid, ':', txt)
            
    # 2. Rule G1 (ellipsis)
    ellipsis = [s for s in sents if '...' in s['text'] or '…' in s['text']]
    if ellipsis:
        print('  Ellipsis found:', len(ellipsis))
        for s in ellipsis:
            print('   ', s['id'], s['text'])
        
    # 3. Repeated adjacent words
    if lang in ['VN', 'EN']:
        rep_pat = re.compile(r'\b([a-zA-ZÀ-ỹ]+)\s+\1\b', re.IGNORECASE)
        reps = [(s['id'], m.group(0)) for s in sents for m in [rep_pat.search(s['text'])] if m]
        if reps:
            print('  Repeated words:', reps)
            
    # 4. End punctuation
    no_end_punct = [s for s in sents if not re.search(r'[.!?。！？…][”"』」)]*$', s['text'])]
    if no_end_punct:
        print('  No end punctuation:', len(no_end_punct))
        for s in no_end_punct:
            print('   ', s['id'], s['text'])

print('All checks finished successfully.')
