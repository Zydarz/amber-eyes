import sys, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

script_file = Path('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
with open(script_file, 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Load parsed json
with open('.work/script_tap10.json', 'r', encoding='utf-8') as f:
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

# 3. Check Digits (Rule K7)
print("\n--- 3. KIỂM TRA CON SỐ / KÝ HIỆU (K7) ---")
digits_found = []
for s_id, act, role, s in all_sentences:
    # Find numbers
    nums = re.findall(r'\b\d+\b', s)
    if nums:
        digits_found.append((s_id, nums, s))
print(f"Số câu chứa chữ số: {len(digits_found)}")
for s_id, nums, s in digits_found:
    print(f"  {s_id} ({nums}): {s}")

# 4. Check double spaces or spacing before punctuation
print("\n--- 4. KIỂM TRA LỖI KHOẢNG TRẮNG VÀ DẤU CÂU ---")
spacing_issues = []
for s_id, act, role, s in all_sentences:
    if '  ' in s:
        spacing_issues.append((s_id, 'Double space', s))
    if re.search(r'\s+[,.:;?!]', s):
        spacing_issues.append((s_id, 'Space before punct', s))
    # Missing space after punctuation (excluding decimal numbers or abbreviations)
    m = re.findall(r'([,;?!])([^\s"”\'\)])', s)
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

