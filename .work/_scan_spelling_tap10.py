import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load script
d = json.load(open('.work/script_tap10.json', encoding='utf-8'))
loi_elems = [e for e in d if e.get('kind') == 'LOI']

print(f"Tổng số lượt thoại LOI: {len(loi_elems)}")
all_sentences = []
for e in loi_elems:
    eid = e['id']
    role = e['role']
    for s in e['sentences']:
        all_sentences.append((eid, s['id'], role, s['text']))

print(f"Tổng số câu đọc: {len(all_sentences)}")

# Check rules
issues = []

# 1. Check double spaces
for eid, sid, role, text in all_sentences:
    if "  " in text:
        issues.append((sid, "DOUBLE_SPACE", "Khoảng trắng đôi trong câu", text))

# 2. Check space before punctuation
space_punct = re.compile(r'\s+[,.:;?!]')
for eid, sid, role, text in all_sentences:
    m = space_punct.search(text)
    if m:
        issues.append((sid, "SPACE_BEFORE_PUNCT", f"Khoảng trắng trước dấu câu '{m.group()}'", text))

# 3. Check punctuation at end of sentence
for eid, sid, role, text in all_sentences:
    stripped = text.strip()
    if not stripped.endswith(('.', '!', '?', '”', '"')):
        issues.append((sid, "NO_END_PUNCT", "Không kết thúc bằng dấu chấm/hỏi/than/ngoặc kép", text))

# 4. Check unmatched quotes
for eid, sid, role, text in all_sentences:
    open_q = text.count('“')
    close_q = text.count('”')
    if open_q != close_q:
        issues.append((sid, "UNMATCHED_QUOTES", f"Lệch dấu ngoặc kép: {open_q} mở vs {close_q} đóng", text))
    # single quotes
    sq = text.count("'")
    if sq % 2 != 0:
        issues.append((sid, "ODD_SINGLE_QUOTES", f"Số dấu nháy đơn lẻ: {sq}", text))

# 5. Check telex typing artifacts (e.g. repeated w, s, r, x, f, j)
telex_pattern = re.compile(r'\b[a-zA-ZÀ-ỹ]*(?:[a-z]{2,})*(?:ww|jj|ff|ss|rr|xx)[a-zA-ZÀ-ỹ]*\b', re.IGNORECASE)
for eid, sid, role, text in all_sentences:
    for word in text.split():
        clean_word = word.strip(' ,.:;?!"“”()\'’')
        # Skip valid English words like 'off', 'too', 'good', 'will', 'all', 'see', 'free', 'feel', etc.
        valid_eng = {'off', 'too', 'good', 'will', 'all', 'see', 'free', 'feel', 'creepy', 'crawling', 'coffee', 'success', 'boss', 'cross', 'across', 'speech', 'sweet', 'speed', 'green', 'street', 'meet', 'keep', 'sleep', 'deep', 'need', 'peer', 'beer', 'cheer', 'wheel', 'steer', 'week', 'fleet', 'sheet', 'greet', 'sweet'}
        if clean_word.lower() in valid_eng:
            continue
        # Check repeated characters that might be telex
        for art in ['ww', 'jj', 'aa', 'ee', 'oo', 'dd']:
            if art in clean_word.lower() and not any(clean_word.lower().startswith(p) for p in ['week', 'wood', 'feed', 'good', 'door', 'deep', 'meet', 'keep', 'seem', 'been', 'seen', 'peer']):
                # Could be telex error in Vietnamese word
                # Check if it contains Vietnamese diacritics with telex
                pass

# 6. Check common Vietnamese spelling confusions
# e.g., 'giành giật' vs 'dành', 'sơ suất' vs 'sơ xuất', 'chẩn đoán' vs 'chuẩn đoán', etc.
checks_spelling = [
    (r'\bchuẩn đoán\b', 'chẩn đoán'),
    (r'\bsơ xuất\b', 'sơ suất'),
    (r'\bxuất sắc\b', 'xuất sắc (đúng)'),
    (r'\bsuất sắc\b', 'sai chính tả (phải là xuất sắc)'),
    (r'\bdành giật\b', 'giành giật'),
    (r'\bgiành riêng\b', 'dành riêng'),
    (r'\bgiành cho\b', 'dành cho'),
    (r'\btiềm tàng\b', 'tiềm tàng (đúng)'),
    (r'\btrăn trở\b', 'trăn trở (đúng)'),
    (r'\bchăn trở\b', 'sai chính tả (phải là trăn trở)'),
    (r'\bgặp gỡ\b', 'gặp gỡ (đúng)'),
    (r'\bgặp gở\b', 'sai chính tả'),
    (r'\btàn khốc\b', 'tàn khốc (đúng)'),
    (r'\btàn cốc\b', 'sai chính tả'),
    (r'\bman rợ\b', 'man rợ (đúng)'),
    (r'\bman rợn\b', 'sai chính tả'),
    (r'\brùng mình\b', 'rùng mình (đúng)'),
    (r'\brùng rợn\b', 'rùng rợn (đúng)'),
    (r'\brùng rợn\b', 'rùng rợn (đúng)'),
    (r'\bhoang tưởng\b', 'hoang tưởng (đúng)'),
    (r'\bảo tưởng\b', 'ảo tưởng (đúng)'),
    (r'\bảo giác\b', 'ảo giác (đúng)'),
]

for pat, desc in checks_spelling:
    if 'sai' in desc:
        for eid, sid, role, text in all_sentences:
            if re.search(pat, text, re.IGNORECASE):
                issues.append((sid, "SPELLING_ERROR", desc, text))

# 7. Check diacritic placement on tone marks
# Vietnamese tone mark errors (hòa vs hoà, thủy vs thuỷ - both OK, but check broken characters)
broken_chars = ['', '\ufffd', '\u200b', '\ufeff']
for eid, sid, role, text in all_sentences:
    for bc in broken_chars:
        if bc in text:
            issues.append((sid, "BROKEN_CHAR", f"Ký tự rác/hỏng {repr(bc)}", text))

# 8. Check English spelling in script
proper_names = [
    ("Colleen Stan", r'\bColleen Stan\b'),
    ("Cameron Hooker", r'\bCameron Hooker\b'),
    ("Janice Hooker", r'\bJanice Hooker\b'),
    ("Red Bluff", r'\bRed Bluff\b'),
    ("Westwood", r'\bWestwood\b'),
    ("Eugene", r'\bEugene\b'),
    ("Riverside", r'\bRiverside\b'),
    ("Tehama", r'\bTehama\b'),
    ("The Company", r'\bThe Company\b'),
    ("Martin Seligman", r'\bMartin Seligman\b'),
    ("Patrick Carnes", r'\bPatrick Carnes\b'),
    ("Chris Hatcher", r'\bChris Hatcher\b'),
    ("Clarence Knight", r'\bClarence Knight\b'),
    ("Richard Tedeschi", r'\bRichard Tedeschi\b'),
    ("Lawrence Calhoun", r'\bLawrence Calhoun\b'),
    ("Gavin de Becker", r'\bGavin de Becker\b'),
]

print("\n--- KẾT QUẢ QUÉT LỖI KỸ THUẬT & CHÍNH TẢ BAN ĐẦU ---")
print(f"Tổng số vấn đề phát hiện: {len(issues)}")
for iss in issues:
    print(f"[{iss[0]}] {iss[1]}: {iss[2]}")
    print(f"     Nội dung: {iss[3]}")
