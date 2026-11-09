import re, sys
sys.stdout.reconfigure(encoding='utf-8')
raw = open('01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md', encoding='utf-8').read()
quotes = re.findall(r"'([^']{2,})'", raw)
print(f"Total {len(quotes)} quotes in VN:")
for i, q in enumerate(quotes, 1):
    print(f"  [{i}] {q}")
