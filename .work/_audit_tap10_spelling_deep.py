# -*- coding: utf-8 -*-
"""Comprehensive spellcheck and linguistic audit for Tap 10 Vietnamese script."""
import sys, io, re, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

path = '01_KICH_BAN/Tap10/kichban_tap10_23102026.md'
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
    (r'\bgiành riêng\b', 'dành riêng'),
    (r'\bdành giật\b', 'giành giật'),
    (r'\bdành lại\b', 'giành lại (quyền lợi/tự do)'),
    (r'\bdãy dụa\b', 'giãy giụa'),
    (r'\bchăn trở\b', 'trăn trở'),
    (r'\bhụt hẫn\b', 'hụt hẫng'),
    (r'\bbàng hoảng\b', 'bàng hoàng'),
    (r'\bdày vò\b', 'giày vò (hoặc dằn vặt)'),
    (r'\bdằn vặt\b', None), # valid
    (r'\bgiằng xé\b', None), # valid
    (r'\bdằng xé\b', 'giằng xé'),
    (r'\btàn cốc\b', 'tàn khốc'),
    (r'\bman rợn\b', 'man rợ'),
    (r'\btựu chung\b', 'tựu trung'),
    (r'\bcứu dỗi\b', 'cứu rỗi'),
    (r'\bcứu rổi\b', 'cứu rỗi'),
    (r'\bcắn dứt\b', 'cắn rứt'),
    (r'\bcắn rức\b', 'cắn rứt'),
    (r'\bngỡ ngàn\b', 'ngỡ ngàng'),
    (r'\bngỡ nghàng\b', 'ngỡ ngàng'),
    (r'\bchấn thương\b', None), # valid
    (r'\btrấn thương\b', 'chấn thương'),
    (r'\btrân trọng\b', None), # valid
    (r'\bchân trọng\b', 'trân trọng'),
    (r'\brực rỡ\b', None), # valid
    (r'\bdực dỡ\b', 'rực rỡ'),
    (r'\brực dỡ\b', 'rực rỡ'),
    (r'\bphẫn nộ\b', None), # valid
    (r'\bphẩn nộ\b', 'phẫn nộ'),
    (r'\bthấu xuất\b', 'thấu suốt'),
    (r'\btoan tính\b', None), # valid
    (r'\bngẫu nhiên\b', None), # valid
    (r'\bngẩu nhiên\b', 'ngẫu nhiên'),
    (r'\brạn nứt\b', None), # valid
    (r'\bdạn nứt\b', 'rạn nứt'),
    (r'\bdơi rụng\b', 'rơi rụng'),
    (r'\brơi rụng\b', None), # valid
    (r'\bchập chững\b', None), # valid
    (r'\bchập chửng\b', 'chập chững'),
    (r'\bvỡ vụn\b', None), # valid
    (r'\bvở vụn\b', 'vỡ vụn'),
    (r'\bsụp đổ\b', None), # valid
    (r'\bxụp đổ\b', 'sụp đổ'),
    (r'\bxuy nghĩ\b', 'suy nghĩ'),
    (r'\bsuy nghĩ\b', None), # valid
    (r'\bsâu sắc\b', None), # valid
    (r'\bxâu sắc\b', 'sâu sắc'),
    (r'\bxâu xa\b', 'sâu xa'),
    (r'\bsâu xa\b', None), # valid
    (r'\bday dứt\b', None), # valid
]

spelling_issues = []
for e in loi:
    for s in e['sentences']:
        txt = s['text']
        sid = s['id']
        for pat, fix in confusing_patterns:
            if fix and re.search(pat, txt, re.IGNORECASE):
                spelling_issues.append((sid, pat, fix, txt))

print(f"2. Điểm nghi vấn từ ngữ dễ nhầm lẫn: {len(spelling_issues)}")
for err in spelling_issues:
    print(f"   [{err[0]}] Phát hiện '{err[1]}' -> Khuyến nghị: '{err[2]}' | Câu: \"{err[3]}\"")

# 3. Vocabulary & Syllable Isolation Check
KNOWN_FOREIGN = {
    'Colleen', 'Stan', 'Cameron', 'Hooker', 'Janice', 'Red', 'Bluff', 'Westwood', 'Eugene',
    'Riverside', 'Tehama', 'The', 'Company', 'Martin', 'Seligman', 'Patrick', 'Carnes',
    'Chris', 'Hatcher', 'Clarence', 'Knight', 'Richard', 'Tedeschi', 'Lawrence', 'Calhoun',
    'Gavin', 'de', 'Becker', 'Gifts', 'of', 'Life', 'Gift', 'Fear', 'Amber', 'Eyes', 'BGM',
    'LOI', 'ACT', 'Simple', 'County', 'Sheriff', 'Stockholm', 'Trauma', 'Bonding',
    'Learned', 'Helplessness', 'Dissociation', 'Compartmentalization', 'Post', 'Traumatic',
    'Growth', 'Normalcy', 'Bias', 'Relief', 'Blindspot', 'Sykes', 'Matza', 'Evan', 'Stark',
    'Lenore', 'Walker', 'Coercive', 'Control', 'God', 'Complex', 'Battered', 'Woman',
    'Syndrome', 'Moral', 'Injury', 'Disengagement', 'Pragmatic', 'Remorse', 'Full', 'Immunity',
    'Theory', 'Mind', 'Halo', 'Effect', 'PTG'
}

all_words = set()
for e in loi:
    for s in e['sentences']:
        tokens = re.findall(r'[a-zA-ZÀ-ỹ]+', s['text'])
        for t in tokens:
            all_words.add(t)

# Find words with telex artifacts or strange consonant clusters
telex_errors = []
for w in sorted(all_words):
    if w in KNOWN_FOREIGN:
        continue
    wl = w.lower()
    # If contains foreign chars
    if any(c in wl for c in 'fwzj'):
        # Check if it's an english phrase or foreign name
        if wl not in {x.lower() for x in KNOWN_FOREIGN}:
            telex_errors.append((w, "Chứa chữ f, w, z, j ngoài danh mục"))
    # Check double letters that are telex errors (like 's' at end followed by 's', or 'dd', 'aa', 'ee', 'oo', 'ww')
    for dbl in ['aa', 'ee', 'oo', 'dd', 'ww']:
        if dbl in wl:
            # check if not foreign
            if wl not in {x.lower() for x in KNOWN_FOREIGN}:
                telex_errors.append((w, f"Chứa chuỗi telex lặp: '{dbl}'"))

print(f"3. Nghi vấn lỗi gõ phím / ký tự lạ: {len(telex_errors)}")
for err in telex_errors:
    print(f"   Từ: '{err[0]}' -> {err[1]}")
