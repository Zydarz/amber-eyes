import re, json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('01_KICH_BAN/Tap04/kichban_tap04_23102026.md', encoding='utf-8') as f:
    lines = f.readlines()

print("--- LINES WITH QUOTES ---")
for i, line in enumerate(lines, 1):
    if any(q in line for q in ['“', '”', "'", '‘', '’']):
        print(f"L{i}: {line.strip()}")
