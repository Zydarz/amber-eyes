import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CACHE = Path(r"D:/TEST/Gax/amber-eyes/.work/_src_cache")

URL = {}
for m in CACHE.glob("*.meta"):
    p = m.read_text(encoding="utf-8").split("\t")
    if len(p) > 1:
        URL[m.stem] = p[1]

bodies = []
for b in CACHE.glob("*.txt"):
    if b.stat().st_size:
        bodies.append((URL.get(b.stem, b.stem),
                       " ".join(b.read_text(encoding="utf-8", errors="replace").split())))

PATS = [
    ("gas station", "2-13 tra tram xang"),
    ("gasoline", "2-13 xang"),
    ("filling station", "2-13 tram xang (biet mau)"),
    ("withdraw", "2-15 rut tien mat"),
    ("bank", "2-15 ngan hang"),
    ("cash", "2-15 tien mat"),
    ("restaurant", "2-14 nha hang"),
    ("diner", "2-14 quan an"),
]
for pat, tag in PATS:
    print(f"\n=== /{pat}/  [{tag}]")
    n = 0
    rx = re.compile(pat, re.I)
    for url, txt in bodies:
        for s in re.split(r"(?<=[.!?])\s+", txt):
            s2 = " ".join(s.split())
            if 20 < len(s2) < 400 and rx.search(s2):
                print(f"   [{url[:62]}] {s2}")
                n += 1
                if n >= 5:
                    break
        if n >= 5:
            break
    if n == 0:
        print("   (khong co ket qua)")
