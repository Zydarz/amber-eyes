import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/_tap10_sentences.json', 'r', encoding='utf-8') as f:
    raw_sentences = json.load(f)

sentences = []
for item in raw_sentences:
    s_obj = item['text']
    sid = s_obj.get('id', f"{item['elem_id']}#{item['s_idx']}")
    txt = s_obj.get('text', '')
    sentences.append({
        'id': sid,
        'role': item['role'],
        'text': txt,
        'words': s_obj.get('words', 0)
    })

print(f'Total sentences loaded: {len(sentences)}')

issues = []
for item in sentences:
    sid = item['id']
    txt = item['text']
    role = item['role']

    # 1. Space before punctuation
    if re.search(r'\s+[,.:;?!]', txt):
        m = re.findall(r'\s+[,.:;?!]', txt)
        issues.append((sid, f'Space before punctuation {m}', txt))

    # 2. Punctuation without following space (except before closing quotes/parens/dashes/digits)
    # Check for e.g. comma or period followed immediately by a letter
    m = re.findall(r'[,:;?!][^\s\"\'’”\)0-9–\-\\]', txt)
    if m:
        issues.append((sid, f'Punctuation without following space: {m}', txt))

    # Period followed immediately by a letter (potential missing space or abbreviation dot)
    m_dot = re.findall(r'\.[^\s\"\'’”\)0-9–\-\\]', txt)
    if m_dot:
        issues.append((sid, f'Period without space (K9 abbreviation risk?): {m_dot}', txt))

    # 3. Double dots
    if '..' in txt and '...' not in txt:
        issues.append((sid, 'Double dot (..)', txt))

    # 4. Ellipsis (G1 violation)
    if '...' in txt or '…' in txt:
        issues.append((sid, 'G1 violation: Ellipsis (...) or (…)', txt))

    # 5. Curly quotes count
    if txt.count('“') != txt.count('”'):
        issues.append((sid, f'Mismatched curly quotes ({txt.count("“")} open vs {txt.count("”")} close)', txt))

    # 6. Straight quotes count
    cnt_quote = txt.count('"')
    if cnt_quote % 2 != 0:
        issues.append((sid, f'Mismatched straight quotes ({cnt_quote} found)', txt))

    # 7. Parentheses count
    if txt.count('(') != txt.count(')'):
        issues.append((sid, 'Mismatched parentheses', txt))

    # 8. Ends with proper punct
    if not txt.endswith(('.', '!', '?', '”', '"')):
        issues.append((sid, 'Sentence does not end with period/punct', txt))

    # 9. Check repeated words
    double_words = re.findall(r'\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]+)\s+\1\b', txt, re.IGNORECASE)
    if double_words:
        valid_doubles = {'từ', 'mãi', 'ngày', 'người', 'nhà', 'lớp', 'từng', 'chầm', 'lần', 'rất'}
        bad = [w for w in double_words if w.lower() not in valid_doubles]
        if bad:
            issues.append((sid, f'Unusual duplicated words: {bad}', txt))

    # 10. Check common Vietnamese spelling confusions
    # e.g. 'chuẩn đoán' -> 'chẩn đoán'
    if 'chuẩn đoán' in txt.lower():
        issues.append((sid, "Spelling error: 'chuẩn đoán' -> 'chẩn đoán'", txt))
    if 'sử lý' in txt.lower():
        issues.append((sid, "Spelling error: 'sử lý' -> 'xử lý'", txt))
    if 'chia xẻ' in txt.lower():
        issues.append((sid, "Spelling error: 'chia xẻ' -> 'chia sẻ'", txt))
    if 'sơ xuất' in txt.lower():
        issues.append((sid, "Spelling error: 'sơ xuất' -> 'sơ suất'", txt))
    if 'xuất sắc' in txt.lower() and 'suất sắc' in txt.lower():
        issues.append((sid, "Spelling error: 'suất sắc'", txt))
    if 'giằng xé xé' in txt.lower():
        issues.append((sid, "Duplication typo: 'giằng xé xé' -> 'giằng xé'", txt))
    if 'thấu cảm cảm xúc' in txt.lower():
        issues.append((sid, "Duplication typo: 'thấu cảm cảm xúc'", txt))
    if 'bàng hoang' in txt.lower() and 'bàng hoàng' not in txt.lower():
        issues.append((sid, "Spelling typo: 'bàng hoang'", txt))
    if 'huyễn hoặc' not in txt.lower() and 'huyễn hoạc' in txt.lower():
        issues.append((sid, "Spelling typo: 'huyễn hoạc'", txt))

print(f'Total issues detected: {len(issues)}')
for sid, err_type, txt in issues:
    print(f'\n[{sid}] {err_type}\n  Content: {txt}')
