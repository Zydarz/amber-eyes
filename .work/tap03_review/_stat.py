import json
import sys
from collections import Counter

p = sys.argv[1]
els = json.load(open(p, encoding="utf-8"))
print("total elements:", len(els))
print("kinds:", Counter(e["kind"] for e in els))
words = 0
sent = 0
print("--- LOI elements ---")
for e in els:
    if e["kind"] != "LOI":
        continue
    w = sum(s["words"] for s in e["sentences"])
    words += w
    sent += len(e["sentences"])
    first = e["text"][:46].replace("\n", " ")
    print(f'{e["id"]:>6} {e["role"]:<3} {w:>4}w {len(e["sentences"]):>3}s  {first}')
print("--- totals ---")
print("words:", words, "| sentences:", sent)
r = words / 3.30
print(f"speech est @3.30 w/s = {r:.0f}s = {r/60:.1f} min")
r2 = words / 3.47
print(f"speech est @3.47 w/s = {r2:.0f}s = {r2/60:.1f} min")
# roles per act
print("--- N-role elements (need N_ELEMENT) ---")
for e in els:
    if e["kind"] == "LOI" and e["role"] == "N":
        print("  N:", e["id"])
