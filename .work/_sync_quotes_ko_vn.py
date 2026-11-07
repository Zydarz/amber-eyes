# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

vn_raw = open("01_KICH_BAN/Tap11/kichban_tap11_23102026.md", encoding="utf-8").read()
ko_raw = open("01_KICH_BAN/Tap11_KO/kichban_tap11_KO.md", encoding="utf-8").read()

vn_q = re.findall(r"'([^']{2,})'", vn_raw)
ko_q = re.findall(r"‘([^’]{2,})’", ko_raw)

print(f"VN quotes ({len(vn_q)}):")
for i, q in enumerate(vn_q, 1):
    print(f"  [{i}] {q}")

print(f"\nKO quotes ({len(ko_q)}):")
for i, q in enumerate(ko_q, 1):
    print(f"  [{i}] {q}")
