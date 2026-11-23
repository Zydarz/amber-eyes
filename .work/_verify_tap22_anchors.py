# -*- coding: utf-8 -*-
from pathlib import Path

files = {
    'VN': Path('01_KICH_BAN/Ho_So_Toi_Pham/Tap22/kichban_tap22_23102026.md'),
    'EN': Path('01_KICH_BAN/Ho_So_Toi_Pham/Tap22_EN/kichban_tap22_EN.md'),
    'JA': Path('01_KICH_BAN/Ho_So_Toi_Pham/Tap22_JA/kichban_tap22_JA.md'),
    'KO': Path('01_KICH_BAN/Ho_So_Toi_Pham/Tap22_KO/kichban_tap22_KO.md'),
}

def get_blocks(p):
    lines = p.read_text(encoding='utf-8').splitlines()
    blocks = {}
    curr_h = None
    curr_lines = []
    for l in lines:
        if l.startswith('**') and not l.startswith('**['):
            if curr_h:
                blocks[curr_h] = curr_lines
            curr_h = l.strip()
            curr_lines = []
        elif curr_h and l.strip() and not l.startswith('**[') and not l.startswith('##') and not l.startswith('*'):
            curr_lines.append(l.strip())
    if curr_h:
        blocks[curr_h] = curr_lines
    return blocks

target_indices = [3, 5, 8, 11, 13, 17, 21, 26, 28, 29]
# correspond to:
# 3: 1.07 (N1)
# 5: 1.10 (D)
# 8: 2.06 (D)
# 11: 2.10 (H)
# 13: 3.03 (C)
# 17: 3.07 (C)
# 21: 4.06 (D)
# 26: 4.11 (C)
# 28: 5.03 (D)
# 29: 5.04 (C)

data = {lang: get_blocks(p) for lang, p in files.items()}

for lang in files:
    blist = list(data[lang].items())
    print(f"=== {lang} ({len(blist)} blocks) ===")
    for idx in target_indices:
        h, l = blist[idx]
        print(f"[{idx}] {h[:25]}... (lines: {len(l)}) -> Last line: {l[-1][:40]}...")
