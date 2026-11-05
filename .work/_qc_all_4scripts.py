import json, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap07/kichban_tap07_23102026.md'),
    ('EN', '01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md'),
    ('JA', '01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md'),
    ('KO', '01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md'),
]

forbidden = {
    'VN': ['máu', 'thi thể', 'đập tan', 'đập loạn', 'tự sát', 'cắt cổ', 'chặt', 'bóp cổ', 'khí độc', 'ngạt thở'],
    'EN': ['blood', 'corpse', 'decapitat', 'strangl', 'suicide'],
    'JA': ['自殺', '死体', '血液', '窒息'],
    'KO': ['자살', '시체', '혈흔', '질식'],
}

all_green = True
for lang, path in files:
    print(f"\n==========================================")
    print(f"QC SCRIPT: {path} ({lang})")
    print(f"==========================================")
    parsed = PK.parse_file(path)
    total_elements = len(parsed)
    loi = [e for e in parsed if e['kind'] == 'LOI']
    total_sentences = sum(len(x.get('sentences', [])) for x in loi)
    total_words = sum(sum(s['words'] for s in x['sentences']) for x in loi)
    
    print(f"Elements: {total_elements}")
    print(f"LOI turns: {len(loi)}")
    print(f"Sentences: {total_sentences}")
    print(f"Total words: {total_words}")
    
    fb_hits = []
    ellipsis_hits = []
    
    fb_list = forbidden.get(lang, [])
    for e in loi:
        for s in e['sentences']:
            txt = s['text']
            sid = s['id']
            for fb in fb_list:
                # for EN/VN use word boundaries, for JA/KO use substring
                if lang in ['VN', 'EN']:
                    if re.search(r'\b' + re.escape(fb) + r'\b', txt, re.IGNORECASE):
                        fb_hits.append((sid, fb, txt))
                else:
                    if fb in txt:
                        fb_hits.append((sid, fb, txt))
            if '...' in txt or '…' in txt:
                ellipsis_hits.append((sid, txt))
                
    print(f"Forbidden word hits: {len(fb_hits)}")
    for h in fb_hits:
        print(f"  - {h[0]}: forbidden '{h[1]}' in '{h[2]}'")
    print(f"Ellipsis (G1) hits: {len(ellipsis_hits)}")
    for d in ellipsis_hits:
        print(f"  - {d[0]}: ellipsis in '{d[1]}'")
        
    status = (len(fb_hits) == 0 and len(ellipsis_hits) == 0 and total_sentences == 147 and total_elements == 50)
    print(f"Result for {lang}: {'PASS' if status else 'FAIL'}")
    all_green = all_green and status

print(f"\n>>> FINAL STATUS: {'ALL PASS' if all_green else 'FAILURES FOUND'} <<<")
