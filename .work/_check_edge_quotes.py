# -*- coding: utf-8 -*-
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = [
    ('VN', '01_KICH_BAN/Tap10/kichban_tap10_23102026.md'),
    ('EN', '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md'),
    ('JA', '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md'),
    ('KO', '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md'),
]

for lang, path in files:
    print(f"\n=== Checking lines in {lang}: {path} ===")
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, l in enumerate(lines, 1):
        s = l.strip()
        if not s or s.startswith('#') or s.startswith('*') or s.startswith('-'):
            continue
        if s.startswith('“') or s.startswith('"'):
            print(f"  Line {idx} STARTS WITH QUOTE: {s[:60]}...")
        if s.endswith('”') or s.endswith('"'):
            print(f"  Line {idx} ENDS WITH QUOTE: ...{s[-60:]}")
