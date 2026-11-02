#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tim 6 cau trich tren hinh trong kich ban JA Tap02."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

s = (ROOT / "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md").read_text(encoding="utf-8-sig")
norm = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’()（）\-—–…]", "", t)
ns = norm(s)

tests = [
    ("3-21", "はい、しかし答えは分かりませんし、答え自体が重要でないことも確かです"),
    ("3-28", "俺は誰よりも上に立つ者だ…俺には手を届かせられない"),
    ("4-08", "軍服を着た男が闇の中に立ち、じっと自分を見つめていた"),
    ("4-14", "まったく同じだ"),
    ("4-15", "すべてが終わった"),
    ("5-10", "文末に置く点こそ小さいけれど、その点には実に多くの意味が込められています"),
]
for sid, q in tests:
    core = norm(q)
    hit = core in ns
    print(f"{sid}: nguyen van trong kich ban JA = {hit}")
    if not hit:
        found = False
        for frag in [core[:12], core[-12:], core[len(core) // 2 - 6:len(core) // 2 + 7]]:
            if len(frag) < 4:
                continue
            i = ns.find(frag)
            if i >= 0:
                print(f"     ...{ns[max(0, i - 30):i + len(frag) + 30]}...")
                found = True
                break
        if not found:
            print("     KHONG tim thay cum nao khop")

print()
print("=== doi chieu bang VN (nguon cua bang shot JA) ===")
v = (ROOT / "01_KICH_BAN/Tap02/kichban_tap02.md").read_text(encoding="utf-8-sig")
nv = norm(v)
vn_tests = [
    ("3-21", "Có thể, nhưng chúng ta không biết câu trả lời"),
    ("3-28", "Tôi là kẻ đứng trên tất cả mọi người"),
    ("4-08", "một người đàn ông mặc quân phục"),
    ("4-14", "Hoàn toàn giống nhau"),
    ("4-15", "Tất cả đã kết thúc"),
    ("5-10", "Đặt ở cuối câu thì dù nhỏ"),
]
for sid, q in vn_tests:
    print(f"{sid}: trong kich ban VN = {norm(q) in nv}")
