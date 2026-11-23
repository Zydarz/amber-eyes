# -*- coding: utf-8 -*-
"""Comprehensive Spelling, Punctuation, and Lexicon Audit for Episode 44 in VN, EN, JA."""
import sys, re
sys.path.insert(0, '.work')
import parse_kichban as PK

files = [
    ('VN', '01_KICH_BAN/Ho_So_Toi_Pham/Tap44/kichban_tap44_19112026.md'),
    ('EN', '01_KICH_BAN/Ho_So_Toi_Pham/Tap44_EN/kichban_tap44_EN.md'),
    ('JA', '01_KICH_BAN/Ho_So_Toi_Pham/Tap44_JA/kichban_tap44_JA.md'),
]

print("==================================================================")
print("AUDIT BÁO CÁO CHÍNH TẢ, NGÔN TỪ & DẤU CÂU TẬP 44 (VN - EN - JA)")
print("==================================================================")

for lang, fpath in files:
    print(f"\n--- KIỂM TRA NGÔN NGỮ: {lang} ---")
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Brackets and quotes balance
    parens = text.count('(') - text.count(')')
    brackets = text.count('[') - text.count(']')
    quotes_vn = text.count('“') - text.count('”')
    quotes_ja = text.count('「') - text.count('」')
    
    print(f"Cân bằng dấu ngoặc đơn ( ): {parens} ({'ĐẠT' if parens == 0 else 'LỖI'})")
    print(f"Cân bằng dấu ngoặc vuông [ ]: {brackets} ({'ĐẠT' if brackets == 0 else 'LỖI'})")
    if lang == 'VN':
        print(f"Cân bằng dấu ngoặc kép “ ”: {quotes_vn} ({'ĐẠT' if quotes_vn == 0 else 'LỖI'})")
    if lang == 'JA':
        print(f"Cân bằng dấu ngoặc vuông 「 」: {quotes_ja} ({'ĐẠT' if quotes_ja == 0 else 'LỖI'})")

    # 2. Check line endings
    p = PK.parse_file(fpath)
    loi = [e for e in p if e['kind'] == 'LOI']
    bad_endings = []
    repeated_words = []
    
    for e in loi:
        for s in e['sentences']:
            txt = s['text'].strip()
            sid = s['id']
            # Check endings
            if lang in ['VN', 'EN']:
                if txt[-1] not in '.!?;:\"”\'':
                    bad_endings.append((sid, txt))
            elif lang == 'JA':
                if txt[-1] not in '。！？…」』”"':
                    bad_endings.append((sid, txt))
            
            # Check accidental immediate repeat of words (e.g., "trong trong", "the the")
            words = txt.split()
            for w_idx in range(len(words) - 1):
                w1 = re.sub(r'[^\w]', '', words[w_idx].lower())
                w2 = re.sub(r'[^\w]', '', words[w_idx + 1].lower())
                if w1 and w2 and w1 == w2:
                    # Ignore intentional Vietnamese reduplications if any, but flag for review
                    repeated_words.append((sid, f"{words[w_idx]} {words[w_idx+1]}", txt))

    print(f"Dấu kết thúc câu cuối dòng: {len(bad_endings)} lỗi ({'ĐẠT' if len(bad_endings) == 0 else 'CẦN SỬA'})")
    for b in bad_endings:
        print(f"  - {b[0]}: {b[1]}")
        
    print(f"Từ lặp liên tiếp: {len(repeated_words)} vị trí")
    for r in repeated_words:
        print(f"  - {r[0]}: lặp '{r[1]}' trong câu: \"{r[2]}\"")

print("\nAudit completed.")
