import json, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap16/kichban_tap16_23102026.md'),
    ('EN', '01_KICH_BAN/Tap16_EN/kichban_tap16_EN.md'),
    ('JA', '01_KICH_BAN/Tap16_JA/kichban_tap16_JA.md'),
    ('KO', '01_KICH_BAN/Tap16_KO/kichban_tap16_KO.md'),
]

forbidden = {
    'VN': ['máu', 'thi thể', 'đập tan', 'đập loạn', 'tự sát', 'cắt cổ', 'chặt', 'bóp cổ', 'khí độc', 'ngạt thở'],
    'EN': ['blood', 'corpse', 'decapitat', 'strangl', 'suicide'],
    'JA': ['自殺', '死体', '血液', '窒息'],
    'KO': ['자살', '시체', '혈흔', '질식'],
}

all_green = True
counts = {}

for lang, path in files:
    print(f"\n==========================================")
    print(f"QC SCRIPT: {path} ({lang})")
    print(f"==========================================")
    parsed = PK.parse_file(path)
    total_elements = len(parsed)
    loi = [e for e in parsed if e['kind'] == 'LOI']
    total_sentences = sum(len(x.get('sentences', [])) for x in loi)
    total_words = sum(sum(s['words'] for s in x['sentences']) for x in loi)
    counts[lang] = (total_elements, len(loi), total_sentences)
    
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
        
    status = (len(fb_hits) == 0 and len(ellipsis_hits) == 0 and total_sentences == 220 and total_elements == 51)
    print(f"Result for {lang}: {'PASS' if status else 'FAIL'}")
    all_green = all_green and status

# Check parity across languages
print("\n==========================================")
print("PARITY AUDIT ACROSS 4 EDITIONS")
print("==========================================")
ref = counts['VN']
parity_ok = True
for lang, cnt in counts.items():
    if cnt != ref:
        print(f"MISMATCH in {lang}: {cnt} != VN {ref}")
        parity_ok = False
    else:
        print(f"{lang}: {cnt[0]} elements, {cnt[1]} LOI turns, {cnt[2]} sentences -> MATCH")

all_green = all_green and parity_ok
print(f"\n>>> FINAL STATUS TAP 16: {'ALL PASS' if all_green else 'FAILURES FOUND'} <<<")
sys.exit(0 if all_green else 1)
