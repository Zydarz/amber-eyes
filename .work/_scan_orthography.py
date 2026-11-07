# -*- coding: utf-8 -*-
import re, io, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = [
    '01_KICH_BAN/Tap15/kichban_tap15_23102026.md',
    '01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md',
    '01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md',
    '01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md',
    '01_KICH_BAN/Tap17/kichban_tap17_23102026.md',
    '01_KICH_BAN/Tap17_EN/kichban_tap17_EN.md',
    '01_KICH_BAN/Tap17_JA/kichban_tap17_JA.md',
    '01_KICH_BAN/Tap17_KO/kichban_tap17_KO.md'
]

for fp in files:
    content = Path(fp).read_text(encoding='utf-8')
    lines = content.splitlines()
    print(f"\n--- Checking: {fp} ---")
    issues = 0
    for i, line in enumerate(lines, 1):
        sline = line.strip()
        if not sline:
            continue
        # Double spaces (not tables)
        if not sline.startswith('|') and '  ' in sline:
            print(f"  [L{i}] Double space: {sline[:80]}")
            issues += 1
        # Unbalanced parentheses
        if sline.count('(') != sline.count(')'):
            print(f"  [L{i}] Unbalanced (): {sline[:80]}")
            issues += 1
        # Unbalanced square brackets
        if sline.count('[') != sline.count(']'):
            print(f"  [L{i}] Unbalanced []: {sline[:80]}")
            issues += 1
        # Unbalanced Japanese quotes
        if sline.count('「') != sline.count('」'):
            print(f"  [L{i}] Unbalanced 「」: {sline[:80]}")
            issues += 1
        if sline.count('『') != sline.count('』'):
            print(f"  [L{i}] Unbalanced 『』: {sline[:80]}")
            issues += 1
    if issues == 0:
        print("  -> No bracket/spacing anomalies found.")
