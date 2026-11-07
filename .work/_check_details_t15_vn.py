# -*- coding: utf-8 -*-
"""Detailed spelling and lexical analysis for Tap 15 Vietnamese script."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('01_KICH_BAN/Tap15/kichban_tap15_23102026.md', encoding='utf-8') as f:
    lines = f.readlines()

print("=== KIỂM TRA TỪ LẶP LẠI TRONG TẬP 15 VN ===")
for i, l in enumerate(lines):
    words = re.findall(r'\b([A-Za-zÀ-ỹ]+)\b', l)
    for j in range(len(words)-1):
        if words[j].lower() == words[j+1].lower():
            print(f"Line {i+1}: lặp từ '{words[j]}' -> {l.strip()[:80]}...")

print("\n=== KIỂM TRA TÊN RIÊNG VÀ ĐỊA DANH TRONG TẬP 15 VN ===")
names = ['Jodi', 'Arias', 'Travis', 'Alexander', 'Mesa', 'Arizona', 'Yreka', 'California', 'Maricopa', 'Flores', 'Martinez', 'Nurmi']
for name in names:
    count = sum(l.count(name) for l in lines)
    # Check lowercase occurrences
    lower_count = sum(len(re.findall(r'\b' + name.lower() + r'\b', l)) for l in lines)
    print(f"  {name:10}: {count} lần (dạng thường: {lower_count})")

print("\n=== KIỂM TRA CÁC CÂU CÓ DẤU CHẤM HỎI HOẶC CHẤM THAN ===")
for i, l in enumerate(lines):
    if '?' in l or '!' in l:
        print(f"Line {i+1}: {l.strip()[:80]}...")
