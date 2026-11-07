# -*- coding: utf-8 -*-
"""Deep spell check and typography validation for Episode 10 scripts in 4 languages."""
import sys, os, io, re, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = {
    'VN': '01_KICH_BAN/Tap10/kichban_tap10_23102026.md',
    'EN': '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md',
    'JA': '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md',
    'KO': '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md',
}

def check_vietnamese(sentences):
    issues = []
    
    # Common VN spelling pairs
    spelling_checks = [
        (r'\bchuẩn đoán\b', 'chẩn đoán (y học dùng chẩn đoán)'),
        (r'\bsơ xuất\b', 'sơ suất'),
        (r'\bsuất sắc\b', 'phải là xuất sắc'),
        (r'\bxuất sứ\b', 'xuất xứ'),
        (r'\bgiành riêng\b', 'dành riêng'),
        (r'\bgiành cho\b', 'dành cho'),
        (r'\bdành giật\b', 'giành giật'),
        (r'\bdãy dụa\b', 'giãy giụa'),
        (r'\bchăn trở\b', 'trăn trở'),
        (r'\bhụt hẫn\b', 'hụt hẫng'),
        (r'\bvội vàng\b', None),
        (r'\bgặp gở\b', 'gặp gỡ'),
        (r'\bbàng hoàng\b', None),
        (r'\bbàng hoảng\b', 'bàng hoàng'),
        (r'\bday dứt\b', None),
        (r'\bdày vò\b', None),
        (r'\bgiày vò\b', None),
        (r'\blãnh cảm\b', None),
        (r'\btàn khốc\b', None),
        (r'\btàn cốc\b', 'tàn khốc'),
        (r'\bman rợn\b', 'man rợ'),
        (r'\btựu trung\b', None),
        (r'\btựu chung\b', 'tựu trung'),
    ]
    
    # Broken characters
    broken = ['\ufffd', '\u200b', '\ufeff']
    
    for sid, text, role in sentences:
        # 1. Double space
        if '  ' in text:
            issues.append((sid, 'DOUBLE_SPACE', 'Có 2 khoảng trắng liên tiếp', text))
            
        # 2. Space before punctuation
        m = re.search(r'\s+[,.:;?!]', text)
        if m:
            issues.append((sid, 'SPACE_BEFORE_PUNCT', f"Khoảng trắng trước '{m.group()}'", text))
            
        # 3. Missing space after punctuation (e.g. 'cô,tôi' or 'đó.Người')
        m2 = re.search(r'([a-zA-ZÀ-ỹ])([,;:])([a-zA-ZÀ-ỹ])', text)
        if m2:
            issues.append((sid, 'NO_SPACE_AFTER_PUNCT', f"Thiếu khoảng trắng sau dấu câu: '{m2.group()}'", text))
            
        # 4. Quotes matching
        curly_open = text.count('“')
        curly_close = text.count('”')
        if curly_open != curly_close:
            issues.append((sid, 'UNMATCHED_CURLY_QUOTES', f"Ngoặc kép cong lệch: {curly_open} mở '“' vs {curly_close} đóng '”'", text))
            
        straight_quotes = text.count('"')
        if straight_quotes % 2 != 0:
            issues.append((sid, 'UNMATCHED_STRAIGHT_QUOTES', f"Ngoặc kép thẳng lẻ: {straight_quotes}", text))
            
        # 5. End punctuation
        st = text.strip()
        if not st.endswith(('.', '!', '?', '”', '"')):
            issues.append((sid, 'NO_END_PUNCT', f"Không kết thúc bằng dấu chấm/hỏi/than/ngoặc kép: đuôi '{st[-5:]}'", text))
            
        # 6. Capitalization after dot
        m_cap = re.search(r'\.\s+([a-zà-ỹ])', text)
        if m_cap:
            issues.append((sid, 'LOWERCASE_AFTER_PERIOD', f"Chữ thường sau dấu chấm: '{m_cap.group()}'", text))
            
        # 7. Check spelling dictionary
        for pat, fix in spelling_checks:
            if fix and re.search(pat, text, re.IGNORECASE):
                issues.append((sid, 'SPELLING_ERROR', f"Nghi vấn sai từ: {fix}", text))
                
        # 8. Check broken characters
        for b in broken:
            if b in text:
                issues.append((sid, 'BROKEN_CHAR', f"Ký tự rác: {repr(b)}", text))
                
        # 9. Telex leftovers
        # Find words with suspicious double characters
        words = re.findall(r'[a-zA-ZÀ-ỹ0-9_]+', text)
        for w in words:
            wl = w.lower()
            # check telex duplicates in VN words
            for t_err in ['s\b', 'f\b', 'r\b', 'x\b', 'j\b']: # lone tone keys? no
                pass
            if any(dup in wl for dup in ['ww', 'jj', 'aa', 'ee', 'oo', 'dd']):
                # Filter out valid English/loanwords
                valid_words = {'good', 'door', 'week', 'wood', 'feed', 'deep', 'meet', 'keep', 'seem', 'been', 'seen', 'peer', 'beer', 'cheer', 'wheel', 'steer', 'fleet', 'sheet', 'greet', 'sweet', 'speech', 'speed', 'green', 'street', 'free', 'feel', 'creepy', 'crawling', 'coffee', 'success', 'boss', 'cross', 'across', 'weed', 'flee', 'bleed', 'breed', 'creed', 'greed', 'need', 'seed', 'reed', 'deed'}
                if wl not in valid_words and not any(wl.startswith(vw) for vw in ['week', 'wood', 'feed', 'good', 'door', 'deep', 'meet', 'keep']):
                    # Check if it has Vietnamese accents AND telex artifact
                    if re.search(r'[à-ỹ]', wl):
                        issues.append((sid, 'TELEX_ARTIFACT', f"Nghi vấn lỗi gõ telex trong từ: '{w}'", text))
                        
    return issues


