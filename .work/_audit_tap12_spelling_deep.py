# -*- coding: utf-8 -*-
"""Comprehensive spellcheck and linguistic audit for Tap 12 Vietnamese script."""
import sys, io, re, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

path = '01_KICH_BAN/Tap12/kichban_tap12_23102026.md'
p = PK.parse_file(path)
loi = [e for e in p if e['kind'] == 'LOI']

print(f"Tổng số phần tử: {len(p)} | Số lượt LOI: {len(loi)}")

# 1. Punctuation and Typography Checks
punct_issues = []
for e in loi:
    for s in e['sentences']:
        txt = s['text']
        sid = s['id']
        
        # Double space
        if '  ' in txt:
            punct_issues.append((sid, "DOUBLE_SPACE", "Hai khoảng trắng liên tiếp", txt))
            
        # Space before punctuation
        m_sbp = re.search(r'\s+([,.:;?!])', txt)
        if m_sbp:
            punct_issues.append((sid, "SPACE_BEFORE_PUNCT", f"Khoảng trắng trước dấu '{m_sbp.group(1)}'", txt))
            
        # Missing space after punctuation (excluding decimals e.g. 1.5)
        m_msa = re.search(r'([a-zA-ZÀ-ỹ])([,;:])([a-zA-ZÀ-ỹ])', txt)
        if m_msa:
            punct_issues.append((sid, "NO_SPACE_AFTER_PUNCT", f"Thiếu khoảng trắng sau dấu: '{m_msa.group()}'", txt))
            
        # Lowercase after full stop / question mark / exclamation mark
        m_cap = re.search(r'[.?!]\s+([a-zà-ỹ])', txt)
        if m_cap:
            punct_issues.append((sid, "LOWERCASE_AFTER_SENTENCE_END", f"Chữ thường sau dấu kết câu: '{m_cap.group()}'", txt))
            
        # Ellipsis
        if '...' in txt or '…' in txt:
            punct_issues.append((sid, "ELLIPSIS", "Dấu ba chấm vi phạm G1", txt))
            
        # Unbalanced quotes
        c_open = txt.count('“')
        c_close = txt.count('”')
        if c_open != c_close:
            punct_issues.append((sid, "UNBALANCED_QUOTES", f"Mở: {c_open} vs Đóng: {c_close}", txt))

print(f"1. Lỗi dấu câu & định dạng khoảng trắng: {len(punct_issues)}")
for err in punct_issues:
    print(f"   [{err[0]}] {err[1]}: {err[2]} -> \"{err[3]}\"")

# 2. Confusing Pairs and Spelling Rules
confusing_patterns = [
    (r'\bchuẩn đoán\b', 'chẩn đoán'),
    (r'\bsơ xuất\b', 'sơ suất'),
    (r'\bsuất sắc\b', 'phải là xuất sắc'),
    (r'\bxuất sứ\b', 'xuất xứ'),
    (r'\bgiành cho\b', 'dành cho'),
    (r'\bdành giật\b', 'giành giật'),
    (r'\btham quan\b(?=.*(chức vụ|hối lộ))', 'tham quan (địa danh) vs tham quan (quan lại)'),
    (r'\bthăm quan\b', 'tham quan'),
    (r'\bchắp vá\b', 'chắp vá'),
    (r'\btrắp vá\b', 'chắp vá'),
    (r'\bchông gai\b', 'chông gai'),
    (r'\btrông gai\b', 'chông gai'),
    (r'\bvô hình chung\b', 'vô hình trung'),
    (r'\btựu chung\b', 'tựu trung'),
    (r'\bchững chạc\b', 'chững chạc'),
    (r'\bchững chạc\b', 'chững chạc'),
    (r'\bxán lạn\b', 'sáng lạng -> xán lạn'),
    (r'\bsáng lạng\b', 'xán lạn'),
    (r'\bnhậm chức\b', 'nhậm chức'),
    (r'\bnhận chức\b', 'nhận chức'),
    (r'\bgiấu giếm\b', 'giấu giếm'),
    (r'\bdấu diếm\b', 'giấu giếm'),
    (r'\btập triệt\b', 'tập dượt'),
]

spelling_issues = []
for e in loi:
    for s in e['sentences']:
        txt = s['text']
        sid = s['id']
        for pat, note in confusing_patterns:
            m = re.search(pat, txt, re.IGNORECASE)
            if m:
                spelling_issues.append((sid, "CONFUSING_WORD", f"'{m.group()}' ({note})", txt))

print(f"2. Cặp từ dễ nhầm lẫn & chính tả: {len(spelling_issues)}")
for err in spelling_issues:
    print(f"   [{err[0]}] {err[1]}: {err[2]}")

print("AUDIT COMPLETE.")
