# -*- coding: utf-8 -*-
"""Spellcheck and grammar pass for Tap 15 VN."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('01_KICH_BAN/Tap15/kichban_tap15_23102026.md', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Check for common Vietnamese spelling mistakes
typo_checks = [
    ('giằng xé', 'giằng xé'), ('giành giật', 'giành giật'),
    ('sơ suất', 'sơ xuất'), ('xuất sắc', 'suất sắc'),
    ('chắp vá', 'chắp vá'), ('chực chờ', 'chực chờ'),
    ('trao chuốt', 'trau chuốt'), ('chẩn đoán', 'chuẩn đoán'),
    ('xúc tích', 'súc tích'), ('bàng quan', 'bàng quang'),
    ('vô hình chung', 'vô hình trung'), ('cọ sát', 'cọ xát'),
    ('tham quan', 'thăm quan'), ('chân mạng', 'chân mệnh'),
]

for correct, wrong in typo_checks:
    for idx, l in enumerate(lines):
        if wrong in l.lower() and wrong != correct:
            print(f"Cảnh báo lỗi dùng từ tại dòng {idx+1}: '{wrong}' -> nên dùng '{correct}': {l.strip()}")

# Print lines with quotes to verify quote spelling
print("\n=== CÁC CÂU TRÍCH DẪN TRONG TẬP 15 VN ===")
for idx, l in enumerate(lines):
    quotes = re.findall(r'[‘“\'](.*?)[’”\']', l)
    if quotes:
        for q in quotes:
            if len(q) > 3:
                print(f"Line {idx+1}: ‘{q}’")
