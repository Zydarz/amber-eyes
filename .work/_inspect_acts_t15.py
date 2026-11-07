# -*- coding: utf-8 -*-
"""Inspect Tap 15 VN content by act."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('01_KICH_BAN/Tap15/kichban_tap15_23102026.md', encoding='utf-8') as f:
    text = f.read()

acts = text.split('## HỒI ')
for i in range(1, len(acts)):
    header = acts[i].split('\n')[0]
    lines = [l.strip() for l in acts[i].split('\n') if l.strip() and not l.startswith('**[') and not l.startswith('---')]
    print(f"Hồi {i}: {header} ({len(lines)} đoạn/lượt nói)")
