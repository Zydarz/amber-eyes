# -*- coding: utf-8 -*-
"""Update EN, JA, KO scripts and run full QC."""
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. READ VI SCRIPT to get sentence structure template
with open('01_KICH_BAN/Tap10/kichban_tap10_23102026.md', 'r', encoding='utf-8') as f:
    vi_text = f.read()

# Let's inspect where the insertions are by reading the original EN, JA, KO
en_path = '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md'
ja_path = '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md'
ko_path = '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md'

with open(en_path, 'r', encoding='utf-8') as f: en_lines = f.readlines()
with open(ja_path, 'r', encoding='utf-8') as f: ja_lines = f.readlines()
with open(ko_path, 'r', encoding='utf-8') as f: ko_lines = f.readlines()

print(f"Read lines: EN={len(en_lines)}, JA={len(ja_lines)}, KO={len(ko_lines)}")
