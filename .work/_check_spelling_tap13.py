# -*- coding: utf-8 -*-
"""Script rà soát chính tả chi tiết toàn bộ kịch bản Tập 13."""
import sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap13/kichban_tap13_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

sentences = []
for e in loi:
    for s in e['sentences']:
        sentences.append((s['id'], e['role'], s['text']))

print(f"Tổng số câu kịch bản Tập 13: {len(sentences)}")

# 1. Kiểm tra khoảng trắng và dấu câu
spacing_errors = []
for sid, role, text in sentences:
    if '  ' in text:
        spacing_errors.append((sid, "Khoảng trắng kép (double space)", text))
    if re.search(r'\s[,\.\?!;:]', text):
        spacing_errors.append((sid, "Khoảng trắng trước dấu câu", text))
    m = re.findall(r'[,;:][^\s”\"’\'\)]', text)
    if m:
        spacing_errors.append((sid, f"Dấu câu dính chữ: {m}", text))

print(f"\n1. Lỗi khoảng trắng và dấu câu: {len(spacing_errors)}")
for err in spacing_errors:
    print(f"  - [{err[0]}] {err[1]}: {err[2]}")

# 2. Kiểm tra các lỗi chính tả phổ biến
typo_patterns = [
    (r'\bxắp xếp\b', 'sắp xếp'),
    (r'\bsản suất\b', 'sản xuất'),
    (r'\bsơ xài\b', 'sơ sài'),
    (r'\bsảy ra\b', 'xảy ra'),
    (r'\bdằng xé\b', 'giằng xé'),
    (r'\bchôn dấu\b', 'chôn giấu'),
    (r'\bche dấu\b', 'che giấu'),
    (r'\bdấu giếm\b', 'giấu giếm'),
    (r'\bsử lý\b', 'xử lý'),
    (r'\bxử dụng\b', 'sử dụng'),
    (r'\bchuẩn đoán\b', 'chẩn đoán'),
    (r'\bxuất sứ\b', 'xuất xứ'),
]

found_typos = []
for sid, role, text in sentences:
    for pat, fix in typo_patterns:
        if re.search(pat, text, re.IGNORECASE):
            found_typos.append((sid, pat, fix, text))

print(f"\n2. Lỗi chính tả từ vựng phổ biến: {len(found_typos)}")
for err in found_typos:
    print(f"  - [{err[0]}] Phát hiện '{err[1]}' -> Gợi ý sửa: '{err[2]}'\n    Câu: {err[3]}")

# 3. Kiểm tra tính chuẩn xác của các tên riêng
proper_names = [
    'Jennifer Pan', 'Huei Hann Pan', 'Bich Ha Pan', 'Daniel Wong',
    'Lenford Crawford', 'David Mylvaganam', 'William Goetz', 'Bill Goetz',
    'Markham', 'Ontario', 'Helen', 'SickKids', 'Ryerson', 'Toronto',
    'Mary Ward', 'Cary Boswell'
]

print("\n3. Kiểm tra sự xuất hiện của các tên riêng:")
for name in proper_names:
    count = sum(1 for _, _, text in sentences if name.lower() in text.lower())
    print(f"  - {name}: {count} lần")

# 4. Kiểm tra các cặp từ ngữ cảnh (dành/giành, nổi/nỗi)
suspicious_checks = [
    (r'\b(giành|dành)\b', 'kiểm tra ngữ cảnh dành/giành'),
    (r'\b(nổi|nỗi)\b', 'kiểm tra ngữ cảnh nổi/nỗi'),
]

for pat, desc in suspicious_checks:
    matches = []
    for sid, role, text in sentences:
        m = re.findall(pat, text, re.IGNORECASE)
        if m:
            matches.append((sid, m, text))
    if matches:
        print(f"\n4. {desc} ({len(matches)} vị trí):")
        for sid, m, text in matches:
            print(f"  [{sid}] ({m}): {text}")

# 5. Rà soát toàn bộ từ có dấu ngã
nga_words = set()
for sid, role, text in sentences:
    words = re.findall(r'[a-zA-ZÀ-ỹ]+', text)
    for w in words:
        if re.search(r'[ãẽĩõũỹẵẫẽễỗỡũữỹ]', w, re.IGNORECASE):
            nga_words.add(w.lower())

print(f"\n5. Các từ có dấu ngã trong văn bản ({len(nga_words)} từ):")
print(', '.join(sorted(list(nga_words))))

# 6. Kiểm tra lặp từ liền kề
dup_words = []
for sid, role, text in sentences:
    words = text.split()
    for i in range(len(words)-1):
        w1 = re.sub(r'[^\w]', '', words[i]).lower()
        w2 = re.sub(r'[^\w]', '', words[i+1]).lower()
        if w1 and w1 == w2 and w1 not in ['ngày', 'đêm', 'từng']:
            dup_words.append((sid, w1, text))

print(f"\n6. Lặp từ liền kề: {len(dup_words)}")
for dw in dup_words:
    print(f"  [{dw[0]}] lặp '{dw[1]}': {dw[2]}")
