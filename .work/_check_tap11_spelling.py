import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Check raw lines of kichban_tap11_23102026.md
with open('01_KICH_BAN/Tap11/kichban_tap11_23102026.md', 'r', encoding='utf-8') as f:
    raw_lines = f.readlines()

print(f"Total raw lines: {len(raw_lines)}")

line_issues = []
for i, line in enumerate(raw_lines, 1):
    l = line.strip()
    if not l:
        continue
    # Mismatched quotes
    if l.count('“') != l.count('”'):
        line_issues.append((i, 'Mismatched curly quotes', l))
    if l.count('"') % 2 != 0:
        line_issues.append((i, 'Mismatched straight quotes', l))
    if l.count('(') != l.count(')'):
        line_issues.append((i, 'Mismatched parentheses', l))
    if l.count('[') != l.count(']'):
        line_issues.append((i, 'Mismatched brackets', l))
    # Double spaces in text
    if not l.startswith('|') and not l.startswith('#'):
        mid = re.sub(r'  $', '', l)
        if '  ' in mid:
            line_issues.append((i, 'Double space in text', l))
        m = re.findall(r'\s+[,.:;?!]', l)
        if m:
            line_issues.append((i, f'Space before punctuation {m}', l))
    # Stage direction unclosed
    if '*(' in l and ')*' not in l:
        line_issues.append((i, 'Unclosed stage direction', l))

print(f"Raw line issues: {len(line_issues)}")
for iss in line_issues:
    print(f"  Line {iss[0]} [{iss[1]}]: {iss[2]}")

# 2. Check parsed sentences
with open('.work/_tap11_sentences.json', 'r', encoding='utf-8') as f:
    sentences_data = json.load(f)

sent_issues = []
for item in sentences_data:
    s_obj = item['text']
    sid = s_obj.get('id', f"{item['elem_id']}#{item['s_idx']}")
    txt = s_obj.get('text', '')
    role = item['role']

    # Punctuation checks
    if re.search(r'\s+[,.:;?!]', txt):
        m = re.findall(r'\s+[,.:;?!]', txt)
        sent_issues.append((sid, f'Space before punctuation {m}', txt))

    # Punctuation without following space (except before quote, paren, dash, digit)
    m = re.findall(r'[,:;?!][^\s\"\'’”\)0-9–\-\\]', txt)
    if m:
        sent_issues.append((sid, f'Punctuation without space {m}', txt))

    # Period without following space
    m_dot = re.findall(r'\.[^\s\"\'’”\)0-9–\-\\]', txt)
    if m_dot:
        sent_issues.append((sid, f'Period without space (K9 abbreviation risk?): {m_dot}', txt))

    # Double dots
    if '..' in txt and '...' not in txt:
        sent_issues.append((sid, 'Double dot (..)', txt))

    # Ellipsis (G1 violation)
    if '...' in txt or '…' in txt:
        sent_issues.append((sid, 'G1 violation: Ellipsis (...) or (…)', txt))

    # Curly quotes
    if txt.count('“') != txt.count('”'):
        sent_issues.append((sid, 'Mismatched curly quotes', txt))

    # Terminal punct
    if not txt.endswith(('.', '!', '?', '”', '"')):
        sent_issues.append((sid, 'Sentence does not end with period/terminal punct', txt))

    # Repeated words check
    double_words = re.findall(r'\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]+)\s+\1\b', txt, re.IGNORECASE)
    if double_words:
        valid_doubles = {'từ', 'mãi', 'ngày', 'người', 'nhà', 'lớp', 'từng', 'chầm', 'lần', 'rất', 'xa'}
        bad = [w for w in double_words if w.lower() not in valid_doubles]
        if bad:
            sent_issues.append((sid, f'Unusual duplicated words: {bad}', txt))

    # Common Vietnamese confusion checks
    confusions = [
        ('chuẩn đoán', 'chẩn đoán'),
        ('sử lý', 'xử lý'),
        ('chia xẻ', 'chia sẻ'),
        ('sơ xuất', 'sơ suất'),
        ('suất sắc', 'xuất sắc'),
        ('bàng hoang', 'bàng hoàng'),
        ('huyễn hoạc', 'huyễn hoặc'),
        ('cứu dỗi', 'cứu rỗi'),
        ('rúng động', 'rúng động'),
        ('dúng động', 'rúng động'),
        ('chơ tráo', 'trơ tráo'),
        ('chơ cháo', 'trơ tráo'),
        ('xa sút', 'sa sút'),
        ('dăn đe', 'răn đe'),
        ('dào cản', 'rào cản'),
        ('quá dang', 'quá giang'),
    ]
    for wrong, right in confusions:
        if wrong in txt.lower():
            sent_issues.append((sid, f"Spelling confusion: '{wrong}' -> '{right}'", txt))

print(f"\nTotal sentence issues: {len(sent_issues)}")
for sid, err_type, txt in sent_issues:
    print(f"[{sid}] {err_type}\n  -> {txt}")
