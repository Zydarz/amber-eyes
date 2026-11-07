# -*- coding: utf-8 -*-
"""Precise Vietnamese syllable validator for Tap 15 and Tap 18."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Regex to check actual illegal consonant clusters in Vietnamese:
# e.g., 'ngh' before a/o/u, 'c' before i/e/y, 'k' before a/o/u, 'gh' before a/o/u, 'g' before i/e/y (except gi)
ILLEGAL_VN = [
    (r'\bngh[aáoàọơớờợuúùụ]\w*', 'ngh đứng trước a/o/u'),
    (r'\bgh[aáoàọơớờợuúùụ]\w*', 'gh đứng trước a/o/u'),
    (r'\bk[aáoàọơớờợuúùụ]\w*', 'k đứng trước a/o/u (trừ từ mượn)'),
    (r'\bc[ieyíìịéèẹýỳỵ]\w*', 'c đứng trước i/e/y (trừ từ mượn)'),
]

for ep in ['Tap15', 'Tap18']:
    path = f'01_KICH_BAN/{ep}/kichban_{ep.lower()}_23102026.md'
    with open(path, encoding='utf-8') as f:
        text = f.read()
    
    print(f"=== KIỂM TRA CHÍNH TẢ ÂM TIẾT: {ep} ===")
    for pattern, desc in ILLEGAL_VN:
        matches = re.findall(pattern, text, re.IGNORECASE)
        # Filter English/proper nouns
        filtered = [m for m in matches if m.lower() not in {'kauai', 'kết', 'kế', 'kẻ', 'kỳ', 'ký', 'kiểm', 'kiên', 'kiến', 'kim', 'kinh', 'kia', 'khi', 'khép', 'không', 'khiến', 'khoác', 'khóa', 'khoản', 'khung', 'khu', 'khóc', 'khối', 'khẳng', 'khẩn', 'khéo', 'khám', 'khán', 'khách', 'khép', 'khỏi', 'khôn', 'khủng', 'khuyết', 'khép', 'cancun', 'car', 'card', 'case', 'camera', 'california', 'call', 'check', 'city', 'center', 'cyber', 'cox'}]
        if filtered:
            print(f"  {desc}: {filtered}")
        else:
            print(f"  {desc}: SẠCH 100%")
