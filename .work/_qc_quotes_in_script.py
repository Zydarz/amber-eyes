#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V3/A9.2: cau trich tren hinh co nguyen van trong KICH BAN (JA) va (VN) khong?"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

JA = (ROOT / "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md").read_text(encoding="utf-8-sig")
VN = (ROOT / "01_KICH_BAN/Tap02/kichban_tap02_22102026.md").read_text(encoding="utf-8-sig")

norm = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t)
nja, nvn = norm(JA), norm(VN)

QUOTES = [
    ("3-21", "はい、しかし答えは分かりませんし、答え自体が重要でないことも確かです",
     "Có thể, nhưng chúng ta không biết câu trả lời, và cũng xác nhận rằng câu trả lời không quan trọng"),
    ("3-28", "俺は誰よりも上に立つ者だ…俺には手を届かせられない",
     "Tôi là kẻ đứng trên tất cả mọi người… không ai có thể chạm tới tôi"),
    ("4-08", "…軍服を着た男が闇の中に立ち、じっと自分を見つめていた…",
     "…một người đàn ông mặc quân phục đứng trong bóng tối, và nhìn chằm chằm vào mình…"),
    ("4-14", "まったく同じだ", "Hoàn toàn giống nhau"),
    ("4-15", "すべてが終わった", "Tất cả đã kết thúc"),
    ("5-10", "文末に置く点こそ小さいけれど、その点には実に多くの意味が込められています",
     "Đặt ở cuối câu thì dù nhỏ, nhưng điểm đó chứa rất nhiều ý nghĩa"),
]
print(f"{'shot':<7}{'trong kich ban JA':<22}{'trong kich ban VN':<22}")
for sid, ja, vn in QUOTES:
    a = norm(ja) in nja
    b = norm(vn) in nvn
    print(f"{sid:<7}{str(a):<22}{str(b):<22}")
    if not a:
        # gan nhat trong JA
        target = norm(ja)
        best = 0
        bi = -1
        for i in range(max(1, len(nja) - len(target))):
            m = sum(1 for x, y in zip(target, nja[i:i + len(target)]) if x == y)
            if m > best:
                best, bi = m, i
        if bi >= 0:
            print(f"        gan nhat JA {best}/{len(target)}: ...{nja[max(0, bi - 25):bi + len(target) + 25]}...")

print()
print("=== SO DOAT: co bao nhieu dau trich trong kich ban JA? ===")
q_ja = re.findall(r"'([^']{6,})'", JA)
print(f"  kich ban JA: {len(q_ja)} dau trich don")
print("=== SO DOAT: so cau trich tren hinh co nam trong kich ban JA ===")
shots = __import__("json").loads((ROOT / ".work/shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
n_all = sum(1 for s in shots for seg in s["segments"] for k, v in seg["elems"] if k == "quote")
print(f"  cau trich tren hinh: {n_all}")
