#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Doc nguoi canh quanh regex trong 1 URL da cache (dung de doc timeline).

Usage: py -3 .work/_src_ctx.py <url> <regex> [radius]
"""
import hashlib
import re
import sys
from pathlib import Path

CACHE = Path(r"D:/TEST/Gax/amber-eyes/.work/_src_cache")


def body(url):
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    p = CACHE / f"{key}.txt"
    if not p.exists():
        raise SystemExit("chua cache URL nay: " + url)
    return p.read_text(encoding="utf-8", errors="replace")


def main():
    url, pat = sys.argv[1], sys.argv[2]
    rad = int(sys.argv[3]) if len(sys.argv) > 3 else 500
    txt = " ".join(body(url).split())
    for m in re.finditer(pat, txt, re.I):
        a = max(0, m.start() - rad)
        b = min(len(txt), m.end() + rad)
        print("---")
        print(txt[a:b])


if __name__ == "__main__":
    main()
