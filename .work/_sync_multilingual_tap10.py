# -*- coding: utf-8 -*-
"""Update EN, JA, KO scripts of Tap 10 to 240 sentences and verify 1:1 parity."""
import os, sys, re, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

# 1. READ ORIGINAL EN, JA, KO SCRIPTS
en_path = '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md'
ja_path = '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md'
ko_path = '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md'

with open(en_path, 'r', encoding='utf-8') as f:
    en_raw = f.read()

with open(ja_path, 'r', encoding='utf-8') as f:
    ja_raw = f.read()

with open(ko_path, 'r', encoding='utf-8') as f:
    ko_raw = f.read()

# Let's inspect elements in EN, JA, KO
p_en = PK.parse_file(en_path)
p_ja = PK.parse_file(ja_path)
p_ko = PK.parse_file(ko_path)

print(f"Original counts -> EN: {sum(len(e.get('sentences',[])) for e in p_en if e['kind']=='LOI')}, JA: {sum(len(e.get('sentences',[])) for e in p_ja if e['kind']=='LOI')}, KO: {sum(len(e.get('sentences',[])) for e in p_ko if e['kind']=='LOI')}")
