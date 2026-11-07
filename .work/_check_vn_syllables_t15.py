# -*- coding: utf-8 -*-
"""Check Vietnamese syllable validity for Tap 15 VN."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('01_KICH_BAN/Tap15/kichban_tap15_23102026.md', encoding='utf-8') as f:
    text = f.read()

# Look for patterns like lowercase words with strange marks or known typos
lines = text.splitlines()
for idx, line in enumerate(lines):
    # Check for words with double tone marks or typos
    tokens = re.findall(r'\b[A-Za-zÀ-ỹĐđ]+\b', line)
    for t in tokens:
        # Check if word has consecutive consonants that don't exist in VN
        # Ex: 'trg', 'nghĩang', 'nhugn', 'hoacj'
        if re.search(r'[sptkmnbdgclvhr][jfrxs]', t.lower()):
            print(f"Line {idx+1}: nghi vấn lỗi gõ telex/vni '{t}' -> {line[:80]}")
        # Check odd letters
        if re.search(r'[a-z][A-ZÀ-Ỹ]', t):
            print(f"Line {idx+1}: nghi vấn dính chữ hoa thường '{t}' -> {line[:80]}")

print("Check finished.")
