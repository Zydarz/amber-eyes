import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

vn8 = open('01_KICH_BAN/Tap08/kichban_tap08_23102026.md', encoding='utf-8').read()
ko8 = open('01_KICH_BAN/Tap08_KO/kichban_tap08_KO.md', encoding='utf-8').read()

vn_q = re.findall(r"'([^']{2,})'", vn8)
ko_q = re.findall(r"'([^']{2,})'", ko8)

print(f"Tap 08 VN quotes ({len(vn_q)}):")
for i, q in enumerate(vn_q):
    print(f"  [{i+1}] VN: {q}")
    print(f"       KO: {ko_q[i] if i < len(ko_q) else 'MISSING'}")
