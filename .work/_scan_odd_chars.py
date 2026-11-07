# -*- coding: utf-8 -*-
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

for lang, fpath in [
    ('VN', '01_KICH_BAN/Tap19/kichban_tap19_23102026.md'),
    ('EN', '01_KICH_BAN/Tap19_EN/kichban_tap19_EN.md'),
    ('JA', '01_KICH_BAN/Tap19_JA/kichban_tap19_JA.md'),
    ('KO', '01_KICH_BAN/Tap19_KO/kichban_tap19_KO.md')
]:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    # Check for curly quotes or weird quotes inside words
    odd_quotes = re.findall(r'[a-zA-Z0-9]+[“”"’`]+[a-zA-Z0-9]+', text)
    if odd_quotes:
        print(f'{lang} odd quotes inside words: {odd_quotes}')
    else:
        print(f'{lang} quotes inside words: CLEAN')
