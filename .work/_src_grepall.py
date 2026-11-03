#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grep nhieu regex qua toan bo cache nguon, in ra dung doan khop + ten file.

Usage: py -3 .work/_src_grepall.py <file_regexes.txt> [max_hits_per_regex]
file_regexes.txt: moi dong = "regex<TAB>nhan_dien"
"""
import re
import sys
from pathlib import Path

CACHE = Path(r"D:/TEST/Gax/amber-eyes/.work/_src_cache")

URL_BY_HASH = {}


def load_meta():
    for m in CACHE.glob("*.meta"):
        parts = m.read_text(encoding="utf-8").split("\t")
        url = parts[1] if len(parts) > 1 else ""
        URL_BY_HASH[m.stem] = url


def main():
    pats = []
    for line in Path(sys.argv[1]).read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        bits = line.split("\t")
        pats.append((bits[0], bits[1] if len(bits) > 1 else ""))
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    load_meta()
    bodies = []
    for b in CACHE.glob("*.txt"):
        if b.stat().st_size == 0:
            continue
        bodies.append((b.stem, URL_BY_HASH.get(b.stem, b.stem),
                       b.read_text(encoding="utf-8", errors="replace")))
    for pat, tag in pats:
        print(f"\n=== [{tag}] /{pat}/")
        try:
            rx = re.compile(pat, re.I)
        except re.error as e:
            print("   REGEX ERROR", e)
            continue
        n = 0
        for stem, url, txt in bodies:
            for s in re.split(r"(?<=[.!?])\s+|\n", txt):
                s2 = " ".join(s.split())
                if 18 < len(s2) < 420 and rx.search(s2):
                    print(f"   [{url[:70]}] {s2}")
                    n += 1
                    if n >= cap:
                        break
            if n >= cap:
                break
        if n == 0:
            print("   (khong co ket qua)")


if __name__ == "__main__":
    main()
