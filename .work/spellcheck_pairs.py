# -*- coding: utf-8 -*-
"""Check Vietnamese spelling context for s/x, ch/tr, d/gi/r, l/n, hỏi/ngã."""

import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open(".work/all_sentences_vn.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect specific compound phrases and potential spelling pitfalls:
check_pairs = [
    # (correct regex, wrong regex, description)
    (r'giấu', r'dấu\s+(kín|giếm|vào|trong)', 'dấu -> giấu (động từ cất giấu)'),
    (r'dấu\s+(vết|hiệu|ấn|hỏi|chấm)', r'giấu\s+(vết|hiệu|ấn)', 'giấu -> dấu (danh từ dấu vết)'),
    (r'sốt\s+sắng', r'(xốt\s+xắng|xốt\s+sắng|sốt\s+xắng)', 'sốt sắng'),
    (r'rùng\s+mình', r'(dùng\s+mình|giùng\s+mình)', 'rùng mình'),
    (r'rụt\s+rè', r'(dụt\s+dè|giụt\s+giè)', 'rụt rè'),
    (r'trơ\s+lì', r'(chơ\s+lì|trơ\s+lỳ|chơ\s+lỳ)', 'trơ lì'),
    (r'vỡ\s+vụn', r'vở\s+vụn', 'vỡ vụn'),
    (r'nỗi\s+(đau|sợ|hoang|lo|buồn|thương|kinh)', r'nổi\s+(đau|sợ|hoang|lo|buồn|thương|kinh)', 'nỗi (tâm trạng) vs nổi (nổi bật, nổi lên)'),
    (r'nỗ\s+lực', r'nổ\s+lực', 'nỗ lực'),
    (r'rạng\s+rỡ', r'(dạng\s+dỡ|dạng\s+rỡ|rạng\s+dỡ)', 'rạng rỡ'),
    (r'trĩu\s+nặng', r'(chĩu|trỉu|chỉu)\s+nặng', 'trĩu nặng'),
    (r'trần\s+trụi', r'(chần|trần)\s+(chụi|trụi)', 'trần trụi'),
    (r'chững\s+chạc', r'chứng\s+chạc', 'chững chạc'),
    (r'khuỵu', r'(khuỵ|khuỵo|khụy)', 'khuỵu'),
    (r'bàng\s+hoàng', r'bàng\s+hoàn\b', 'bàng hoàng vs bàng hoàn'),
    (r'bàng\s+quan', r'bàng\s+quang', 'bàng quan vs bàng quang'),
    (r'vô\s+hình\s+trung', r'vô\s+hình\s+chung', 'vô hình trung vs vô hình chung'),
    (r'chuẩn\s+xác', r'chuẩn\s+xát', 'chuẩn xác vs chuẩn xát'),
    (r'chạm\s+trán', r'chạm\s+tráng', 'chạm trán'),
    (r'nghiệp\s+vụ', r'nghiệp\s+vũ', 'nghiệp vụ'),
    (r'xảo\s+quyệt', r'sảo\s+quyệt', 'xảo quyệt'),
    (r'gián\s+đoạn', r'dán\s+đoạn', 'gián đoạn'),
    (r'xâm\s+phạm', r'sâm\s+phạm', 'xâm phạm'),
    (r'sơ\s+hở', r'xơ\s+hở', 'sơ hở'),
    (r'xúc\s+cảm', r'súc\s+cảm', 'xúc cảm'),
    (r'triệt\s+tiêu', r'chiệt\s+tiêu', 'triệt tiêu'),
    (r'trí\s+tuệ', r'chí\s+tuệ', 'trí tuệ'),
    (r'chứng\s+cứ', r'trứng\s+cứ', 'chứng cứ'),
]

errors_found = []
for correct, wrong, desc in check_pairs:
    for m in re.finditer(wrong, text, re.IGNORECASE):
        # find sentence
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 40)
        errors_found.append((desc, text[start:end]))

print(f"Targeted spelling checks completed. Potential errors flagged: {len(errors_found)}")
for e in errors_found:
    print(f"  FLAG: {e[0]} in context: ...{e[1]}...")