def check_english(sentences):
    issues = []
    broken = ['\ufffd', '\u200b', '\ufeff']
    
    for sid, text, role in sentences:
        if '  ' in text:
            issues.append((sid, 'DOUBLE_SPACE', 'Double space detected', text))
        m = re.search(r'\s+[,.:;?!]', text)
        if m:
            issues.append((sid, 'SPACE_BEFORE_PUNCT', f"Space before punct '{m.group()}'", text))
        m2 = re.search(r'([a-zA-Z])([,;:])([a-zA-Z])', text)
        if m2:
            issues.append((sid, 'NO_SPACE_AFTER_PUNCT', f"Missing space after punct '{m2.group()}'", text))
            
        # Quotes matching
        open_q = text.count('“') + text.count('"')
        close_q = text.count('”') + text.count('"')
        if (open_q + close_q) % 2 != 0:
            issues.append((sid, 'UNMATCHED_QUOTES', f"Unmatched quotes", text))
            
        # Capitalization after period
        m_cap = re.search(r'\.\s+([a-z])', text)
        if m_cap:
            issues.append((sid, 'LOWERCASE_AFTER_PERIOD', f"Lowercase after period: '{m_cap.group()}'", text))
            
        # End punct
        st = text.strip()
        if not st.endswith(('.', '!', '?', '”', '"', "'")):
            issues.append((sid, 'NO_END_PUNCT', f"Sentence does not end with punctuation: '{st[-5:]}'", text))
            
        # First char capitalized
        if text and text[0].islower():
            issues.append((sid, 'FIRST_CHAR_LOWERCASE', f"First letter lowercase: '{text[:10]}'", text))
            
        # Repeated words
        m_rep = re.search(r'\b(the|in|to|of|that|and|is|was|for)\s+\1\b', text, re.IGNORECASE)
        if m_rep:
            issues.append((sid, 'REPEATED_WORD', f"Repeated word: '{m_rep.group()}'", text))
            
        for b in broken:
            if b in text:
                issues.append((sid, 'BROKEN_CHAR', f"Broken character {repr(b)}", text))
                
    return issues


def check_japanese(sentences):
    issues = []
    broken = ['\ufffd', '\u200b', '\ufeff']
    
    for sid, text, role in sentences:
        # Bracket matching 「 」
        open_b = text.count('「')
        close_b = text.count('」')
        if open_b != close_b:
            issues.append((sid, 'UNMATCHED_BRACKETS', f"Lệch ngoặc vuông: {open_b} mở vs {close_b} đóng", text))
            
        # Double spaces (rare in Japanese unless intentional)
        if '  ' in text:
            issues.append((sid, 'DOUBLE_SPACE', 'Double space in JA text', text))
            
        # End punct
        st = text.strip()
        if not st.endswith(('。', '！', '？', '」', '』', '…', '・')):
            issues.append((sid, 'NO_END_PUNCT_JA', f"Sentence does not end with Japanese punctuation: '{st[-3:]}'", text))
            
        for b in broken:
            if b in text:
                issues.append((sid, 'BROKEN_CHAR', f"Broken character {repr(b)}", text))
                
    return issues


def check_korean(sentences):
    issues = []
    broken = ['\ufffd', '\u200b', '\ufeff']
    
    for sid, text, role in sentences:
        if '  ' in text:
            issues.append((sid, 'DOUBLE_SPACE', 'Double space in KO text', text))
            
        m = re.search(r'\s+[,.:;?!]', text)
        if m:
            issues.append((sid, 'SPACE_BEFORE_PUNCT', f"Space before punct '{m.group()}'", text))
            
        # Quotes matching
        open_q = text.count('“') + text.count('‘')
        close_q = text.count('”') + text.count('’')
        if open_q != close_q:
            issues.append((sid, 'UNMATCHED_QUOTES_KO', f"Lệch ngoặc: {open_q} mở vs {close_q} đóng", text))
            
        # End punct
        st = text.strip()
        if not st.endswith(('.', '!', '?', '”', '’', '"', "'")):
            issues.append((sid, 'NO_END_PUNCT_KO', f"Sentence does not end with punctuation: '{st[-3:]}'", text))
            
        for b in broken:
            if b in text:
                issues.append((sid, 'BROKEN_CHAR', f"Broken character {repr(b)}", text))
                
    return issues


def main():
    print("=================================================================")
    print("RÀ SOÁT CHÍNH TẢ & QUY TẮC CHỮ VIẾT TOÀN DIỆN KỊCH BẢN TẬP 10")
    print("=================================================================")
    
    all_issues = {}
    
    for lang, path in files.items():
        p = PK.parse_file(path)
        loi = [e for e in p if e['kind'] == 'LOI']
        s_list = []
        for e in loi:
            for s in e['sentences']:
                s_list.append((s['id'], s['text'], e.get('role')))
                
        print(f"\n--- Đang quét ngôn ngữ: {lang} ({len(s_list)} câu) ---")
        if lang == 'VN':
            iss = check_vietnamese(s_list)
        elif lang == 'EN':
            iss = check_english(s_list)
        elif lang == 'JA':
            iss = check_japanese(s_list)
        elif lang == 'KO':
            iss = check_korean(s_list)
        else:
            iss = []
            
        all_issues[lang] = iss
        print(f"Số lỗi / điểm nghi vấn phát hiện: {len(iss)}")
        for item in iss:
            print(f"  [{item[0]}] {item[1]}: {item[2]}")
            print(f"      Text: {item[3]}")
            
    return all_issues

if __name__ == '__main__':
    main()
