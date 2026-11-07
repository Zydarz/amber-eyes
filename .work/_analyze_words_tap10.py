# -*- coding: utf-8 -*-
"""Phân tích chi tiết ngữ từ tiếng Việt trong kịch bản Tập 10."""
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

# Kiểm tra kỹ từng câu có từ nào khả nghi
suspicious_checks = [
    (r'\b(chôn dấu|che dấu|dấu giếm)\b', 'giấu/dấu'),
    (r'\b(sử lý|xử dụng)\b', 'xử lý / sử dụng'),
    (r'\b(giành|dành)\b', 'kiểm tra ngữ cảnh dành/giành'),
    (r'\b(nổi|nỗi)\b', 'kiểm tra ngữ cảnh nổi/nỗi'),
    (r'\b(sáp nhập|xáp nhập)\b', 'sáp nhập'),
    (r'\b(rạng rỡ|rạng rở)\b', 'rạng rỡ'),
    (r'\b(chắp vá|chắp vá)\b', 'chắp vá'),
    (r'\b(giãy giụa|giẫy giụa)\b', 'giãy giụa'),
    (r'\b(dày dạn|dày dặn)\b', 'dày dạn/dày dặn'),
    (r'\b(vỗ về|vổ về)\b', 'vỗ về'),
    (r'\b(ngỡ ngàng|ngở ngàng)\b', 'ngỡ ngàng'),
    (r'\b(bàng hoàng|bàng hoàng)\b', 'bàng hoàng'),
]

for pat, desc in suspicious_checks:
    matches = []
    for sid, role, text in sentences:
        m = re.findall(pat, text, re.IGNORECASE)
        if m:
            matches.append((sid, m, text))
    if matches:
        print(f"\n--- {desc} ({len(matches)} vị trí) ---")
        for sid, m, text in matches:
            print(f"  [{sid}] ({m}): {text}")

# In toàn bộ các từ chứa dấu ngã để rà soát hỏi/ngã
nga_words = set()
for sid, role, text in sentences:
    words = re.findall(r'[a-zA-ZÀ-ỹ]+', text)
    for w in words:
        if any(c in w for c in 'ãẽĩõũỹÃẼĨÕŨỸđĐ') or any(c in w for c in 'ãẽĩõũỹẵặẳằắẫậẩầấẽẹẻềếỗộổồốỡợởờớũụủừứỹỵỷỳ'):
            # word has tilde (dấu ngã)
            if re.search(r'[ãẽĩõũỹẵẫẽễỗỡũữỹ]', w, re.IGNORECASE):
                nga_words.add(w.lower())

print(f"\nCác từ có dấu ngã trong văn bản ({len(nga_words)} từ):")
print(', '.join(sorted(list(nga_words))))
