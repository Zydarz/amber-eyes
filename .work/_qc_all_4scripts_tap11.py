# -*- coding: utf-8 -*-
"""QC toàn diện 4 ngôn ngữ của Kịch bản Tập 11: VN, EN, JA, KO."""
import json, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Tap11/kichban_tap11_23102026.md'),
    ('EN', '01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md'),
    ('JA', '01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md'),
    ('KO', '01_KICH_BAN/Tap11_KO/kichban_tap11_KO.md'),
]

forbidden = {
    'VN': ['máu', 'thi thể', 'xác chết', 'tự sát', 'cắt cổ', 'bóp cổ', 'khí độc', 'ngạt thở'],
    'EN': ['blood', 'corpse', 'decapitat', 'strangl', 'suicide'],
    'JA': ['自殺', '死体', '血液', '窒息'],
    'KO': ['자살', '시체', '혈흔', '질식'],
}

parsed_all = {}
all_green = True

print("================================================================")
print("BÁO CÁO KIỂM THỬ QC TOÀN DIỆN KỊCH BẢN TẬP 11 (4 NGÔN NGỮ)")
print("================================================================")

expected_sentences = None
expected_elements = None

for lang, path in files:
    print(f"\n--- QC LANGUAGE: {lang} ({path}) ---")
    p = PK.parse_file(path)
    parsed_all[lang] = p
    
    total_elements = len(p)
    loi = [e for e in p if e['kind'] == 'LOI']
    total_sentences = sum(len(x.get('sentences', [])) for x in loi)
    total_words = sum(sum(s['words'] for s in x['sentences']) for x in loi)
    
    if expected_sentences is None:
        expected_sentences = total_sentences
        expected_elements = total_elements
    
    print(f"Elements: {total_elements}")
    print(f"LOI turns: {len(loi)}")
    print(f"Sentences: {total_sentences} (Yêu cầu >= 200: {'PASS' if total_sentences >= 200 else 'FAIL'})")
    print(f"Words: {total_words}")
    
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
                
    print(f"Forbidden word hits (V9): {len(fb_hits)}")
    for h in fb_hits:
        print(f"  - {h[0]}: forbidden '{h[1]}' in '{h[2]}'")
    print(f"Ellipsis hits (G1): {len(ellipsis_hits)}")
    for d in ellipsis_hits:
        print(f"  - {d[0]}: ellipsis in '{d[1]}'")
        
    status = (len(fb_hits) == 0 and len(ellipsis_hits) == 0 and total_sentences >= 200 and total_sentences == expected_sentences and total_elements == expected_elements)
    print(f"Result for {lang}: {'PASS' if status else 'FAIL'}")
    all_green = all_green and status

# Kiểm tra Parity chéo giữa 4 ngôn ngữ
print("\n================================================================")
print("ĐỐI SOÁT PARITY CHÉO 1:1 (VN vs EN vs JA vs KO)")
print("================================================================")
parity_pass = True
vn_p = parsed_all['VN']

for lang in ['EN', 'JA', 'KO']:
    lp = parsed_all[lang]
    if len(lp) != len(vn_p):
        print(f"FAIL: Element count mismatch VN({len(vn_p)}) vs {lang}({len(lp)})")
        parity_pass = False
        continue
    mismatches = []
    for i in range(len(vn_p)):
        evn = vn_p[i]
        el = lp[i]
        if evn['kind'] != el['kind']:
            mismatches.append(f"Element {evn['id']}: Kind mismatch VN({evn['kind']}) vs {lang}({el['kind']})")
        if evn.get('role') != el.get('role'):
            mismatches.append(f"Element {evn['id']}: Role mismatch VN({evn.get('role')}) vs {lang}({el.get('role')})")
        svn = len(evn.get('sentences', []))
        sl = len(el.get('sentences', []))
        if svn != sl:
            mismatches.append(f"Element {evn['id']}: Sentence count mismatch VN({svn}) vs {lang}({sl})")
    if mismatches:
        print(f"FAIL Parity VN vs {lang} ({len(mismatches)} errors):")
        for m in mismatches[:10]:
            print(f"  - {m}")
        parity_pass = False
    else:
        loi_count = len([e for e in vn_p if e['kind'] == 'LOI'])
        print(f"PASS Parity VN vs {lang}: 100% {len(vn_p)} elements, {loi_count} LOI turns, {expected_sentences} sentences match 1:1")

all_pass = all_green and parity_pass
print(f"\n>>> FINAL QUALITY GATE: {'ALL GREEN - PASSED' if all_pass else 'FAILED'} <<<")
