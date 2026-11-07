# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for p in ['01_KICH_BAN/Tap10/kichban_tap10_23102026.md', '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md', '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md']:
    print(f"=== {p} ===")
    with open(p, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, l in enumerate(lines, 1):
        if '4.05' in l or 'Cameron không hề thuộc về' in l or 'Cameron does not belong' in l or 'Cameron은 The Company' in l:
            for j in range(max(0, i-2), min(len(lines), i+6)):
                print(f"  {j+1}: {lines[j].strip()}")
            break
