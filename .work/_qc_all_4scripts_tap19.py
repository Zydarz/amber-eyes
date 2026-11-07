# -*- coding: utf-8 -*-
"""Comprehensive 4-Language Quality Control (QC) for Tap 19 Scripts: VN, EN, JA, KO."""
import json, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK
import edition

files = [
    ('VN', '01_KICH_BAN/Tap19/kichban_tap19_23102026.md'),
    ('EN', '01_KICH_BAN/Tap19_EN/kichban_tap19_EN.md'),
    ('JA', '01_KICH_BAN/Tap19_JA/kichban_tap19_JA.md'),
    ('KO', '01_KICH_BAN/Tap19_KO/kichban_tap19_KO.md'),
]

forbidden = {
    'VN': ['máu', 'thi thể', 'xác chết', 'tự sát', 'cắt cổ', 'bóp cổ', 'khí độc', 'ngạt thở', 'đâm', 'trói', 'sát hại', 'diệt chủng', 'đầu độc', 'bỏ đói', 'móc áo'],
    'EN': ['blood', 'corpse', 'decapitat', 'strangl', 'suicide'],
    'JA': ['血液', '死体', '切断', '絞殺', '自殺', '毒殺'],
    'KO': ['혈흔', '시체', '교살', '자살', '참수'],
}

parsed_all = {}
all_green = True

print("================================================================")
print("BÁO CÁO KIỂM THỬ QC TOÀN DIỆN KỊCH BẢN TẬP 19 (4 NGÔN NGỮ)")
print("================================================================")

for lang, path in files:
    print(f"\n--- QC LANGUAGE: {lang} ({path}) ---")
    p = PK.parse_file(path)
    parsed_all[lang] = p
    
    total_elements = len(p)
    loi = [e for e in p if e['kind'] == 'LOI']
    total_sentences = sum(len(x.get('sentences', [])) for x in loi)
    total_words = sum(sum(s['words'] for s in x['sentences']) for x in loi)
    
    print(f"Elements: {total_elements}")
    print(f"LOI turns: {len(loi)}")
    print(f"Sentences: {total_sentences}")
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
        
    status = (len(fb_hits) == 0 and len(ellipsis_hits) == 0 and total_sentences == 210 and total_elements == 51)
    print(f"Result for {lang}: {'PASS' if status else 'FAIL'}")
    all_green = all_green and status

# Parity check between languages
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
        print(f"PASS Parity VN vs {lang}: 100% 51 elements, 32 LOI turns, 210 sentences match 1:1")

# Check configuration parity with edition.py
print("\n================================================================")
print("KIỂM TRA CẤU HÌNH PIPELINE (EDITION.PY EPISODES['19'])")
print("================================================================")
cfg = edition.EPISODES.get('19', {})
all_sentences = set()
for e in vn_p:
    if e['kind'] == 'LOI':
        for s in e['sentences']:
            all_sentences.add(s['id'])

cfg_pass = True
for skey in cfg.get('summary', ()):
    if skey in all_sentences:
        print(f"PASS: summary key '{skey}' exists in script")
    else:
        print(f"FAIL: summary key '{skey}' NOT FOUND in script!")
        cfg_pass = False

for ckey in [cfg.get('act1_cue'), cfg.get('silence_cue')]:
    if ckey:
        found = any(e['id'] == ckey for e in vn_p)
        if found:
            print(f"PASS: cue key '{ckey}' exists in script")
        else:
            print(f"FAIL: cue key '{ckey}' NOT FOUND in script!")
            cfg_pass = False

for n_id, n_role in cfg.get('n_element', {}).items():
    matching = [e for e in vn_p if e['id'] == n_id]
    if matching and matching[0].get('role') == 'N':
        print(f"PASS: n_element '{n_id}' mapped to '{n_role}' matches role N in script")
    else:
        print(f"FAIL: n_element '{n_id}' mismatch in script!")
        cfg_pass = False

print("\n================================================================")
print(f"KẾT QUẢ CUỐI CÙNG: {'ALL GREEN — ĐẠT 100% TIÊU CHUẨN MỚI' if (all_green and parity_pass and cfg_pass) else 'FAIL — CẦN ĐIỀU CHỈNH'}")
print("================================================================")
