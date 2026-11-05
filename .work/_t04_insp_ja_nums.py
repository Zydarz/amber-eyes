#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — quét câu JA xem có token số đứng riêng không; và xem chữ JA của tập khác."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(__file__).resolve().parent


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


sent = json.loads((W / "_t04_sentences.json").read_text(encoding="utf-8"))
ja = sent["ja"]
print("=== token số đứng riêng trong câu JA ===")
found = 0
for eid, ss in ja.items():
    for s in ss:
        for tok in norm(s["text"]).split():
            if re.fullmatch(r"\d[\d.,]*", tok):
                print(" ", s["id"], tok, "|", s["text"][:70])
                found += 1
print("tổng:", found)

print()
print("=== file chữ JA của các tập khác trong .work ===")
for p in sorted(W.glob("_t0*_chu_ja.json")):
    print(" ", p.name, p.stat().st_size)

print()
print("=== file beat JA của các tập khác ===")
for p in sorted(W.glob("_t0*_beat_ja.json")):
    print(" ", p.name, p.stat().st_size)
