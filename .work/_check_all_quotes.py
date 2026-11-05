import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

vn_raw = open('01_KICH_BAN/Tap07/kichban_tap07_23102026.md', encoding='utf-8').read()
en_raw = open('01_KICH_BAN/Tap07_EN/kichban_tap07_EN.md', encoding='utf-8').read()
ja_raw = open('01_KICH_BAN/Tap07_JA/kichban_tap07_JA.md', encoding='utf-8').read()
ko_raw = open('01_KICH_BAN/Tap07_KO/kichban_tap07_KO.md', encoding='utf-8').read()

vn_q = re.findall(r"'([^']{2,})'", vn_raw)
en_q = re.findall(r"‘([^’]{2,})’", en_raw)
ja_q = re.findall(r"「([^」]{2,})」", ja_raw)
ko_q = re.findall(r"‘([^’]{2,})’", ko_raw)

print(f"VN quotes ({len(vn_q)}):", vn_q)
print(f"EN quotes ({len(en_q)}):", en_q)
print(f"JA quotes ({len(ja_q)}):", ja_q)
print(f"KO quotes ({len(ko_q)}):", ko_q)
