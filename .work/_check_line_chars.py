# -*- coding: utf-8 -*-
"""Check invisible characters, trailing spaces, and character encoding in Tap 10 script."""
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = '01_KICH_BAN/Tap10/kichban_tap10_23102026.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Tổng số dòng trong kịch bản: {len(lines)}")

issues = []
for i, line in enumerate(lines):
    # Check invisible chars
    for ch in ['\u200b', '\u200c', '\u200d', '\ufeff', '\ufffd']:
        if ch in line:
            issues.append((i+1, "INVISIBLE_CHAR", f"Ký tự ẩn {repr(ch)}", line.strip()))
    # Check trailing whitespace (except empty lines)
    if line.rstrip('\r\n') != line.rstrip():
        # Trailing spaces at end of line
        issues.append((i+1, "TRAILING_SPACE", "Khoảng trắng thừa cuối dòng", line.strip()))

print(f"Số lỗi định dạng dòng: {len(issues)}")
for iss in issues:
    print(f"  Dòng {iss[0]}: {iss[1]} -> {iss[2]}")
