import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
CACHE = ROOT / ".work" / "_src_cache"

URL = {}
for m in CACHE.glob("*.meta"):
    p = m.read_text(encoding="utf-8").split("\t")
    if len(p) > 1:
        URL[m.stem] = p[1]
bodies = [(URL.get(b.stem, b.stem),
           " ".join(b.read_text(encoding="utf-8", errors="replace").split()))
          for b in CACHE.glob("*.txt") if b.stat().st_size]

CHECKS = [
    (r"trap door|closet", "3-03 nap ham o tu hay phong ngu"),
    (r"FBI Academy|Quantico", "5-07 hoc vien FBI"),
    (r"pawn shop|pawnbroker", "2-08 tiem cam do"),
    (r"thrift|secondhand|used goods", "2-08 tiem cam do (biet mau)"),
    (r"1972|1967 to 1978|first known murder", "1-05 gan mot thap ky"),
]
for pat, tag in CHECKS:
    print(f"\n=== /{pat}/  [{tag}]")
    rx = re.compile(pat, re.I)
    n = 0
    for url, txt in bodies:
        for s in re.split(r"(?<=[.!?])\s+", txt):
            s2 = " ".join(s.split())
            if 20 < len(s2) < 380 and rx.search(s2):
                print(f"   [{url[:58]}] {s2}")
                n += 1
                if n >= 4:
                    break
        if n >= 4:
            break
    if n == 0:
        print("   (khong co ket qua)")

print("\n\n=== CAU 1.06#5 / 1.06#4 / 2.07#4 / 3.05#1 / 5.06#2 (nguyen van) ===")
data = json.loads((ROOT / ".work/script_tap06.json").read_text(encoding="utf-8-sig"))
S = {s["id"]: s["text"] for el in data if el.get("kind") == "LOI" for s in el.get("sentences", [])}
for i in ["1.06#5", "1.06#4", "2.07#4", "3.05#1", "3.06#2", "5.06#2", "3.07#1"]:
    print(f"\n{i}: {S.get(i, 'KHONG TON TAI')}")
