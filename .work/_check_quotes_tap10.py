import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for lang, path in [
    ('VN', '01_KICH_BAN/Tap10/kichban_tap10_23102026.md'),
    ('EN', '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md'),
    ('JA', '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md'),
    ('KO', '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md'),
]:
    t = open(path, encoding='utf-8').read()
    # Find all quoted phrases
    if lang == 'VN':
        q = re.findall(r"'([^']{2,})'", t)
    elif lang == 'EN':
        q = re.findall(r"'([^']{2,})'", t)
    elif lang == 'JA':
        q = re.findall(r"「([^」]{2,})」", t)
    elif lang == 'KO':
        q = re.findall(r"[‘'“]([^’'”]{2,})[’'”]", t)
    print(f'{lang}: {len(q)} quotes found')
