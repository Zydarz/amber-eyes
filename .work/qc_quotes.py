import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('01_KICH_BAN/Tap04/kichban_tap04_23102026.md', encoding='utf-8') as f:
    text = f.read()

for i, line in enumerate(text.splitlines(), 1):
    q_straight = line.count('"')
    q_curly_open = line.count('“')
    q_curly_close = line.count('”')
    if q_straight % 2 != 0:
        print(f"Line {i} straight: {line}")
    if q_curly_open != q_curly_close:
        print(f"Line {i} curly: {line}")
print("VN quote check complete")
