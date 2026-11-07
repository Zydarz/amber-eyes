import sys, json, re
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

script_file = Path('01_KICH_BAN/Tap12/kichban_tap12_23102026.md')
with open(script_file, 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Load parsed json
with open('.work/script_tap12.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

all_sentences = []
for el in elements:
    if 'sentences' in el:
        for s_idx, s_obj in enumerate(el['sentences'], 1):
            if isinstance(s_obj, dict):
                s_text = s_obj.get('text', '').strip()
                s_id = s_obj.get('id', f"{el['id']}#{s_idx}")
            else:
                s_text = str(s_obj).strip()
                s_id = f"{el['id']}#{s_idx}"
            role = el.get('role', '')
            act = el.get('act', 1)
            all_sentences.append((s_id, act, role, s_text))

print(f"Total elements: {len(elements)}")
print(f"Total spoken sentences: {len(all_sentences)}")

# 1. Check end punctuation
print("\n--- 1. KIỂM TRA DẤU KẾT CÂU ---")
no_end = []
for s_id, act, role, s in all_sentences:
    if not re.search(r'[.?!]["”\']?$', s):
        no_end.append((s_id, s))
print(f"Số câu thiếu dấu kết: {len(no_end)}")
for s_id, s in no_end:
    print(f"  {s_id}: {s}")

# 2. Check Ellipses (Rule G1)
print("\n--- 2. KIỂM TRA DẤU CHẤM LỬNG (G1) ---")
ellipses = []
for s_id, act, role, s in all_sentences:
    if '...' in s or '…' in s:
        ellipses.append((s_id, s))
print(f"Số câu vi phạm G1: {len(ellipses)}")
for s_id, s in ellipses:
    print(f"  {s_id}: {s}")

# Check any ellipsis in the entire markdown file
raw_ellipses = [i+1 for i, l in enumerate(raw_text.splitlines()) if '...' in l or '…' in l]
print(f"Dòng có dấu chấm lửng trong toàn bộ file: {raw_ellipses}")

# 3. Check Digits (Rule K7)
print("\n--- 3. KIỂM TRA CON SỐ / KÝ HIỆU (K7) ---")
digits_found = []
for s_id, act, role, s in all_sentences:
    nums = re.findall(r'\b\d+\b', s)
    if nums:
        digits_found.append((s_id, nums, s))
print(f"Số câu chứa chữ số: {len(digits_found)}")
for s_id, nums, s in digits_found:
    print(f"  {s_id} ({nums}): {s}")

# 4. Check double spaces or spacing around punctuation
print("\n--- 4. KIỂM TRA LỖI KHOẢNG TRẮNG VÀ DẤU CÂU ---")
spacing_issues = []
for s_id, act, role, s in all_sentences:
    if '  ' in s:
        spacing_issues.append((s_id, 'Double space', s))
    if re.search(r'\s+[,.:;?!]', s):
        spacing_issues.append((s_id, 'Space before punct', s))
    m = re.findall(r'([,;?!])([^\s"”\'\)])', s)
    # filter out decimal numbers
    m = [x for x in m if not (x[0] == ',' and x[1].isdigit())]
    if m:
        spacing_issues.append((s_id, f'Missing space after punct {m}', s))
print(f"Số lỗi khoảng trắng/dấu câu: {len(spacing_issues)}")
for s_id, err, s in spacing_issues:
    print(f"  {s_id} [{err}]: {s}")

# 5. Check Quotes pairing
print("\n--- 5. KIỂM TRA ĐÓNG MỞ NGOẶC KÉP ---")
quote_issues = []
for s_id, act, role, s in all_sentences:
    q_straight = s.count('"')
    q_left = s.count('“')
    q_right = s.count('”')
    if q_straight % 2 != 0:
        quote_issues.append((s_id, f'Mismatched straight quotes ({q_straight})', s))
    if q_left != q_right:
        quote_issues.append((s_id, f'Mismatched curly quotes (“={q_left}, ”={q_right})', s))
print(f"Số lỗi ngoặc kép: {len(quote_issues)}")
for s_id, err, s in quote_issues:
    print(f"  {s_id} [{err}]: {s}")

# 6. Check duplicate words
print("\n--- 6. KIỂM TRA LẶP TỪ BẤT THƯỜNG ---")
natural_redup = {'từ', 'mãi', 'ngày', 'người', 'dần', 'chầm', 'lần', 'rất', 'từng', 'năm', 'đêm'}
dup_issues = []
for s_id, act, role, text in all_sentences:
    words = text.split()
    for i in range(len(words) - 1):
        w1 = re.sub(r'[^\w\s]', '', words[i]).lower()
        w2 = re.sub(r'[^\w\s]', '', words[i+1]).lower()
        if w1 == w2 and w1 and w1 not in natural_redup:
            dup_issues.append((s_id, f"{words[i]} {words[i+1]}", text))
print(f"Số từ lặp bất thường: {len(dup_issues)}")
for s_id, pair, text in dup_issues:
    print(f"  [{s_id}] '{pair}': {text}")

# 7. Check confusing word pairs
print("\n--- 7. KIỂM TRA CÁC TỪ DỄ LẪN TRONG TIẾNG VIỆT ---")
confusing_patterns = [
    (r'\bsát nhập\b', 'sáp nhập'),
    (r'\bdấu diếm\b', 'giấu giếm'),
    (r'\bgiấu diếm\b', 'giấu giếm'),
    (r'\bdấu giếm\b', 'giấu giếm'),
    (r'\bvô hình chung\b', 'vô hình trung'),
    (r'\bxoay sở\b', 'xoay xở'),
    (r'\bchẩn đoán\b', 'chẩn đoán (kiểm tra context nếu là chuẩn đoán)'),
    (r'\bchuẩn đoán\b', 'chẩn đoán'),
    (r'\bthăm quan\b', 'tham quan'),
    (r'\bchắp vá\b', 'chắp vá'),
    (r'\bchấp vá\b', 'chắp vá'),
    (r'\btrăn trở\b', 'trăn trở'),
    (r'\bchăn chở\b', 'trăn trở'),
    (r'\bbạt vô âm tín\b', 'bặt vô âm tín'),
    (r'\btrực chờ\b', 'chực chờ'),
    (r'\bchực chờ\b', 'chực chờ'),
    (r'\bchải nghiệm\b', 'trải nghiệm'),
    (r'\btựu chung\b', 'tựu trung'),
    (r'\bsuông sẻ\b', 'suôn sẻ'),
    (r'\bchững chạt\b', 'chững chạc'),
    (r'\bchần trừ\b', 'chần chừ'),
    (r'\blãng mạng\b', 'lãng mạn'),
    (r'\blãng mạn\b', 'lãng mạn'),
    (r'\btỉ mỉ\b', 'tỉ mỉ'),
    (r'\btrơ trẽn\b', 'trơ trẽn'),
    (r'\bgiằn vặt\b', 'dằn vặt'),
    (r'\bdằng xé\b', 'giằng xé'),
    (r'\bsao nhãng\b', 'xao nhãng'),
    (r'\bbàng quang\b', 'bàng quan'),
    (r'\bcuồng tín\b', 'cuồng tín'),
    (r'\bhoang tưởng\b', 'hoang tưởng'),
    (r'\bquyến rũ\b', 'quyến rũ'),
]

for pattern, note in confusing_patterns:
    for s_id, act, role, text in all_sentences:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            print(f"  [{s_id}] Khớp '{m.group(0)}' -> {note}")
