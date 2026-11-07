# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for ep in ['01', '02', '07', '08']:
    fname = f'01_KICH_BAN/Tap{ep}/kichban_tap{ep}_22102026_v2.md' if ep == '01' else f'01_KICH_BAN/Tap{ep}/kichban_tap{ep}_22102026.md' if ep == '02' else f'01_KICH_BAN/Tap{ep}/kichban_tap{ep}_23102026.md'
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    # find lines with quotes
    matches = re.findall(r'^[^\n]*[“"”\'][^\n]*$', text, re.M)
    print(f"Tap {ep} has {len(matches)} lines with quotes. Examples:")
    for m in matches[:3]:
        print("  ", m.strip())
