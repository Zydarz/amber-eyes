import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
raw = open('01_KICH_BAN/Tap09/kichban_tap09_23102026.md', encoding='utf-8').read()
q = re.findall(r"'([^']{2,})'", raw)
print(f"Total {len(q)} quotes in VN:")
for i, item in enumerate(q, 1):
    print(f"  [{i}] {item}")
