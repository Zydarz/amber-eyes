# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('01_KICH_BAN/Tap10/kichban_tap10_23102026.md', encoding='utf-8') as f:
    lines = f.readlines()
line = lines[268]

for i, ch in enumerate(line[-15:]):
    print(i, repr(ch), ord(ch), hex(ord(ch)))
