# -*- coding: utf-8 -*-
"""Check spelling in the research document as well."""
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = '01_KICH_BAN/Tap10/NghienCuu_TamLy_BoSung_KichBan_Tap10.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Check confusing patterns
confusing_patterns = [
    (r'\bchuẩn đoán\b', 'chẩn đoán'),
    (r'\bsơ xuất\b', 'sơ suất'),
    (r'\bsuất sắc\b', 'phải là xuất sắc'),
    (r'\bxuất sứ\b', 'xuất xứ'),
    (r'\bgiành cho\b', 'dành cho'),
    (r'\bgiành riêng\b', 'dành riêng'),
    (r'\bdành giật\b', 'giành giật'),
    (r'\bdãy dụa\b', 'giãy giụa'),
    (r'\bchăn trở\b', 'trăn trở'),
    (r'\bhụt hẫn\b', 'hụt hẫng'),
    (r'\bbàng hoảng\b', 'bàng hoàng'),
    (r'\btàn cốc\b', 'tàn khốc'),
    (r'\bman rợn\b', 'man rợ'),
    (r'\btựu chung\b', 'tựu trung'),
    (r'\bcứu dỗi\b', 'cứu rỗi'),
    (r'\bcắn dứt\b', 'cắn rứt'),
    (r'\bthờơ\b', 'thờ ơ'),
]

issues = []
for pat, fix in confusing_patterns:
    m = re.findall(pat, text, re.IGNORECASE)
    if m:
        issues.append((pat, fix, len(m)))

print(f"Số điểm nghi vấn trong bản nghiên cứu: {len(issues)}")
for iss in issues:
    print(f"  {iss[0]} -> {iss[1]} (Số lần: {iss[2]})")
