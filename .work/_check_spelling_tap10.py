# -*- coding: utf-8 -*-
"""Script rà soát chính tả chi tiết toàn bộ kịch bản Tập 10."""
import sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

sentences = []
for e in loi:
    for s in e['sentences']:
        sentences.append((s['id'], e['role'], s['text']))

print(f"Tổng số câu kịch bản Tập 10: {len(sentences)}")

# 1. Kiểm tra khoảng trắng và dấu câu
spacing_errors = []
for sid, role, text in sentences:
    if '  ' in text:
        spacing_errors.append((sid, "Khoảng trắng kép (double space)", text))
    if re.search(r'\s[,\.\?!;:]', text):
        spacing_errors.append((sid, "Khoảng trắng trước dấu câu", text))
    # Dấu phẩy / chấm không có khoảng trắng theo sau (trừ cuối câu hoặc đóng ngoặc)
    m = re.findall(r'[,;:][^\s”\"’\'\)]', text)
    if m:
        spacing_errors.append((sid, f"Dấu câu dính chữ: {m}", text))

print(f"\n1. Lỗi khoảng trắng và dấu câu: {len(spacing_errors)}")
for err in spacing_errors:
    print(f"  - [{err[0]}] {err[1]}: {err[2]}")

# 2. Kiểm tra các cặp từ dễ sai chính tả trong tiếng Việt
common_confusions = [
    (r'\bxắp xếp\b', 'sắp xếp'),
    (r'\bsử lý\b', 'xử lý (nếu là xử lý tình huống/vụ án)'),
    (r'\bsản suất\b', 'sản xuất'),
    (r'\bsơ xài\b', 'sơ sài'),
    (r'\bxơ xác\b', 'xơ xác / sơ xác'),
    (r'\bsảy ra\b', 'xảy ra'),
    (r'\bdằng xé\b', 'giằng xé'),
    (r'\bgiằng xé\b', 'giằng xé (đúng)'),
    (r'\bchôn dấu\b', 'chôn giấu'),
    (r'\bche dấu\b', 'che giấu'),
    (r'\bdấu giếm\b', 'giấu giếm'),
    (r'\bnguôi ngoai\b', 'nguôi ngoai (đúng)'),
    (r'\bchớp nhoáng\b', 'chớp nhoáng (đúng)'),
    (r'\bhoang mang\b', 'hoang mang (đúng)'),
    (r'\bbàng hoàng\b', 'bàng hoàng (đúng)'),
    (r'\bbàng hoàng\b', 'bàng hoàng'),
    (r'\brụng rời\b', 'rụng rời'),
    (r'\bgiãi bày\b', 'giãi bày'),
    (r'\btrần trụi\b', 'trần trụi'),
    (r'\bngỡ ngàng\b', 'ngỡ ngàng'),
    (r'\bbỡ ngỡ\b', 'bỡ ngỡ'),
    (r'\bvẫy vùng\b', 'vẫy vùng'),
    (r'\bgiãy giụa\b', 'giãy giụa'),
]

# Kiểm tra các từ sai chính tả thực sự
typo_patterns = [
    (r'\bxắp xếp\b', 'sắp xếp'),
    (r'\bsản suất\b', 'sản xuất'),
    (r'\bsơ xài\b', 'sơ sài'),
    (r'\bsảy ra\b', 'xảy ra'),
    (r'\bdằng xé\b', 'giằng xé'),
    (r'\bchôn dấu\b', 'chôn giấu'),
    (r'\bche dấu\b', 'che giấu'),
    (r'\bdấu giếm\b', 'giấu giếm'),
    (r'\bgiành giật\b', 'giành giật'),
    (r'\btranh d откры\b', 'tranh giành'),
    (r'\bchẩn đoán\b', 'chẩn đoán (đúng)'),
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

# 3. Kiểm tra tính chuẩn xác của các tên riêng và thuật ngữ nước ngoài
proper_names = [
    'Colleen Stan', 'Cameron Hooker', 'Janice Hooker', 'Red Bluff', 'Tehama',
    'Eugene', 'Oregon', 'Westwood', 'California', 'Interstate 5', 'Martin Seligman',
    'Chris Hatcher', 'The Company', 'The Simple Gifts of Life', 'Marie Elizabeth Spannhake'
]

print("\n3. Kiểm tra sự xuất hiện của các tên riêng:")
name_counts = {}
for name in proper_names:
    count = sum(1 for _, _, text in sentences if name.lower() in text.lower())
    name_counts[name] = count
    print(f"  - {name}: {count} lần")

# 4. Kiểm tra các từ có ký tự lạ hoặc lỗi gõ phím tiếng Việt (vd: uô, ươ, aas, oos...)
unusual_patterns = [
    r'[a-zA-Z][0-9]',  # chữ dính số
    r'\b[a-z]*[A-Z][a-z]*[A-Z][a-z]*\b', # lạc chữ hoa giữa từ
    r'[^\s\w\.,\?!;:\-\–—\(\)“”\"\'’\/%]', # ký tự lạ ngoài dấu câu
]

weird_chars = []
for sid, role, text in sentences:
    for pat in unusual_patterns:
        m = re.findall(pat, text)
        if m:
            weird_chars.append((sid, pat, m, text))

print(f"\n4. Ký tự bất thường / lỗi gõ: {len(weird_chars)}")
for err in weird_chars:
    print(f"  - [{err[0]}] {err[2]}: {err[3]}")
