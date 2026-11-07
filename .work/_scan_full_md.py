# -*- coding: utf-8 -*-
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

paths = [
    '01_KICH_BAN/Tap10/kichban_tap10_23102026.md',
    '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md',
    '01_KICH_BAN/Tap10/kichban_tap10_EN.md',
    '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md',
    '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md',
    '01_KICH_BAN/Tap10/REVIEW_kichban_tap10_10chiau.md',
    '01_KICH_BAN/Tap10/REVIEW_kichban_tap10_multilingual.md'
]

for path in paths:
    print(f"\nScanning: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        # check broken chars
        for bc in ['\ufffd', '\u200b', '\ufeff']:
            if bc in line:
                print(f"  Line {idx}: Broken char {repr(bc)}")
        # check double space (exclude markdown indentation or table alignment)
        stripped = line.strip()
        if not stripped.startswith('|') and not stripped.startswith('#') and not stripped.startswith('-'):
            if '  ' in stripped:
                print(f"  Line {idx}: Double space in text: {stripped[:60]}...")
